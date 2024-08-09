#info de: https://aistudio.google.com/app/prompts/new_chat
## implementar fast API para crear un chat simple

import os
from dotenv import load_dotenv
load_dotenv()  # Load the .env file

import google.generativeai as genai

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import status

from geminiSchema import GeminiSchema

app = FastAPI()

@app.get("/")  #ruta raiz
async def root():
    return {"message": "ESTO ES UNA PRUEBA AAA busca /chatbot"}


@app.post("/chatbot", status_code=status.HTTP_200_OK, tags=["gemini"] )  #ruta chatbot
def chatbotGemini(pregunta: GeminiSchema):
  genai.configure(api_key=os.getenv('API_KEY'))

  model = genai.GenerativeModel( model_name="gemini-1.5-flash" )

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
  response = chat_session.send_message(pregunta.preguntas)

  return JSONResponse(status_code=status.HTTP_200_OK, content={"respuesta": response.text})
