from app.api.services.order_service import OrderService
from fastapi import FastAPI, HTTPException, APIRouter, Query, status
from typing import List, Optional
from decimal import Decimal
from app.models import Product
from app.api.services.product_service import ProductService

router = APIRouter()
order_service = OrderService()