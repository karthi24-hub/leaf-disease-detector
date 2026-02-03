from flask import Flask, request, jsonify
import os
import json
from predict import predict_disease
from datetime import datetime

app = Flask(__name__)

# Directory to save incoming IoT images
UPLOAD_FOLDER = 'iot_uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# File to store the latest monitoring data
LOG_FILE = 'iot_data.json'

@app.route('/api/monitor', methods=['POST'])
def monitor():
    try:
        # 1. Get image file
        if 'image' not in request.files:
            return jsonify({"error": "No image part"}), 400
        
        file = request.files['image']
        temp_path = os.path.join(UPLOAD_FOLDER, "latest_capture.jpg")
        file.save(temp_path)

        # 2. Get sensor data
        temperature = request.form.get('temperature', 'N/A')
        humidity = request.form.get('humidity', 'N/A')

        # 3. Perform Disease Detection
        label, confidence = predict_disease(temp_path)
        confidence_pct = round(float(confidence) * 100, 2)
        clean_label = label.replace('_', ' ').title()

        # 4. Determine Health Status (0 for Healthy, 1 for Disease)
        status_code = 0 if "healthy" in label.lower() else 1

        # 5. Prepare result
        data = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "temperature": temperature,
            "humidity": humidity,
            "prediction": clean_label,
            "confidence": f"{confidence_pct}%",
            "image_path": temp_path,
            "status_code": status_code
        }

        # 6. Save to log file for Streamlit to read
        with open(LOG_FILE, 'w') as f:
            json.dump(data, f)

        print(f"[{data['timestamp']}] Temp: {temperature}C, Hum: {humidity}%, Result: {clean_label}, Status: {status_code}")

        return jsonify({"status": "success", "prediction": clean_label, "status_code": status_code}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run server on your laptop. 
    # Use your laptop's local IP (e.g., 192.168.1.5) so ESP32 can find it.
    app.run(host='0.0.0.0', port=5000, debug=True)
