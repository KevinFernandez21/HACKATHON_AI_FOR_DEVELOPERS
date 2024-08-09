import os
from dotenv import load_dotenv
load_dotenv()  # Load the .env file
import google.generativeai as genai


GOOGLE_API_KEY=os.getenv('API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel( model_name="gemini-1.5-flash",
    generation_config=generation_config, )

chat = model.start_chat(history=[])

while True:
    prompt = input("Ask me anything: ")
    if (prompt == "exit"):
        break
    response = chat.send_message(prompt)
    print(response)
