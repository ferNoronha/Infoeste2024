from transformers import AutoModel
from PIL import Image
import requests

print("LOAD MODEL")
model = AutoModel.from_pretrained('jinaai/jina-clip-v1', trust_remote_code=True)

def get_vector(image):
    return model.encode_image(Image.open(image))