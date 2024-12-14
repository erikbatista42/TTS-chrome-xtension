import os
import sys
from flask import Flask, request, jsonify
from elevenlabs import ElevenLabs
from flask_cors import CORS
import pygame
import traceback
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize pygame mixer for audio playback
pygame.mixer.init()

# Get API key and validate
api_key = os.getenv('ELEVEN_LABS_API_KEY')
if not api_key:
    print("ERROR: ELEVEN_LABS_API_KEY environment variable is not set!")
    sys.exit(1)

# Initialize Eleven Labs client
try:
    client = ElevenLabs(api_key=api_key)
except Exception as e:
    print(f"Failed to initialize Eleven Labs client: {e}")
    sys.exit(1)

@app.route('/play-audio', methods=['GET'])
def play_audio():
    text = request.args.get('text', '')
    print(f"Received text: {text}")  # Debugging print

    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    try:
        # Generate speech using Eleven Labs client method
        audio = client.text_to_speech.convert(
            voice_id="21m00Tcm4TlvDq8ikWAM",
            model_id="eleven_multilingual_v2",
            text=text
        )
        
        # Return the audio data directly with the correct content type
        return audio, 200, {'Content-Type': 'audio/mpeg'}
    
    except Exception as e:
        print(f"Error occurred: {e}")
        traceback.print_exc()
        return jsonify({"error": str(e), "traceback": traceback.format_exc()}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)