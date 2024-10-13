from app.api.exceptions.GlobalException import OutOfStockException, ProductDoesNotExistException
from app.api.routes import status
from app.api.services.order_service import OrderService
from fastapi import FastAPI, HTTPException, APIRouter
from typing import List, Optional
from decimal import Decimal
from app.models import Order, OrderItem, Product
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
        content=order.dict(exclude={"created_at", "updated_at"})
    )

