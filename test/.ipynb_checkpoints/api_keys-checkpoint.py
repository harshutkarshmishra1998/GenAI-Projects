from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access your variables
lang_chain_key = os.getenv("LANG_CHAIN")
open_ai_key = os.getenv("OPEN_AI")
hugging_face = os.getenv("HUGGING_FACE")
groq_api = os.getenv("GROQ_API")

# print("I'm good")
# print(open_ai_key)