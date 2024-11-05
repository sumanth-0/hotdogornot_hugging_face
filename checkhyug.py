import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your Hugging Face API URL and token
API_URL = "https://api-inference.huggingface.co/models/julien-c/hotdog-not-hotdog"
API_TOKEN = os.getenv("HUGGING_FACE_API_TOKEN", "put ur key")

# Prepare headers with the Authorization token
headers = {'Authorization': f'Bearer {API_TOKEN}'}

# Function to check the API key
def check_api_key():
    try:
        response = requests.get(API_URL, headers=headers)
        if response.status_code == 200:
            print("API key is working!")
            print("Response:", response.json())
        else:
            print("API key is not working.")
            print("Status Code:", response.status_code)
            print("Response:", response.json())
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    check_api_key()
