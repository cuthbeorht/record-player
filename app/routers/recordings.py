from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
import os
from app.services.recordings import Service as RecordingService, Recording
from typing import List
from pydantic import BaseModel

router = APIRouter()


class GetRecordingsResponse(BaseModel):
    recordings: List[Recording]


@router.get("/play")
async def play():
    def recording_audio_streamer():
        print(f"CWD: {os.getcwd()}")
        with open("recordings/2021-12-27_19-35-02.mp3", "rb") as audio_stream:
            yield from audio_stream

    return StreamingResponse(recording_audio_streamer(), media_type="audio/mp3")


@router.get("/")
async def get_recordings(recording_service: RecordingService = Depends(RecordingService)) -> GetRecordingsResponse:
    recordings = await recording_service.get_recordings()


    return GetRecordingsResponse(**{"recordings": recordings})
