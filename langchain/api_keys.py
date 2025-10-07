from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access your variables
lang_chain_key = os.getenv("LANG_CHAIN")
open_ai_key = os.getenv("OPEN_AI")
lang_chain_project = os.getenv("LANG_CHAIN_PROJECT")

# print(lang_chain_key)
# print(open_ai_key)