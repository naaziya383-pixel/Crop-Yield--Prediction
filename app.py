import streamlit as st

st.set_page_config(page_title="Crop Yield Predictor", layout="centered")

st.title("🌱 Smart Crop Yield Prediction")
st.markdown("---")

# Input Section - Line by Line
st.header("Enter Details Below:")

state = st.selectbox("📍 Select State", ["Punjab", "Haryana", "UP", "Maharashtra", "Gujarat"])
district = st.text_input("🏙️ Enter District Name")
crop = st.selectbox("🌾 Select Crop", ["Wheat", "Rice", "Cotton", "Sugarcane", "Maize"])
season = st.radio("📅 Season", ["Kharif", "Rabi", "Whole Year"])

st.markdown("---")

# Technical Parameters
area = st.number_input("📏 Area (in Hectares)", min_value=1, value=10)
temp = st.slider("🌡️ Average Temperature (°C)", 10, 50, 25)
soil_type = st.selectbox("🌍 Soil Type", ["Alluvial", "Black", "Red", "Sandy"])
irrigation = st.select_slider("💧 Irrigation Level", options=["Low", "Medium", "High"])

# Ma'am ke liye special point: Fertilizer
fertilizer = st.slider("🧪 Fertilizer Input (kg/hectare)", 0, 500, 100)

st.markdown("---")

if st.button("🚀 Predict Yield"):
    # Simple logic for Demo
    prediction = (area * temp * 0.5) + (fertilizer * 0.1)
    st.success(f"✅ Estimated Yield: {prediction:.2f} Metric Tons")
    st.balloons()
