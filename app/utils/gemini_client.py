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

            logger.warning(
                "Missing GEMINI_API_KEY"
            )

            self.model = None
            return

        try:

            genai.configure(
                api_key=GEMINI_API_KEY
            )

            self.model = genai.GenerativeModel(
                MODEL_NAME
            )

        except Exception as e:

            logger.error(
                f"Gemini init failed: {e}"
            )

            self.model = None

    def generate_vision(
        self,
        prompt,
        image
    ):

        if self.model is None:
            return "error: model not initialized"

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
