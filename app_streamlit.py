import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from PIL import Image

# ===== Load trained ML pipeline =====
pipeline = joblib.load("cricket_pipeline.pkl")

# ===== Page setup =====
st.set_page_config(page_title="Advanced Cricket Predictor", page_icon="🏏")
st.title("🏏 Advanced Cricket Score Predictor")
st.markdown("Predict the final score of an innings with interactive visuals and team logos.")

# ===== Teams and cities =====
teams = ["Sri Lanka", "India", "Pakistan", "Australia"]
cities = ["Lahore", "Dubai", "Mumbai", "Karachi"]

# ===== Team Logos =====
logo_path = "logos/"

# ===== User Inputs =====
batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)

# Show team logos
col1, col2 = st.columns(2)
with col1:
    st.image(Image.open(f"{logo_path}{batting_team}.png"), width=100, caption=f"{batting_team}")
with col2:
    st.image(Image.open(f"{logo_path}{bowling_team}.png"), width=100, caption=f"{bowling_team}")

current_score = st.slider("Current Score", 0, 400, 100, help="Score at current moment")
balls_bowled = st.slider("Balls Bowled", 0, 120, 60, help="Total balls bowled so far")
wickets_left = st.slider("Wickets Left", 0, 10, 5, help="Wickets remaining")
runs_last_3_overs = st.slider("Runs in Last 3 Overs", 0, 60, 20)
crr = st.number_input("Current Run Rate (CRR)", min_value=0.0, value=6.5, step=0.01)
city = st.selectbox("City", cities)

# ===== Predict Button =====
if st.button("Predict Final Score"):
    # Prepare input
    df = pd.DataFrame([{
        'batting_team': batting_team,
        'bowling_team': bowling_team,
        'current_score': int(current_score),
        'balls_bowled': int(balls_bowled),
        'wickets_left': int(wickets_left),
        'runs_last_3_overs': int(runs_last_3_overs),
        'crr': float(crr),
        'city': city
    }])
    
    # Predict final runs
    predicted_runs = int(round(pipeline.predict(df)[0]))
    
    # Show result with suggestion
    if predicted_runs > 250:
        st.success(f"🏏 Predicted Final Runs: {predicted_runs} – High Scoring Match!")
    elif predicted_runs < 150:
        st.warning(f"🏏 Predicted Final Runs: {predicted_runs} – Low Scoring Match!")
    else:
        st.info(f"🏏 Predicted Final Runs: {predicted_runs} – Average Scoring Match")
    
    # ===== Projected Score Over Each 5 Over Segment =====
    segments = 6  # divide remaining overs into 6 segments
    projected_scores = [current_score + i*(predicted_runs-current_score)//segments for i in range(segments+1)]
    plt.figure(figsize=(8,4))
    plt.plot(range(len(projected_scores)), projected_scores, marker='o', color='orange')
    plt.title("Projected Score Progression")
    plt.xlabel("Over Segments")
    plt.ylabel("Runs")
    plt.grid(True)
    st.pyplot(plt)
    
    # ===== Bar Chart Comparison =====
    st.bar_chart({"Current Score": [current_score], "Predicted Final Score": [predicted_runs]})
