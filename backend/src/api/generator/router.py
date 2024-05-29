import os
from fastapi import APIRouter
from src.api.generator.models import ChatRequest
from src.api.generator import service

generator_router = APIRouter()


@generator_router.post("/linkedin/{user_id}")
async def linkedin_api(request: ChatRequest):
    return await service.linkedin_api(request)


@generator_router.post("/facebook/{user_id}")
async def facebook_api(request: ChatRequest):
    return await service.facebook_api(request)


@generator_router.post("/instagram/{user_id}")
async def instagram_api(request: ChatRequest):
    return await service.instagram_api(request)


@generator_router.post("/twitter/{user_id}")
async def twitter_api(request: ChatRequest):
    return await service.twitter_api(request)


@generator_router.post("/youtube_script_creator/{user_id}")
async def youtube_script_creator_api(request: ChatRequest):
    return await service.youtube_script_creator_api(request)

# from pydantic import BaseModel
# from enum import Enum
# class API_ENUMS(str, Enum):
#     class CONTENT_TYPE:
#         FACEBOOK: "FACEBOOK"
#         YOUTUBE: "YOUTUBE"
    
# class GenerateDto(BaseModel):
#     type: API_ENUMS.CONTENT_TYPE
    
# class GenerateRequest(BaseModel):
#     token: str
#     generateDto: GenerateDto

# def generate_content(request: GenerateRequest):
#     payload = request["generateDto"]