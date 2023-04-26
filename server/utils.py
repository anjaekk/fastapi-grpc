import hvac
import base64
from os import getenv
from dotenv import load_dotenv

env = load_dotenv()

ALLOWED_ORIGINS = getenv("CORS_ALLOWED_ORIGINS")

DATABASE_URL = getenv("DATABASE_URL")