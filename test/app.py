from fastapi import FastAPI
from langserve import add_routes
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
import os
import api_keys

os.environ["OPENAI_API_KEY"] = api_keys.open_ai_key

# Step 1️⃣ — Initialize FastAPI app
app = FastAPI(
    title="LangServe Summarizer API",
    version="1.0",
    description="Summarizes text in one sentence using GPT-4o-mini.",
)

# Step 2️⃣ — Define LLM and prompt
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
prompt = PromptTemplate.from_template("Summarize this in one sentence: {text}")

# Step 3️⃣ — Combine using RunnableSequence
chain = prompt | llm  # ✅ replaces old LLMChain()

# Step 4️⃣ — Add LangServe route
add_routes(app, chain, path="/summarize")

# To run:
# uvicorn app:app --host 0.0.0.0 --port 8000