from uuid import uuid4, UUID
from pydantic import BaseModel, Field, EmailStr, validator
from typing import Optional
from decimal import Decimal
from datetime import datetime
from app.api.exceptions.GlobalException import (
    PriceValidationException,
    StockValidationException,
)


class Product(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()), description="Product ID !  ")
    name: str = Field(..., description="Product Name !  ")
    description: str = Field(None, description="Product Description ! ")
    price: Decimal = Field(..., description="Product Price !  ")
    stock: Optional[int] = Field(None, description="Stock Quantity ")
    isAvailable: bool = Field(default=True, description="Is Product Available ? ")

    @validator("price")
    def validate_price(cls, value):
        if value <= 0:
            raise PriceValidationException()
        return value

    @validator("stock")
    def validate_stock(cls, value):
        if value is not None and value < 0:
            raise StockValidationException()
        return value


class User(BaseModel):
    id: Optional[UUID] = Field(None, description="User ID Automatically Created . !  ")
    username: str = Field(..., description="User Name.")
    email: EmailStr = Field(..., description="The email address of the user.")
    hashed_password: str = Field(..., description="The Password of the user.")
    is_admin: bool = Field(False, description="Admin or not?")
    is_active: bool = Field(True, description="User active or not?")
    created_at: Optional[datetime] = Field(
        None, description="The date and time when the user was created."
    )
    updated_at: Optional[datetime] = Field(
        None, description="The date and time when the user was last updated."
    )

class Order(BaseModel):
    id: UUID = Field(default_factory=lambda: uuid4(), description="Order ID.")
    user_id: Optional[UUID] = Field(None, description="User ID connected to a user.") # references user, SET NULL on delete, on database implementation
    status_id: Optional[UUID] = Field(None, description="Status ID connected to an order_status.") # references order_status, SET NULL on delete, on database implementation
    total_price: Decimal = Field(..., description="Total price of the order.", gt=0, max_digits=10, decimal_places=2)
    created_at: datetime = Field(datetime.now, description="Time the order is created at.")
    updated_at: datetime = Field(None, description="Time of the last update for the order.")

class OrderStatus:
    id: UUID = Field(default_factory=lambda: uuid4(), description="order_status ID.")
    name: str = Field("pending", description="Name of the order_status.", unique=True)
    created_at: datetime = Field(datetime.now, description="Time the order_status is created at.")
    updated_at: datetime = Field(None, description="Time of the last update for the order_status.")

class OrderProduct:
    id: UUID = Field(default_factory=lambda: uuid4(), description="order_product ID.")
    order_id: Optional[UUID] = Field(None, description="Order ID connected to an order.") # references order, CASCADE on delete, on database implementation
    product_id: Optional[UUID] = Field(None, description="Product ID connected to an Product.") # references product, SET NULL on delete, on database implementation
    quantity: int = Field(..., description="Quantity of order_products.")
    created_at: datetime = Field(datetime.now, description="Time the order_product is created at.")
    updated_at: datetime = Field(None, description="Time of the last update for the order_product.")

class OrderItem:
    product_id: UUID = Field(..., description="The id of the product being ordered.")
    quantity: int = Field(1, description="The quantity of the product.")

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: UUID | None = None


class UserDTO(BaseModel):
    id: Optional[UUID] = Field(
        None, description="User ID. Automatically generated upon user creation."
    )
    username: str = Field(..., description="User Name.")
    email: EmailStr = Field(..., description="The email address of the user.")
    is_admin: bool = Field(False, description="Admin or not?")
    is_active: bool = Field(True, description="User active or not?")
    created_at: Optional[datetime] = Field(
        None, description="The date and time when the user was created."
    )
    updated_at: Optional[datetime] = Field(
        None, description="The date and time when the user was last updated."
    )

    class Config:
        orm_mode = True
        from_attributes = True
