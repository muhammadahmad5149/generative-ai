from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "you_key"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    prompt = request.form['prompt']
    print(prompt)
    try:
        # Generate an image using DALL·E
        response = openai.Image.create(
            prompt=prompt,  # This is the prompt to generate the image
            n=1,  # Generate one image
            size="256x256"  # You can adjust the size (256x256, 512x512, 1024x1024)
        )
        # Get the URL of the generated image
        print(response)
        image_url = response['data'][0]['url']
        
        # Render the image on the page
        return render_template('story.html', prompt=prompt, image_url=image_url)
    except Exception as e:
        print(e)
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
