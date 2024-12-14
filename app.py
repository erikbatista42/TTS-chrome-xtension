from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from gtts import gTTS  # You'll need to install this: pip install gTTS
import os
import tempfile

app = Flask(__name__)
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

# Add a root route for testing
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Server is running"})

# Make sure the route exactly matches '/tts'
@app.route('/tts', methods=['POST'])
def text_to_speech():
    print("Received TTS request")  # Debug print
    try:
        data = request.get_json()
        text = data.get('text', '')
        print(f"Processing text: {text}")  # Debug print
        
        return jsonify({
            "success": True,
            "message": f"Processed text: {text}"
        })
    except Exception as e:
        print(f"Error: {str(e)}")  # Debug print
        return jsonify({
            "success": False,
            "error": str(e)
        }), 400

@app.route('/play-audio', methods=['GET'])
def play_audio():
    try:
        text = request.args.get('text', '')
        if not text:
            return jsonify({"error": "No text provided"}), 400

        # Create a temporary file for the audio
        temp_dir = tempfile.gettempdir()
        temp_audio = os.path.join(temp_dir, 'speech.mp3')

        # Generate audio file
        tts = gTTS(text=text, lang='en')
        tts.save(temp_audio)

        # Send the audio file
        return send_file(
            temp_audio,
            mimetype='audio/mpeg',
            as_attachment=True,
            download_name='speech.mp3'
        )

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Server starting on http://localhost:5001")  # Debug print
    app.run(host='localhost', port=5001, debug=True) 