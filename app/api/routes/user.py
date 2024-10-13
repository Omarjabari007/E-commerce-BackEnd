from fastapi import APIRouter, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.user import UserCreateRequest, UserResponse, UserUpdateRequest
from app.api.services.user_service import UserService
from app.api.exceptions.global_exceptions import (
    InvalidPasswordException,
    EmailAlreadyExistsException,
    UserNotFoundException,
    InvalidUUIDException,
)
from uuid import UUID

router = APIRouter()


@router.post("/users", response_model=UserResponse)
def create_user(user: UserCreateRequest, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.create_user(user)


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: str, db: Session = Depends(get_db)):
    try:
        user_uuid = UUID(user_id)
    except ValueError:
        raise InvalidUUIDException()

    service = UserService(db)
    try:
        return service.get_user(user_uuid)
    except UserNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )


@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: str, user_data: UserUpdateRequest, db: Session = Depends(get_db)
):
    try:
        user_uuid = UUID(user_id)
    except ValueError:
        raise InvalidUUIDException()

    service = UserService(db)
    return service.update_user(user_uuid, user_data)


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str, db: Session = Depends(get_db)):
    try:
        user_uuid = UUID(user_id)
    except ValueError:
        raise InvalidUUIDException()

    service = UserService(db)
    try:
        service.delete_user(user_uuid)
    except UserNotFoundException:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found."
        )


@router.get("/users", response_model=list[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()
