
import numpy as np
from PIL import Image

def preprocess_image(uploaded_file):

    image = Image.open(uploaded_file)

    image = image.convert("RGB")

    image_array = np.array(image)

    if image_array.size == 0:
        raise ValueError("Invalid image")

    return image_array
