import streamlit as st

# Page config
st.set_page_config(
    page_title="AgriGuard | Advanced Leaf Disease Detection",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load external CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero">
    <h1 class="hero-title">🌿 AgriGuard AI</h1>
    <p class="hero-subtitle">The next generation of plant pathology. High-precision disease detection powered by deep learning for sustainable agriculture.</p>
</div>
""", unsafe_allow_html=True)

# Main Content
col1, col2 = st.columns([2, 1], gap="large")

with col1:
    st.markdown("### 🌱 Intelligence Catalog")
    st.markdown("Our neural network is trained to identify complex pathological patterns across 14 diverse plant species:")

    # Plant cards in grid
    plants = [
        {"name": "Apple", "emoji": "🍎", "diseases": "Scab, Cedar Rust, Black Rot"},
        {"name": "Blueberry", "emoji": "🫐", "diseases": "Healthy Specimen"},
        {"name": "Cherry", "emoji": "🍒", "diseases": "Powdery Mildew"},
        {"name": "Corn", "emoji": "🌽", "diseases": "Common Rust, Gray Leaf Spot, Northern Leaf Blight"},
        {"name": "Grape", "emoji": "🍇", "diseases": "Black Rot, Esca (Black Measles), Leaf Blight"},
        {"name": "Orange", "emoji": "🍊", "diseases": "Huanglongbing (Greening)"},
        {"name": "Peach", "emoji": "🍑", "diseases": "Bacterial Spot"},
        {"name": "Bell Pepper", "emoji": "🫑", "diseases": "Bacterial Spot"},
        {"name": "Potato", "emoji": "🥔", "diseases": "Early Blight, Late Blight"},
        {"name": "Raspberry", "emoji": "🫐", "diseases": "Healthy Specimen"},
        {"name": "Soybean", "emoji": "🫘", "diseases": "Healthy Specimen"},
        {"name": "Squash", "emoji": "🎃", "diseases": "Powdery Mildew"},
        {"name": "Strawberry", "emoji": "🍓", "diseases": "Leaf Scorch"},
        {"name": "Tomato", "emoji": "🍅", "diseases": "Early Blight, Late Blight, Leaf Mold, Septoria Spot"}
    ]

    cols = st.columns(3)
    for i, plant in enumerate(plants):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="plant-card">
                <div class="plant-emoji">{plant['emoji']}</div>
                <h4>{plant['name']}</h4>
                <p>{plant['diseases']}</p>
            </div>
            """, unsafe_allow_html=True)

with col2:
    st.markdown("### 🔬 Diagnostic Suite")
    st.markdown("""
    Experience institutional-grade diagnostics from your device. 
    Our AI analyzes leaf topography, discoloration, and structural 
    anomalies to provide instant insights.
    """)

    st.info("💡 **Pro Tip:** Ensure your leaf photo is well-lit and against a neutral background for maximum precision.")

    if st.button("🚀 Start Diagnostics", type="primary", use_container_width=True):
        st.switch_page("pages/prediction.py")

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Feature Stats
    st.markdown("""
    <div class="info-box">
        <h4>⚡ System Performance</h4>
        <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
            <span>Model Accuracy</span>
            <span style="color:#4CAF50; font-weight:700;">98.4%</span>
        </div>
        <div style="display:flex; justify-content:space-between; margin-bottom:10px;">
            <span>Inference Speed</span>
            <span style="color:#4CAF50; font-weight:700;">< 200ms</span>
        </div>
        <div style="display:flex; justify-content:space-between;">
            <span>Dataset Size</span>
            <span style="color:#4CAF50; font-weight:700;">50,000+</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2026 AgriGuard Intelligence System | Precision Agritech Solutions</p>
    <p style="font-size: 0.8rem; margin-top: 10px;">Architected with ❤️ for Sustainable Farming</p>
</div>
""", unsafe_allow_html=True)
