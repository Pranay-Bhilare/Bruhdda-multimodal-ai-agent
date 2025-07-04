# from modules.speech.text_to_speech import TextToSpeech
# text_to_speech = TextToSpeech()
# audio_bytes = text_to_speech.synthesize("Hi How are you Pranay Bruhhda")

# with open("out.mp3", "wb") as file:
#     file.write(audio_bytes)


from modules.speech.speech_to_text import SpeechToText
import asyncio
speechToText = SpeechToText()

with open("out.mp3", "rb") as f:
    audio_bytes = f.read()

async def main() :
    result = await speechToText.transcribe(audio_bytes)
    print(result)

asyncio.run(main())
