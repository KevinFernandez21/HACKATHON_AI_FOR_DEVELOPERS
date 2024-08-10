#info de: https://aistudio.google.com/app/prompts/new_chat
## implementar fast API para crear un chat simple

import os
from dotenv import load_dotenv
load_dotenv()  # Load the .env file

import google.generativeai as genai

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi import status
import httpx

from geminiSchema import GeminiSchema

app = FastAPI()

genai.configure(api_key=os.getenv('API_KEY'))
model = genai.GenerativeModel( model_name="gemini-1.5-flash" )

@app.get("/")  #ruta raiz
async def root():
    return {"message": "ESTO ES UNA PRUEBA AAA busca /chatbot"}


@app.post("/chatbot", status_code=status.HTTP_200_OK, tags=["gemini"])
async def chatbotGemini(preguntas: GeminiSchema):
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "You are an App against procrastination and improving time control. You cannot talk about anything else. I want you to give me a quick greeting, and set 3 different options that the user can ask. Here are some options: \"You are an App against procrastination and improving time control. You cannot talk about anything else\", \"Start a new activity or task\", \"Start a simple task.\" If they don't choose one of these options, continue the conversation with the user.",
                ],
            },
        ]
    )

    if preguntas.pregunta == "I want to take a shower":
        async with httpx.AsyncClient() as client:
            constructor_response = await client.post("http://localhost:8000/constructor", json=preguntas.dict())
            
            if constructor_response.status_code == 200:
                constructor_data = constructor_response.json()
                return JSONResponse(status_code=status.HTTP_200_OK, content=constructor_data)
            else:
                return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"error": "Error communicating with constructor endpoint"})
    
    else:
        response = chat_session.send_message(preguntas.pregunta)
        return JSONResponse(status_code=status.HTTP_200_OK, content={"respuesta": response.text})

@app.post("/constructor", status_code=status.HTTP_200_OK, tags=["constructor"] )  #ruta constructor
async def constructor(preguntas: GeminiSchema):

  chat_session = model.start_chat(
    history=[
      {
        "role": "user",
        "parts": [
          "You are an app specifically designed to combat procrastination and improve time management. You cannot discuss anything else.\n\nThe user will provide you with an activity or event they want to complete. You must respond with a tuple that includes the following elements:\n\nActivity/event name: A short title that you decide based on the activity/event.\nActivity/event description: The activity or event as described by the user.\nEstimated time: The time it will take to complete the activity/event. If the user’s message doesn’t include the time, ask if they have a time in mind. If the user says \"no\" or \"I don’t know,\" provide an estimated time for the activity/event.\nActivity classification: Determine if the activity is \"Simple\" or \"Complex\" based on the following criteria: Use \"Simple\" if the task requires no planning and can be completed easily. Use \"Complex\" if the activity requires scheduling or multiple tasks to complete. If the activity doesn’t clearly fit into either \"Simple\" or \"Complex,\" or if both could apply, return \"nothing.\"",
        ],
      },
      {
        "role": "model",
        "parts": [
          "Okay, tell me about the activity or event you want to complete. I'll break it down for you!  I'll need the details to help you conquer procrastination and manage your time effectively. \n",
        ],
      },
    ]
  )

  response = chat_session.send_message(preguntas.pregunta)
  return JSONResponse(status_code=status.HTTP_200_OK, content={"respuesta": response.text})  


@app.get("/proximamente")  #ruta proximamente
async def proximamente():
    return {"message": "proximamente solo en cines"}