from fastapi import FastAPI
from api.resume.router import router as resume_router

app = FastAPI()

app.include_router(resume_router)