import os
from fastapi import APIRouter
from src.api.generator.models import ChatRequest
from src.api.generator.service import generate_content

generator_router = APIRouter()


@generator_router.post("/generateContent")
async def generate_contents(request: ChatRequest):
    return await generate_content(request)






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