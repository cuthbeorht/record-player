from pydantic import BaseModel
from typing import List

class Recording(BaseModel):
    path: str


class Service:
    """
    This is the recording service.
    """

    def __init__(self, database=None):
        """
        Creates an instance of the Recording Service class with a connection to the
        database.

        :param database:
        """
        self.db = database

    async def get_recordings(self) -> List[Recording]:
        """
        Get all recordings.

        :return: List[Recording]
        """

        recordings = [Recording(**{"path": "recordings/2021-12-27_19-35-02.mp3"})]
        print(f"Recordings: {recordings}")

        return recordings
