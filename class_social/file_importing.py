from fastapi import APIRouter, File, UploadFile
from typing import List
from deta import Deta
import os

upload_router = APIRouter()

token = os.environ.get("DETA_PROJECT_KEY")
deta = Deta(token)
files__ = deta.Drive("myfiles")

@upload_router.post('/teacher/upload', tags=["files"])
async def upload(files: List[UploadFile] = File(...)):
    for file in files:
        files__.put(file.filename, file.file)
    return {"files": [file.filename for file in files]}
