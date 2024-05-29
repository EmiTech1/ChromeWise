from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.api.resume.router import router as resume_router
from src.api.generator.router import generator_router
from src.user.router import signup_router
from src.user.router import login_router
import jwt
from fastapi.middleware.cors import CORSMiddleware
from src.common.chain.config import Connection

app = FastAPI()
connection = Connection()
collection = connection.collection

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

SECRET_KEY = '2d0d51b47c2e3ecc9e8526d2ec011f0caafe1e6903c7a5210aea057cb03c5011'
security = HTTPBearer()

async def verify_jwt_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Include routers
app.include_router(signup_router,dependencies=[Depends(verify_jwt_token)])
app.include_router(login_router)
app.include_router(resume_router,dependencies=[Depends(verify_jwt_token)])
app.include_router(generator_router,dependencies=[Depends(verify_jwt_token)])











# from fastapi import FastAPI, HTTPException, Depends, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from passlib.context import CryptContext
# from pymongo import MongoClient
# from datetime import datetime, timedelta
# from typing import Optional
# import jwt
# from fastapi.middleware.cors import CORSMiddleware
# from src.api.resume.router import router as resume_router
# from src.api.generator.router import generator_router
# from src.user.router import signup_router
# from src.user.router import login_router

# # MongoDB connection settings
# MONGO_URI = "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.2.4"
# DATABASE_NAME = "monica"
# COLLECTION_NAME = "user"

# # Security and JWT settings
# SECRET_KEY = "2d0d51b47c2e3ecc9e8526d2ec011f0caafe1e6903c7a5210aea057cb03c5011"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 15

# # FastAPI instance
# app = FastAPI()

# # OAuth2 password bearer
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# # Password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# # MongoDB connection
# client = MongoClient(MONGO_URI)
# db = client[DATABASE_NAME]
# collection = db[COLLECTION_NAME]

# # Dependency to verify password
# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)

# # Dependency to get password hash
# def get_password_hash(password: str) -> str:
#     return pwd_context.hash(password)

# # Dependency to authenticate user
# def authenticate_user(username: str, password: str):
#     user = collection.find_one({"username": username})
#     if not user or not verify_password(password, user["hashed_password"]):
#         return None
#     return user

# # Dependency to create access token
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt

# # Dependency to get current user
# async def get_current_user(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise HTTPException(status_code=401, detail="Invalid token")
#     except jwt.ExpiredSignatureError:
#         raise HTTPException(status_code=401, detail="Token has expired")
#     except jwt.InvalidTokenError:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return username

# # Route to generate access token
# @app.post("/token")
# async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
#     user = authenticate_user(form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user["username"]}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}


# # Include routers
# app.include_router(signup_router)
# app.include_router(login_router)
# # resume_router.include_router(resume_router, dependencies=[Depends(get_current_user)])
# generator_router.include_router(generator_router, dependencies=[Depends(get_current_user)])




