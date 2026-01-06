from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(__file__).parent / ".env")

def require_env(key):
    value = os.getenv(key)
    if not value:
        raise RuntimeError(f"Missing environment variable: {key}")
    return value

openai_api = require_env("OPENAI_API")
langchain_api = require_env("LANGCHAIN_API")
huggingface_api = require_env("HUGGING_FACE_API")
groq_api = require_env("GROQ_API")
astra_db_api_endpoint = require_env("ASTRA_DB_API_ENDPOINT")
astra_db_application_token = require_env("ASTRA_DB_APPLICATION_TOKEN")
astra_db_keyspace = require_env("ASTRA_DB_KEYSPACE")
wb_api = require_env("WB_API")
serpai_api = require_env("SERPAI_API")

print("OPENAI loaded:", bool(openai_api))
