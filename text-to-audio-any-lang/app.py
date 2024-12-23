from flask import Flask, render_template, request, jsonify, send_file
from googletrans import Translator
from gtts import gTTS
from io import BytesIO
import os

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data or 'text' not in data or 'language' not in data:
            return jsonify({"error": "Invalid input"}), 400

        english_text = data['text']
        target_language = data['language']

        # Translate to the selected language
        translation = translator.translate(english_text, src='en', dest=target_language)
        translated_text = translation.text

        # Convert translated text to speech
        tts = gTTS(translated_text, lang=target_language)
        audio_stream = BytesIO()
        tts.write_to_fp(audio_stream)
        audio_stream.seek(0)  # Reset the stream position to the start

        # Return the audio file as a direct download
        return send_file(
            audio_stream,
            mimetype="audio/mpeg",
            as_attachment=True,
            download_name="translated_audio.mp3"
        )

    except Exception as e:
        print('Translation error:', e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
