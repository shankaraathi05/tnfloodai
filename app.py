import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
os.environ["STREAMLIT_SERVER_HEADLESS"] = "true"
st.set_option("client.showErrorDetails", False)
st.set_option("client.toolbarMode", "minimal")
from datetime import datetime

st.set_page_config(
    page_title="TN Flood AI Dashboard",
    page_icon="🌊",
    layout="wide"
)
st.markdown("""
<style>
.hero {
    background-image: url('https://images.unsplash.com/photo-1547683905-f686c993aae5');
    background-size: cover;
    background-position: center;
    padding: 60px;
    border-radius: 15px;
    margin-bottom: 20px;
}
.hero h1 {
    color: white;
    text-align: center;
    font-size: 42px;
}
</style>

<div class="hero">
    <h1> Tamil Nadu Flood Intelligence System</h1>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0a192f, #112240, #0f3460);
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    animation: fadeIn 1.5s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.glow-bg {
    position: fixed;
    top: -200px;
    left: -200px;
    width: 600px;
    height: 600px;
    background: radial-gradient(circle, rgba(0,198,255,0.3) 0%, transparent 70%);
    animation: floatGlow 10s infinite alternate ease-in-out;
    z-index: -1;
}

@keyframes floatGlow {
    0% { transform: translate(0px, 0px); }
    100% { transform: translate(200px, 150px); }
}
</style>
<div class="glow-bg"></div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(-45deg, #0f2027, #203a43, #2c5364, #1c1f26);
    background-size: 400% 400%;
    animation: gradientMove 15s ease infinite;
    color: white;
}

@keyframes gradientMove {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.block-container {
    background: rgba(255, 255, 255, 0.03);
    padding: 2rem;
    border-radius: 15px;
    backdrop-filter: blur(10px);
}

section[data-testid="stSidebar"] {
    background-color: #111827;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Poppins:wght@400;600&family=Roboto:wght@400;500&display=swap');

.hero h1 {
    font-family: 'Orbitron', sans-serif;
    letter-spacing: 2px;
}

h3 {
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
    color: #00C6FF;
}

body, .stMarkdown, .stText {
    font-family: 'Roboto', sans-serif;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.gov-header {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    padding: 20px;
    background: linear-gradient(90deg, #800000, #a52a2a);
    border-radius: 12px;
    margin-bottom: 20px;
}

.gov-header img {
    width: 80px;
}

.gov-header h1 {
    font-family: 'Orbitron', sans-serif;
    color: white;
    margin: 0;
}

.gov-header p {
    color: #f0f0f0;
    margin: 0;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stApp {
    background-color: #0E1117;
    color: white;
}

.stMetric {
    background-color: #1C1F26;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}

div[data-testid="stMetricValue"] {
    font-size: 28px;
    color: #00C6FF;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
# 🌊 AI-Based Flood Monitoring & Early Warning System
### Government of Tamil Nadu – Smart Disaster Management Dashboard
""")

district = st.selectbox("Select District", ["Chennai", "Madurai", "Trichy", "Coimbatore", "Cuddalore"])

st.sidebar.header("⚙️ Input Parameters")

rainfall = st.sidebar.slider("Rainfall (mm)", 0, 200, 50)
water_level = st.sidebar.slider("Water Level (%)", 0, 100, 40)
flow_rate = st.sidebar.slider("Drain Flow Rate (1-10)", 1, 10, 7)

risk_score = (rainfall * 0.4) + (water_level * 0.4) + ((10 - flow_rate) * 5)

predicted_rainfall = rainfall * 1.15
predicted_water_level = water_level * 1.10

future_risk_score = (predicted_rainfall * 0.4) + (predicted_water_level * 0.4) + ((10 - flow_rate) * 5)

st.write("### 🔮 AI Predicted Risk (Next 24 Hours):", round(future_risk_score, 2), "%")
st.write("### Current Flood Risk Score:", round(risk_score, 2), "%")

if risk_score > 80:
    banner_color = "#ff4b4b"
    banner_text = "🚨 HIGH FLOOD ALERT – IMMEDIATE ACTION REQUIRED"
elif risk_score > 50:
    banner_color = "#ffa500"
    banner_text = "⚠ MODERATE FLOOD RISK – MONITOR CLOSELY"
else:
    banner_color = "#28a745"
    banner_text = "✅ LOW FLOOD RISK – SAFE CONDITIONS"

st.markdown(f"""
<div style="
background-color:{banner_color};
padding:20px;
border-radius:10px;
text-align:center;
font-size:22px;
font-weight:bold;
color:white;">
{banner_text}
</div>
""", unsafe_allow_html=True)

from datetime import datetime
current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

st.markdown(f"""
<div style="text-align:right; font-size:14px; color:gray;">
🕒 Last Updated: {current_time}
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.metric("🌧 Rainfall (mm)", rainfall)
col2.metric("🌊 Water Level (%)", water_level)
col3.metric("⚠ Risk Score (%)", round(risk_score, 2))

if risk_score > 80:
    st.error("🔴 HIGH Flood Risk")
    st.info("📢 Alert Sent to Municipal Corporation")
    st.info("📩 SMS Warning Sent to Residents")
elif risk_score > 50:
    st.warning("🟡 Moderate Flood Risk")
else:
    st.success("🟢 Low Flood Risk")

st.write("### 📊 Flood Parameter Visualization")

data = pd.DataFrame({
    "Parameter": ["Rainfall", "Water Level", "Drain Risk"],
    "Value": [rainfall, water_level, (10 - flow_rate) * 10]
})

fig, ax = plt.subplots()
ax.bar(data["Parameter"], data["Value"])
ax.set_ylabel("Value")
st.pyplot(fig)

st.write("### 🏙️ District Risk Overview")

district_data = pd.DataFrame({
    "District": ["Chennai", "Madurai", "Trichy", "Coimbatore", "Cuddalore"],
    "Rainfall (mm)": [120, 60, 45, 30, 95],
    "Water Level (%)": [85, 55, 40, 35, 75],
    "Risk Status": ["High", "Moderate", "Low", "Low", "High"]
})

st.dataframe(district_data)

st.write("### 🗺️ Tamil Nadu Flood Monitoring Map")

map_data = pd.DataFrame({
    "District": ["Chennai", "Madurai", "Coimbatore"],
    "lat": [13.0827, 9.9252, 11.0168],
    "lon": [80.2707, 78.1198, 76.9558]
})

st.map(map_data)

report = f"""
Flood Monitoring Report
District: {district}
Rainfall: {rainfall} mm
Water Level: {water_level} %
Drain Flow Rate: {flow_rate}

Current Risk Score: {round(risk_score,2)} %
Predicted Risk (Next 24 hrs): {round(future_risk_score,2)} %
"""

st.download_button(
    label="📥 Download Flood Report",
    data=report,
    file_name="Flood_Report.txt",
    mime="text/plain"
)

st.markdown("---")

st.markdown("Developed by CSE Team | Government Hackathon 2026")
