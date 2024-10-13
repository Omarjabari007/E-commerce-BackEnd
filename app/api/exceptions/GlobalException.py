from fastapi import HTTPException, status


class EmailAlreadyExistsException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email is already registered",
        )


class InvalidPasswordException(HTTPException):
    def __init__(self, errors: list):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"password_errors": errors},
        )


class PriceValidationException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Price must be a positive number.",
        )


class StockValidationException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Stock must be greater than zero.",
        )

class ProductDoesNotExistException(HTTPException):
    def __init__(self, item_number: int = None):
        if item_number is not None:
            detail_message = f"Product {item_number} does not exist, enter a valid product_id"
        else:
            detail_message = "Product_id does not exist, enter a valid id"
            
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail_message,
        )

class OutOfStockException(HTTPException):
    def __init__(self, item_number: int = None):
        if item_number is not None:
            detail_message = f"Quantity for product {item_number} is higher than the stock."
        else:
            detail_message = "Quantity for the product is higher than the stock."
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail_message,
        )

class OrderNotFoundException(HTTPException):
    def __init__(self, item_number: int = None):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Order not found",
        )

