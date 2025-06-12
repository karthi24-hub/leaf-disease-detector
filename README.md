# 🌿 Leaf Disease Detector

An AI-powered web application built with **Streamlit** to detect and classify plant leaf diseases using a Convolutional Neural Network (CNN). This tool is designed to help farmers and researchers identify plant health issues early with precision.

![App Screenshot](assets/screenshot.png) <!-- Replace with an actual screenshot if available -->

---

## 🚀 Features

- 📤 Upload a leaf image (JPG, JPEG, PNG formats)
- 🤖 Real-time prediction using a trained CNN model
- 🎯 Displays disease name and confidence score
- 🎨 Custom UI with animated background and responsive design
- ✅ Simple and intuitive interface for non-technical users

---

## 🧠 Model Info

- Framework: **TensorFlow / Keras**
- Architecture: Custom CNN model
- Classes: Tomato Leaf Diseases (e.g., Mosaic Virus, Bacterial Spot, etc.)
- Preprocessed with data augmentation and normalization techniques

---

## 🛠️ Tech Stack

| Component    | Description              |
|--------------|--------------------------|
| `Streamlit`  | Web frontend framework   |
| `Python`     | Core backend logic       |
| `TensorFlow` | Deep learning model      |
| `CSS`        | Custom animations & styling |
| `Matplotlib` | Optional visualization   |

---

## 📂 Directory Structure

---

## ▶️ How to Run the Project

1. **Clone the Repository**

```bash
git clone https://github.com/karthi24-hub/leaf-disease-detector.git
cd leaf-disease-detector
pip install -r requirements.txt
streamlit run app.py

