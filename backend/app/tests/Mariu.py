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

  chat = model.start_chat(history=[])

  response = chat.send_message(pregunta.preguntas)

  return JSONResponse(status_code=status.HTTP_200_OK, content={"respuesta": response.text})
