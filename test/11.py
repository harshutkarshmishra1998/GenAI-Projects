import requests

url = "http://127.0.0.1:8000/summarize/invoke"

payload = {
    "input": {
        "text": "LangChain helps developers build LLM-powered applications easily and efficiently."
    }
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print("✅ Summary:", data.get("output"))
else:
    print("❌ Error:", response.status_code, response.text)