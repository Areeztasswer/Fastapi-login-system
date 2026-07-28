
from models import User
from config import user_collection

from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str):
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def create_user(user: User):

    hashed_password = hash_password(user.password)

    user_data = {
        "username": user.username,
        "password": hashed_password,
        "role": user.role.value
    }

    user_collection.insert_one(user_data)

    return {
        "username": user.username,
        "role": user.role
    }


def login_user(username: str, password: str):

    user = user_collection.find_one(
        {"username": username}
    )

    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    return User(
        username=user["username"],
        password=user["password"],
        role=user["role"]
    )