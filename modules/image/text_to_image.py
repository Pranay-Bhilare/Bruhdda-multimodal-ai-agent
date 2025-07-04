from together import Together
import os
import base64
import logging
from dotenv import load_dotenv
load_dotenv()
class TextToImageError(Exception):
    pass
class TextToImage() : 
    def __init__(self) -> None:
        self._together_client = Together()
        self.logger = logging.getLogger(__name__)
    async def generate_image(self,prompt:str,output_path:str = "")-> bytes:
        """Generate an image from a prompt using Together AI."""
        if not prompt.strip():
            raise ValueError("Prompt cannot be empty")
        try : 
            response = self._together_client.images.generate(
                prompt=prompt,
                model="black-forest-labs/FLUX.1-schnell-Free",
                width=1024,
                height=768,
                steps=4,
                n=1,
                response_format="b64_json"
            )
            image_data = base64.b64decode(response.data[0].b64_json)
            if output_path:
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                with open(output_path, "wb") as f:
                    f.write(image_data)
                self.logger.info(f"Image saved to {output_path}")

            return image_data
        except Exception as e : 
            raise TextToImageError(f"Failed to generate image : {str(e)}") from e