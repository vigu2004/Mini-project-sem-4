from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
from keras.models import load_model

app = Flask(__name__)

# Load the model
model = load_model("model.h5")

# Define preprocessing function
def preprocess_image(image_path):
    image = Image.open(image_path)
    # Resize image to (64, 32)
    image = image.resize((32, 32))
    # Convert image to numpy array
    image_array = np.array(image)
    # Expand dimensions to match batch size
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

@app.route('/')
def home():
    return render_template('melanoma.html')
@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    image_file = request.files['file']
    # Save the image file temporarily
    image_path = "temp.jpg"
    image_file.save(image_path)
    # Preprocess the image
    image = preprocess_image(image_path)
    # Make prediction
    predictions = model.predict(image)
    # Get the predicted class
    predicted_class = int(np.argmax(predictions))
    # Return the predicted class
    return jsonify({'predicted_class': predicted_class})
if __name__ == '__main__':
    app.run(debug=True)
