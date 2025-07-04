# --------- SPEECH TO TEXT TESTING --------------------------

# from modules.speech.text_to_speech import TextToSpeech
# text_to_speech = TextToSpeech()
# audio_bytes = text_to_speech.synthesize("Hi How are you Pranay Bruhhda")

# with open("out.mp3", "wb") as file:
#     file.write(audio_bytes)


# --------- TEXT TO SPEECH TESTING -----------------------------

# from modules.speech.speech_to_text import SpeechToText
# import asyncio
# speechToText = SpeechToText()

# with open("out.mp3", "rb") as f:
#     audio_bytes = f.read()

# async def main() :
#     result = await speechToText.transcribe(audio_bytes)
#     print(result)

# asyncio.run(main())


# --------- IMAGE ANALYSING TESTING -----------------------------

# from modules.image.image_to_text import ImageToText
# image_to_text = ImageToText()
# import asyncio
# async def main() :
#     #  with bytes data as argument passed
#     with open("IMAGE.png","rb") as f :
#         response = await image_to_text.analyze_image(f.read())
#         print(response)
#     # with file path as argument passed
#     # response = await image_to_text.analyze_image("IMAGE.png")
#     # print(response)

# asyncio.run(main())



# ---------------- TEXT TO IMAGE TESTING -------------------------------------
from modules.image.text_to_image import TextToImage
import asyncio

async def main():
    text_to_image = TextToImage()
    image_bytes = await text_to_image.generate_image(
        prompt="A beautiful snowy mountain under a twilight sky with pine trees covered in snow", 
        output_path=""
        )
    with open("out.png", "wb") as file:
        file.write(image_bytes)

asyncio.run(main())