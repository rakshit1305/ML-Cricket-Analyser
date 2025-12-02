# app.py
import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
pipeline = joblib.load("cricket_pipeline.pkl")

# Page configuration
st.set_page_config(page_title="Cricket Score Predictor", page_icon="🏏")
st.title("🏏 Cricket Score Predictor")

st.markdown("""
Predict the final score of an innings based on current match situation.
""")

# ====== User Inputs ======
batting_team = st.selectbox(
    "Batting Team", ["Sri Lanka", "India", "Pakistan", "Australia"]
)
bowling_team = st.selectbox(
    "Bowling Team", ["Sri Lanka", "India", "Pakistan", "Australia"]
)
current_score = st.number_input("Current Score", min_value=0, value=100)
balls_bowled = st.number_input("Balls Bowled", min_value=0, value=60)
wickets_left = st.number_input("Wickets Left", min_value=0, max_value=10, value=5)
runs_last_3_overs = st.number_input("Runs in Last 3 Overs", min_value=0, value=20)
crr = st.number_input("Current Run Rate (CRR)", min_value=0.0, step=0.01, value=6.5)
city = st.selectbox("City", ["Lahore", "Dubai", "Mumbai", "Karachi"])

# ====== Predict Button ======
if st.button("Predict Final Score"):
    # Prepare input data
    match_data = pd.DataFrame([{
        'batting_team': batting_team,
        'bowling_team': bowling_team,
        'current_score': int(current_score),
        'balls_bowled': int(balls_bowled),
        'wickets_left': int(wickets_left),
        'runs_last_3_overs': int(runs_last_3_overs),
        'crr': float(crr),
        'city': city
    }])
    
    # Predict using pipeline
    predicted_runs = int(round(pipeline.predict(match_data)[0]))
    
    # Display result
    st.success(f"🏏 Predicted Final Runs: {predicted_runs}")
