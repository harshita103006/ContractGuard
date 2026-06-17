import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    gemini-2.0-flash"
)

def ask_gemini(prompt):
    try:
        print("Sending request...")

        response = model.generate_content(prompt)

        print("Response received...")

        return response.text

    except Exception as e:
        print("ERROR:", e)
        return str(e)
    
print(model)