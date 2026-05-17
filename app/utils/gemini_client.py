import time
import google.generativeai as genai

from app.config import (
    GEMINI_API_KEY,
    MODEL_NAME,
    MAX_RETRIES
)

from app.utils.logger import get_logger

logger = get_logger(__name__)


class GeminiClient:

    def __init__(self):

        if not GEMINI_API_KEY:
            raise ValueError("Missing API key")

        genai.configure(
            api_key=GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            MODEL_NAME
        )

    def generate_vision(
        self,
        prompt,
        image
    ):

        for attempt in range(MAX_RETRIES):

            try:

                response = self.model.generate_content(
                    [prompt, image]
                )

                if response.text:
                    return response.text.strip()

            except Exception as e:

                logger.error(
                    f"Attempt {attempt+1} failed: {e}"
                )

                time.sleep(1)

        return "error: failed to generate response"
