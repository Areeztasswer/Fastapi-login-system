
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from models import Product, User

from services import product_services
from services import user_services

from security_utilities import create_access_token
from users import admin_only, admin_or_employee


router = APIRouter()


def get_product_service():
    return product_services


def get_user_service():
    return user_services







@router.get(
    "/products",
    response_model=list[Product],
    status_code=status.HTTP_200_OK
)
def get_products(
    service=Depends(get_product_service),
    current_user=Depends(admin_or_employee)
):

    return service.get_products()


@router.get(
    "/product/{id}",
    status_code=status.HTTP_200_OK
)
def get_product(
    id: int,
    service=Depends(get_product_service),
    current_user=Depends(admin_or_employee)
):

    product = service.get_product(id)

    if product:
        return product

    return {
        "message": "Product not found"
    }


@router.post(
    "/product",
    response_model=Product,
    status_code=status.HTTP_201_CREATED
)
def create_product(
    product: Product,
    service=Depends(get_product_service),
    current_user=Depends(admin_only)
):

    return service.create_product(product)


@router.put(
    "/product",
    status_code=status.HTTP_200_OK
)
def update_product(
    id: int,
    product: Product,
    service=Depends(get_product_service),
    current_user=Depends(admin_only)
):

    updated = service.update_product(
        id,
        product
    )

    if updated:
        return updated

    return {
        "message": "Product not found"
    }


@router.delete(
    "/product/{id}",
    status_code=status.HTTP_200_OK
)
def delete_product(
    id: int,
    service=Depends(get_product_service),
    current_user=Depends(admin_only)
):

    deleted = service.delete_product(id)

    if deleted:

        return {
            "message": "Product deleted successfully",
            "deleted_product": deleted.model_dump()
        }

    return {
        "message": "Product not found"
    }





@router.post("/user")
def create_user(
    user: User,
    service=Depends(get_user_service)
):

    return service.create_user(user)




@router.post("/login")
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service=Depends(get_user_service)
):

    user = service.login_user(
        form_data.username,
        form_data.password
)

    if not user:

        return {
            "message": "Invalid Username or Password"
        }

    access_token = create_access_token(
        data={
            "sub": user.username,
            "role": user.role.value
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
