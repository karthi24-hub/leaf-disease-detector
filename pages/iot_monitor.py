import streamlit as st
import numpy as np
import sys
import os
import time
import requests
from io import BytesIO
from PIL import Image

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from predict import predict_disease
from disease_info import disease_info

# Page config
st.set_page_config(page_title="AgriGuard | Stable AI", page_icon="🌿", layout="wide")

# Navigation
if st.button("← Back to Dashboard", type="secondary"):
    st.switch_page("app.py")

st.markdown("""
<div class="page-header">
    <h1>🌿 Neural Field Monitor</h1>
    <p>Smooth live stream with background AI analysis. (Prevents FB-OVF errors)</p>
</div>
""", unsafe_allow_html=True)

# ESP32 Configuration
ESP32_IP = "192.168.31.55"  
STREAM_URL = f"http://{ESP32_IP}:81/"

col1, col2 = st.columns([1.5, 1], gap="large")

with col1:
    st.markdown("### 📡 Live Feed")
    # Show stream directly in browser (0% lag, 1 connection)
    st.markdown(f"""
        <div style="border: 5px solid #2ecc71; border-radius: 20px; overflow: hidden; background: #000; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
            <img src="{STREAM_URL}" width="100%" />
        </div>
    """, unsafe_allow_html=True)
    
    st.info("The live stream is running directly from the camera for maximum speed.")

with col2:
    st.markdown("### 📊 Automated AI Analysis")
    # A single button to toggle continuous background analysis
    detect_on = st.checkbox("🔍 Enable Continuous Auto-Detection", value=True)
    
    analysis_container = st.empty()
    result_container = st.empty()

# THE AI LOOP (Runs only if checked)
if detect_on:
    while True:
        try:
            # Instead of a heavy video connection, we just grab one frame quickly
            # using a request. This prevents the constant "fighting" for the stream.
            response = requests.get(STREAM_URL, timeout=1, stream=True)
            if response.status_code == 200:
                # We save a temporary frame from the stream
                with open("live_analysis.jpg", "wb") as f:
                    # Just grab a chunk enough for a frame
                    for chunk in response.iter_content(chunk_size=10240):
                        f.write(chunk)
                        break # Stop after one chunk to be fast
                
                # Perform prediction
                label, confidence = predict_disease("live_analysis.jpg")
                conf_pct = confidence * 100
                
                is_leaf = "background" not in label.lower()
                
                if is_leaf:
                    status_color = "#2ecc71" if "healthy" in label.lower() else "#e74c3c"
                    clean_label = label.replace('_', ' ').title()
                    
                    with analysis_container.container():
                        st.markdown(f"""
                        <div style="padding: 20px; border-radius: 15px; background: {status_color}11; border: 2px solid {status_color}; text-align: center;">
                            <p style="margin:0; font-size: 0.7rem; color: #666; text-transform: uppercase;">Detection Active</p>
                            <h2 style="margin: 5px 0; color: {status_color};">{clean_label}</h2>
                            <p style="font-weight: bold; margin:0;">{conf_pct:.1f}% Confidence</p>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    if label in disease_info:
                        with result_container.container():
                            st.divider()
                            st.markdown(f"**Cure:** {disease_info[label]['cure']}")
                else:
                    analysis_container.info("Searching for leaf specimen...")
                    result_container.empty()
            
            response.close()
        except Exception as e:
            # If the camera is busy, just wait a bit
            time.sleep(0.5)
            continue
            
        # Wait 2 seconds between AI checks to keep the camera stable
        time.sleep(2)
        st.rerun() # Refresh only the AI parts
else:
    analysis_container.warning("Auto-detection is paused. Enable it to see live AI results.")
