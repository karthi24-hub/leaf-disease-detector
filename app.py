import streamlit as st
from PIL import Image
import os
from predict import predict_disease

# Page config
st.set_page_config(page_title="Leaf Disease Detector", page_icon="🍃", layout="centered")

# Load external CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title and subtitle
st.markdown('<div class="title">🌿 Leaf Disease Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Using AI to detect plant leaf diseases with precision 🍀</div>', unsafe_allow_html=True)

# Upload image
uploaded_file = st.file_uploader("📤 Upload a leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="✅ Image Uploaded", use_container_width=True)

    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    if st.button("🔍 Predict Disease"):
        with st.spinner("🔎 Analyzing... Hang tight!"):
            label, confidence = predict_disease("temp.jpg")

        st.markdown(f"""
            <div class="result">
                <h4>🦠 <strong>Prediction:</strong> <span style='color:#1b5e20'>{label}</span></h4>
                <p>🎯 <strong>Confidence:</strong> {confidence:.2f}%</p>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 3rem; font-size: 0.9rem; color: #2e7d32; animation: fadeIn 2s ease-in-out;'>
       <h3> 🚀 Developed by <strong>Karthi</strong></h3>
    </div>
""", unsafe_allow_html=True)
