import base64
import logging
import os
from groq import Groq
from dotenv import load_dotenv
from typing import Union
load_dotenv()
class ImageToTextError(Exception) : 
        pass
class ImageToText : 
    """Handles image-to-text conversion using Groq's vision capabilities"""

    def __init__(self):
        self._client = Groq(api_key=os.getenv("GROQ_API_KEY"))
        self.logger = logging.getLogger(__name__)

    async def analyze_image(self, image_data : Union[str,bytes], prompt : str = "")->str:   
        #  image_data: Either a file path (str) or binary image data (bytes)
        try : 
            if isinstance(image_data,str):
                if not os.path.exists(image_data):
                    raise ValueError(f"Image file not found: {image_data}")
                with open(image_data, "rb") as f:
                    image_bytes = f.read()
            else : 
                image_bytes = image_data

            if not image_bytes:
                raise ValueError("Image data cannot be empty")
            
            base64_image = base64.b64encode(image_bytes).decode("utf-8")
            if not prompt:
                prompt = "Please describe what you see in this image in detail."
            
            # message for calling the vision API
            messages = [
                {
                    "role" : "user",
                    "content" : [
                        {
                            "type" : "text",
                            "text": prompt
                        },
                        {
                            "type":"image_url",
                            "image_url": {
                                "url" : f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ]

            response = self._client.chat.completions.create(
                model="meta-llama/llama-4-scout-17b-16e-instruct",
                messages=messages,
                max_tokens=1000
            )

            if not response.choices : 
                raise ImageToTextError("No response received from the vision model")
            
            result = response.choices[0].message.content
            self.logger.info(f"Generated image description: {result}")

            return result

        except Exception as e :
            raise ImageToTextError(f"Failed to analyze image: {str(e)}") from e