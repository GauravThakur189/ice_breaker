import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print(f"API Key: {api_key}")  # This will print the API key to verify it's loaded correctly