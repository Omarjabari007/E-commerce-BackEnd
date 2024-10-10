from uuid import uuid4, UUID
from typing import Optional, Dict, List
from app.api.exceptions.GlobalException import ProductDoesNotExistException, OutOfStockException
from app.api.services.order_status import OrderStatusService
from app.api.services.product_service import ProductService
from app.models import Order, OrderItem
from decimal import Decimal
from fastapi import FastAPI, HTTPException, APIRouter, Query

product_service = ProductService()
order_status_service = OrderStatusService()

class OrderService:
    def __init__(self):
        self.orders: Dict[UUID, Order] = {}

  
    def create_order(self, order_items: List[OrderItem], user_id: Optional[UUID] = None) -> Order:
        total_price = Decimal(0)
        for index, item in enumerate(order_items):
            product = self.product_service.get_product(item.product_id)
            if product is None:
                raise ProductDoesNotExistException(index + 1)
            elif item.quantity > product.stock:
                raise OutOfStockException(index + 1)

            total_price += product.price * item.quantity
        
        status_id = order_status_service.get_order_status_by_name("pending")
        order = Order(
            id=uuid4(),
            total_price=total_price,
            status_id=status_id
        )
        
        self.orders.append(order)

        return order
        

        

        

