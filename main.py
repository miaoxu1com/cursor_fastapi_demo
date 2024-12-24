from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import os
from datetime import datetime
import shutil

app = FastAPI()
# 添加CORS中间件配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173"],  # 允许的前端源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有header
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


def ensure_upload_dir():
    upload_dir = "upload"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    return upload_dir


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        upload_dir = ensure_upload_dir()
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_extension = os.path.splitext(file.filename)[1]
        new_filename = f"{timestamp}{file_extension}"
        
        file_path = os.path.join(upload_dir, new_filename)
        
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return {
            "code": 200,
            "message": "文件上传成功",
            "filename": new_filename,
            "file_path": file_path
        }
    except Exception as e:
        return {
            "code": 500,
            "message": f"文件上传失败: {str(e)}"
        }
