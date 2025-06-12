import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

MODEL_PATH = "Z:\projects\leaf_disease_detector\saved_model\plant_disease_model.h5"
CLASS_NAMES_PATH = "Z:\projects\leaf_disease_detector\saved_model\class_names.txt"

# Load model and class names once
model = load_model(MODEL_PATH)

with open(CLASS_NAMES_PATH, "r") as f:
    class_names = [line.strip() for line in f.readlines()]

def predict_disease(img_path):
    try:
        img = image.load_img(img_path, target_size=(128, 128))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array)
        class_index = np.argmax(predictions[0])
        predicted_label = class_names[class_index]
        confidence = float(predictions[0][class_index])

        return predicted_label, confidence
    except Exception as e:
        return f"Error in prediction: {str(e)}", 0.0
