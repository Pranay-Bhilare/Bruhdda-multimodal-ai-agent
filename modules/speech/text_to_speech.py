from elevenlabs import ElevenLabs, Voice, VoiceSettings
from typing import Optional
import os
from dotenv import load_dotenv
load_dotenv()
class TextToSpeech() : 
    """A class to handle text-to-speech conversion using ElevenLabs"""
    # REQUIRED_ENV_VARS = "ELEVENLABS_API_KEY", "ELEVENLABS_VOICE_ID"
    def __init__(self) -> None:
        self._client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
        self.TTS_MODEL_NAME = "eleven_flash_v2_5"
    
    # def client(self) -> ElevenLabs : 
    #     if self._client is None:
    #         self._client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))
    #     return self._client
    
    def synthesize(self,text: str) -> bytes: 
        if not text.strip() : 
            raise ValueError("Empty text not allowed")
        
        if len(text) > 5000:
            raise ValueError("Input text exceeds maximum length of 5000 characters")
        
        try:
            audio_generator = self._client.text_to_speech.convert(
                text=text,
                voice_id=os.getenv("ELEVENLABS_VOICE_ID"),
                model_id= self.TTS_MODEL_NAME,
            )

            # Convert generator to bytes
            audio_bytes = b"".join(audio_generator)
            if not audio_bytes:
                raise ValueError("Generated audio is empty")

            return audio_bytes
        
        except Exception as e:
            raise ValueError(f"Text-to-speech conversion failed: {str(e)}") from e