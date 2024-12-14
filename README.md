# Text-to-Speech Chrome Extension

A Chrome extension that converts selected text to speech using a local Flask server and Google's Text-to-Speech service.

## Features

- Right-click context menu integration
- Convert selected text to speech
- Simple and easy-to-use interface
- Local server processing

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.7+
- Google Chrome browser
- pip (Python package manager)

## Installation

1. Clone the repository:
bash
git clone [your-repository-url]
cd [repository-name]

2. Install Python dependencies:
pip install flask flask-cors gtts

3. Create a `.env` file in the root directory (optional):

4. Load the Chrome extension:
   - Open Chrome and navigate to `chrome://extensions/`
   - Enable "Developer mode" in the top right
   - Click "Load unpacked"
   - Select the extension directory containing `manifest.json`

## Running the Server

1. Start the Flask server:
python app.py

he server will start on `http://localhost:5001`

## Using the Extension

1. Select any text on a webpage
2. Right-click the selected text
3. Choose "Convert to Speech" from the context menu
4. The selected text will be converted to speech and played

## Project Structure

- `app.py`: Flask server code
- `background.js`: Chrome extension background script
- `content.js`: Content script for page interaction
- `manifest.json`: Chrome extension manifest file
- `requirements.txt`: Python dependencies
- `README.md`: This file


## Troubleshooting

- If you hear no audio, ensure the Flask server is running
- If you get a 404 error, check that the server is running on port 5001
- If you get CORS errors, ensure the Flask server's CORS settings are correct

## Development

To modify the extension:
1. Make your changes to the relevant files
2. Reload the extension in `chrome://extensions/`
3. Refresh any tabs where you want to test the extension

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- Google Text-to-Speech service
- Flask framework
- Chrome Extensions API