from pydantic import BaseModel


class VisionRequest(BaseModel):

    image_path: str
    question: str


class VisionResponse(BaseModel):

    status: str
    answer: str
