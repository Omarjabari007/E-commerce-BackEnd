from pydantic import BaseModel, Field, condecimal, constr
from uuid import UUID
from datetime import datetime


class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: float
    stock: int
    is_available: bool = Field(..., alias="isAvailable")

    class Config:
        allow_population_by_field_name = True
        orm_mode = True


class ProductResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    price: float
    stock: int
    is_available: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        orm_mode = True


class ProductUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    price: float | None = None
    stock: int | None = None
    is_available: bool | None = None

    class Config:
        from_attributes = True
        orm_mode = True
