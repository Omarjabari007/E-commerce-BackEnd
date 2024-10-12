from sqlalchemy import Column, String, Boolean, DateTime, Integer, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from app.db.database import Base
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional
from decimal import Decimal


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class UserDTO(BaseModel):
    username: str = Field(None)
    email: EmailStr = Field(None)
    password: str = Field(None)


class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    is_admin: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True
        arbitrary_types_allowed = True


class UserUpdateDTO(BaseModel):
    username: str = Field(None)
    password: str = Field(None)

    class Config:
        from_attributes = True
        orm_mode = True
        arbitrary_types_allowed = True


class Product(Base):
    __tablename__ = "products"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    is_available: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


class ProductDTO(BaseModel):
    name: str = Field(None)
    description: str = Field(None)
    price: float = Field(None)
    stock: int = Field(None)
    is_available: bool = Field(None)

    class Config:
        from_attributes = True
        orm_mode = True
        arbitrary_types_allowed = True


class ProductResponse(BaseModel):
    id: uuid.UUID
    name: str
    description: Optional[str] = None
    price: float
    stock: int
    is_available: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True
        arbitrary_types_allowed = True


class ProductUpdateDTO(BaseModel):
    name: str = Field(None)
    description: str = Field(None)
    price: float = Field(None)
    stock: int = Field(None)
    is_available: bool = Field(None)

    class Config:
        from_attributes = True
        orm_mode = True
        arbitrary_types_allowed = True


class ProductSearchParams(BaseModel):
    name: Optional[str] = Field(
        default=None, description="Partial or full product name"
    )
    min_price: Optional[Decimal] = Field(default=None, description="Minimum price")
    max_price: Optional[Decimal] = Field(default=None, description="Maximum price")
    isAvailable: Optional[bool] = Field(
        default=None, description="Filter by availability"
    )
    page: int = Field(default=1, ge=1, description="Page number for pagination")
    page_size: int = Field(
        default=20, ge=1, le=100, description="Number of products per page"
    )
    sort_by: str = Field(default="name", description="Sort by field")
    sort_order: str = Field(default="asc", description="Sort order: asc or desc")
