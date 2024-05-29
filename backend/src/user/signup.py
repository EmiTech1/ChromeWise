from fastapi import HTTPException, status
from passlib.context import CryptContext
from mongoengine.errors import NotUniqueError
from src.common.chain.config import Connection
from src.user.models import User

# Initialize the database connection
connection = Connection()
collection = connection.collection

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


async def sign_up(username: str, email: str, password: str, confirm_password: str, api_key: str):
    if password != confirm_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password and confirm password do not match"
        )

    if api_key == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="enter valid api_key "
        )

    if api_key == "" or username == "" or password == "" or email == "":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="no any field should will empty"
        )

    hashed_password = get_password_hash(password)

    user_data = {
        "username": username,
        "email": email,
        "hashed_password": hashed_password,
        "api_key": api_key,
    }
    user = User(**user_data)

    try:
        user.save()
    except NotUniqueError as e:
        if "username" in str(e):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already exists"
            )
        elif "email" in str(e):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A user with these details already exists"
            )

    return {"message": "User registered successfully"}
