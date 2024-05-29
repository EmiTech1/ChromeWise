from mongoengine import Document, StringField
from pydantic import BaseModel, Field, field_validator, EmailStr


# for signup
# MongoDB User Document for signup
class User(Document):
    username = StringField(required=True)
    email = StringField(required=True, unique=True)
    hashed_password = StringField(required=True)
    api_key = StringField(required=True, unique=True)
    access_token=StringField()


class UserSignUpRequest(BaseModel):
    username: str
    email: EmailStr
    api_key: str
    password: str = Field(..., min_length=8, max_length=12)
    confirm_password: str

    @field_validator('username')
    def no_numeric_in_username(cls, v):
        if any(char.isdigit() for char in v):
            raise ValueError('username should be string only')
        return v

    @field_validator('password')
    def valid_password(cls, v):
        if len(v) < 8 or len(v) > 12:
            raise ValueError(
                'Password must be between 8 and 12 characters long')
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one digit')
        if not any(char.isupper() for char in v):
            raise ValueError(
                'Password must contain at least one uppercase letter')
        if not any(char.islower() for char in v):
            raise ValueError(
                'Password must contain at least one lowercase letter')
        return v

# for login

# class Users(Document):
#     username = StringField(required=True, unique=True)
#     hashed_password = StringField(required=True)
#     token = StringField(required=True)

# class UserInDB(BaseModel):
#     username: str
#     hashed_password: str
#     token: str

# class UserLogin(BaseModel):
#     username: str
#     password: str