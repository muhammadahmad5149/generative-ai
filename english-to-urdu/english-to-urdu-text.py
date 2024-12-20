from googletrans import Translator

# Create a Translator object
translator = Translator()

# Text to translate
english_text = "Hello, how are you?"

# Translate to Urdu
translation = translator.translate(english_text, src='en', dest='ur')

# Display the translation
print(f"English: {english_text}")
print(f"Urdu: {translation.text}")
