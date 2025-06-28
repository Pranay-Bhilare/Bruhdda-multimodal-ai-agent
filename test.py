from modules.speech.text_to_speech import TextToSpeech
text_to_speech = TextToSpeech()
audio_bytes = text_to_speech.synthesize("Hi How are you Pranay Bruhhda")

with open("out.mp3", "wb") as file:
    file.write(audio_bytes)