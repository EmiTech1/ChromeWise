from fastapi import APIRouter, HTTPException
from src.user.models import UserSignUpRequest
from src.user import signup
from fastapi import FastAPI, HTTPException, Depends, status, APIRouter
from src.user.login import login_for_access_token
from fastapi.security import OAuth2PasswordRequestForm


signup_router = APIRouter()


@signup_router.post("/signup")
async def sign_up_route(request: UserSignUpRequest):
    try:
        response = await signup.sign_up(
            username=request.username,
            email=request.email,
            api_key=request.api_key,
            password=request.password,
            confirm_password=request.confirm_password
        )
        return response
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

login_router = APIRouter()


@login_router.post("/Login or Sig_in")
async def login_route(form_data: OAuth2PasswordRequestForm = Depends()):
    return await login_for_access_token(form_data)


