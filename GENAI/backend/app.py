import os
from flask import Flask, request, jsonify, render_template  # Import render_template
from flask_cors import CORS
import requests
from dotenv import load_dotenv

# ... (rest of your code remains the same)

load_dotenv()

app = Flask(__name__,
            static_folder=os.path.join("..", "frontend", "static"),  # For static files (if you have any)
            template_folder=os.path.join("..", "frontend", "templates")) # For HTML templates

CORS(app)

GOOGLE_CLOUD_API_KEY = os.getenv("GOOGLE_CLOUD_API_KEY")

if not GOOGLE_CLOUD_API_KEY:
    raise ValueError("GOOGLE_CLOUD_API_KEY environment variable not set.")

@app.route('/get_nutrition', methods=['POST'])
def get_nutrition():
    data = request.get_json()
    food_input = data.get('query')

    if not food_input:
        return jsonify({'error': 'No food input provided'}), 400

    api_url = f'https://language.googleapis.com/v1/documents:analyzeEntities?key={GOOGLE_CLOUD_API_KEY}'
    payload = {
        "document": {
            "type": "PLAIN_TEXT",
            "content": food_input
        },
        "features": {
            "extractEntities": {}
        }
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        api_data = response.json()
        return jsonify(api_data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

@app.route('/') # Serve the main HTML page
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)