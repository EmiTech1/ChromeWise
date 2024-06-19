import openai
import re
from src.api.generator.models import ChatRequest
from langchain_openai import OpenAI
from langchain import OpenAI
from src.common.chain.config import Connection
from langchain_community.chat_models import ChatOpenAI
from bson import ObjectId
from fastapi import HTTPException

connection = Connection()
collection = connection.collection


def split_into_sentences(text):
    sentence_endings = re.compile(r'(?<=[.!?]) +')
    sentences = sentence_endings.split(text)
    return sentences


openai_api_key = None
async def fetch_data(request: ChatRequest):
    user_id = ObjectId(request.user_id)
    document = collection.find_one({"_id": user_id})
    try:
        user_id = ObjectId(request.user_id)
    except:
        return "Invalid user ID"
    if document:
        openai_api_key = document.get("api_key")
        if openai_api_key:
            openai.api_key = openai_api_key
        else:
            raise HTTPException(
                status_code=404, detail="API key not found for the user")
    else:
        raise HTTPException(status_code=404, detail="User not found")

llm = OpenAI(api_key=openai_api_key, model_name="gpt-3.5-turbo")


# Define a function to generate response using LangChain
async def generate_response(request: ChatRequest, prompt):
    response = llm(prompt.template.format(topic=request.message))
    content = response.strip()
    sentences = split_into_sentences(content)
    formatted_content = "\n\n".join(
        [sentence.strip() for sentence in sentences])
    formatted_content = formatted_content.replace("\\", "")
    return {"response": formatted_content}
