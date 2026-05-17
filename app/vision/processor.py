import os
from PIL import Image

from app.utils.gemini_client import GeminiClient
from app.vision.prompts import VISION_ANALYSIS_PROMPT

client = GeminiClient()


class VisionProcessor:

    @staticmethod
    def load_image(path):

        if not os.path.exists(path):
            raise ValueError(f"Image not found: {path}")

        return Image.open(path).convert("RGB")

    @staticmethod
    def analyze_image(
        image_path,
        question
    ):

        image = VisionProcessor.load_image(
            image_path
        )

        prompt = f"""
{VISION_ANALYSIS_PROMPT}

User question:
{question}
"""

        result = client.generate_vision(
            prompt,
            image
        )

        return result
