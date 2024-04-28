from flask import Flask, request, jsonify, render_template
from PIL import Image
import numpy as np
from keras.models import load_model

app = Flask(__name__)


model = load_model("model.h5")


def preprocess_image(image_path):
    image = Image.open(image_path)
    
    image = image.resize((32, 32))
    
    image_array = np.array(image)
    
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

@app.route('/')
def home():
    return render_template('melanoma.html')
@app.route('/predict', methods=['POST'])
def predict():
    
    image_file = request.files['file']
    
    image_path = "temp.jpg"
    image_file.save(image_path)
    
    image = preprocess_image(image_path)
    
    predictions = model.predict(image)
    
    predicted_class = int(np.argmax(predictions))
    
    return jsonify({'predicted_class': predicted_class})
if __name__ == '__main__':
    app.run(debug=True)
