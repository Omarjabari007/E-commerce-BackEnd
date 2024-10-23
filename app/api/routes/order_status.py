from uuid import UUID
from app.api.exceptions.global_exceptions import InternalServerErrorException, StatusAlreadyExistsException, StatusInUseException, StatusNameInvalidException, StatusNotFoundException
from app.api.services.order_status_service import OrderStatusService
from fastapi import APIRouter, HTTPException, status

router = APIRouter()
order_status_service = OrderStatusService

@router.post("/statuses/", status_code=status.HTTP_201_CREATED)
def create_order_status(name: str):

    try:
        new_status = order_status_service.create_order_status(name=name)
    except Exception:
        raise InternalServerErrorException()

    return new_status

@router.get("/statuses/{status_id}", status_code=status.HTTP_200_OK)
def get_order_status_by_id(status_id: UUID):

    try:
        order_status = order_status_service.get_order_status_by_id(status_id=status_id)
    except Exception:
        raise InternalServerErrorException()

    return order_status


@router.put("/statuses/{status_id}", status_code=status.HTTP_200_OK)
def update_order_status(status_id: UUID, name: str):

    try:
        updated_status = order_status_service.update_order_status(status_id=status_id, name=name)
    except Exception:
        raise InternalServerErrorException()

    return updated_status

@router.delete("/statuses/{status_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_order_status(status_id: UUID):
    
    try:
        order_status_service.remove_order_status(status_id=status_id)
    except Exception:
        raise InternalServerErrorException()