from pydantic import BaseModel
from fastapi import UploadFile, File

class RequestModel(BaseModel):
    resume: UploadFile = File(None)