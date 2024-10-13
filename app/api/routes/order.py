from uuid import UUID
from app.api.exceptions.GlobalException import OutOfStockException, ProductDoesNotExistException
from app.api.routes import status
from app.api.services.order_service import OrderService
from fastapi import FastAPI, HTTPException, APIRouter
from typing import List, Optional
from decimal import Decimal
from app.models import Order, OrderItem, OrderResponse, Product
from app.api.services.product_service import ProductService
from fastapi.responses import JSONResponse


router = APIRouter()
order_service = OrderService()

@router.post("/orders", response_model=Order)
def create_product(orderItems : List[OrderItem]):
    try:
        order = order_service.create_order(order_items= orderItems)
    except ProductDoesNotExistException as notExits:
        raise notExits
    except OutOfStockException as noStock:
        raise noStock
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {str(e)}")

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=order.dict(exclude={"updated_at"})
    )

@router.get("/orders/{order_id}", response_model=OrderResponse)
def get_order_details(order_id: UUID):
    try:
        order_details = order_service.get_order_by_id(order_id)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while fetching the order details.")
    
    return order_details


