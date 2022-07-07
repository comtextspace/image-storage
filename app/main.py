from typing import Union

from fastapi import FastAPI
from fastapi.responses import FileResponse, PlainTextResponse

app = FastAPI()


@app.get("/")
def read_root():
    return PlainTextResponse("Service is working!")


@app.get("/image/{image_name}")
def get_image(image_name: str):
    return FileResponse(f"./images/{image_name}")
