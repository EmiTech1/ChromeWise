import os
from fastapi import APIRouter, UploadFile, File

from langchain_community.document_loaders import PyPDFLoader

from .utils import processor, scanner
from .models import RequestModel

router = APIRouter()

@router.post('/resume/scanner')
async def scanner_route(file: UploadFile):
        document = processor(file)    
        resume = scanner(document)

        return resume

# @router.post('/router/checker')
# async def checker_route(file: UploadFile):
        