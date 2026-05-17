import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gemini-1.5-flash"
)

MAX_INPUT_LENGTH = int(
    os.getenv("MAX_INPUT_LENGTH", 2000)
)

MAX_RETRIES = int(
    os.getenv("MAX_RETRIES", 3)
)
