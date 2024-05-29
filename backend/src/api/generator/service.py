from fastapi import HTTPException
from src.api.generator.models import ChatRequest
from src.common.chain.prompt import linkedin_prompt, instagram_prompt, facebook_prompt, twitter_prompt, youtube_prompt
from src.common.chain.llm import generate_response, fetch_data
from src.user.models import User
from langchain_community.chat_models import ChatOpenAI


# for LinkedIn

async def linkedin_api(request: ChatRequest):
    try:
        prompt = linkedin_prompt
        response1 = await generate_response(request, prompt)
        response2 = await fetch_data(request)

        combined_response = {
            "response1": response1
        }
        return combined_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# for Instagram


async def instagram_api(request: ChatRequest):
    try:
        prompt = instagram_prompt
        response1 = await generate_response(request, prompt)
        response2 = await fetch_data(request)

        combined_response = {
            "response1": response1,
            "response2": response2
        }
        return response1

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# for Facebook


async def facebook_api(request: ChatRequest):
    try:
        prompt = facebook_prompt
        response1 = await generate_response(request, prompt)
        response2 = await fetch_data(request)

        combined_response = {
            "response1": response1,
            "response2": response2
        }
        return response1
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# for Twitter


async def twitter_api(request: ChatRequest):
    try:
        prompt = twitter_prompt
        response1 = await generate_response(request, prompt)
        response2 = await fetch_data(request)

        combined_response = {
            "response1": response1,
            "response2": response2
        }
        return response1
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# for YouTube script creator


async def youtube_script_creator_api(request: ChatRequest):
    try:
        prompt = youtube_prompt
        response1 = await generate_response(request, prompt)
        response2 = await fetch_data(request)

        combined_response = {
            "response1": response1,
            "response2": response2
        }
        return response1
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
