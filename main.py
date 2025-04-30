from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
import openai
import uuid
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/generate-audio")
async def generate_audio(text: str = Form(...), voice: str = Form("alloy")):
    speech_file_path = f"/tmp/{uuid.uuid4()}.mp3"

    response = openai.audio.speech.create(
        model="tts-1",
        voice=voice,
        input=text
    )
    response.stream_to_file(speech_file_path)
    return FileResponse(speech_file_path, media_type="audio/mpeg", filename="speech.mp3")
