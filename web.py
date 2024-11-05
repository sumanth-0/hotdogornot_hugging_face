#web.py

#web.py

from flask import Flask, render_template, request, jsonify
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("HUGGING_FACE_API_URL", "https://api-inference.huggingface.co/models/julien-c/hotdog-not-hotdog")
API_TOKEN = os.getenv("HUGGING_FACE_API_TOKEN", "put ur key")
headers = {'Authorization': f'Bearer {API_TOKEN}'}
app = Flask(__name__)

def query(data):
    response = requests.request('POST', API_URL, headers=headers, data=data)
    return json.loads(response.content.decode('utf-8'))

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file1']
    modeldata = query(file)
    return jsonify(modeldata)


app.run(host='0.0.0.0', port=81)