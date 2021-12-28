from fastapi import APIRouter
from fastapi.responses import StreamingResponse
import os

router = APIRouter()

@router.get("/play")
async def play():
    def recording_audio_streamer():
        print(f"CWD: {os.getcwd()}")
        with open("recordings/2021-12-27_19-35-02.mp3", "rb") as audio_stream:
            yield from audio_stream

    return StreamingResponse(recording_audio_streamer(), media_type="audio/mp3")