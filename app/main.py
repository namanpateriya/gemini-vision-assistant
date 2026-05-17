from fastapi import FastAPI

from app.schemas import (
    VisionRequest,
    VisionResponse
)

from app.service import VisionService

app = FastAPI(
    title="Gemini Vision Assistant"
)


@app.get("/")
def health():

    return {
        "status": "running",
        "service": "vision-assistant"
    }


@app.post(
    "/analyze",
    response_model=VisionResponse
)
def analyze(request: VisionRequest):

    return VisionService.process(
        request.image_path,
        request.question
    )
