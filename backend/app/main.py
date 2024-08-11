
from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import time
import google.generativeai as genai

# Load the .env file
load_dotenv()

# Configure the API key for genai
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError("API_KEY not found in environment variables")
genai.configure(api_key=api_key)

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las orígenes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar el directorio estático
app.mount("/static", StaticFiles(directory="static"), name="static")
#no tocar esto
# Manejar solicitudes para favicon.ico----
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    # Retornar el archivo favicon.ico si existe, de lo contrario, retornar un estado 204
    favicon_path = "static/favicon.ico"
    if os.path.exists(favicon_path):
        return FileResponse(favicon_path)
    return Response(status_code=204)
#------------------------------------------------
class RequestBody(BaseModel):
    prompt: str

@app.post("/generate")
def generate_content(request: RequestBody):
    try:
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction="You can only say 3 words Simple Complex and nothing, under your criteria you can say simple when the user asks for a simple task that does not need planning, you can say Complex when the user needs a schedule or many tasks and finally if neither of the two or both are the case say nothing, you are an App against procrastination and improving time control you cannot talk about anything else"
        )
        start_time = time.time()
        response = model.generate_content(request.prompt)
        end_time = time.time()
        elapsed_time = end_time - start_time
        return {"response": response.text, "elapsed_time": elapsed_time}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)