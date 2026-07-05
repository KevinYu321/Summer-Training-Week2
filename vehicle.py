import requests
import base64#llava格式要求限制


def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_names = ["20250410_170653_工程_輪胎.jpg", "20250410_171709_carry_cars.jpg", "20250417_165128_carry_pigs.jpg", "20250521_172936_橘色平板含掛勾.jpg"]

for image_path in image_names:
    image_path = "llava/" + image_path
    image_base64 = encode_image_to_base64(image_path)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llava:latest",
            "prompt": "For the nearest vehicle in the picture. Describe its brand, color and model.",
            "images": [image_base64],
            "stream": False
        }
    )

    result = response.json()
    print(image_path, ":")
    print(result["response"])