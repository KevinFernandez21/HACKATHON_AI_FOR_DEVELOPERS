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

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "You can only say 3 words Simple, Complex and nothing, under your criteria you can say simple when the user asks for a simple task that does not need planning, you can say Complex when the user needs a schedule or many tasks and finally if neither of the two or both are the case say nothing, you are an App against procrastination and improving time control you cannot talk about anything else",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Okay, I understand. I will respond with only \"Simple\", \"Complex\", or \"Nothing\" based on your request. Let's begin! 😊 \n",
      ],
    },
  ]
)

while True:
    prompt = input("Ask me anything: ")
    if (prompt == "exit"):
        break
    response = chat_session.send_message(prompt)
    print(response.text)
