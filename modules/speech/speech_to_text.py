from groq import Groq
import os
import tempfile
class SpeechToText(): 
    def __init__(self) -> None:
        self._client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    async def transcribe(self, audio_data : bytes)->str :    
        """Converts audio(speech) into text using Groq's Whisper model"""

        if not audio_data:
            raise ValueError("Audio data cannot be empty")
        
        try : 
            with tempfile.NamedTemporaryFile(suffix=".mp3", delete= False) as temp_file :
                temp_file.write(audio_data)
                temp_file_path = temp_file.name
            try : 
                with open(temp_file_path, "rb") as audio_file:  
                    transcription = self._client.audio.transcriptions.create(
                        file=audio_file,
                        model="whisper-large-v3-turbo",
                        language="en",
                        response_format="text"
                    )
                if not transcription:
                    raise ValueError("Transcription result is empty")
                return transcription
            finally :
                os.unlink(temp_file_path)
        except Exception as e :
            raise ValueError(f"Speech-to-text conversion failed: {str(e)}") from e