import streamlit as st
import pandas as pd
import pickle
# -------------------
# User inputs
# -------------------
with open('cricket_pipeline_bits.pkl', 'rb') as f:
    pipeline = pickle.load(f)
batting_team = st.selectbox("Select Batting Team", ['Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Australia', 'England'])
bowling_team = st.selectbox("Select Bowling Team", ['Bangladesh', 'India', 'Pakistan', 'Sri Lanka', 'Australia', 'England'])
city = st.selectbox("Select City", ['Dhaka', 'Lahore', 'Mumbai', 'Colombo', 'Sydney', 'London'])

current_score = st.number_input("Current Score", min_value=0, step=1)
balls_bowled = st.number_input("Balls Bowled", min_value=0, max_value=120, step=1)
wickets_left = st.number_input("Wickets Left", min_value=0, max_value=10, step=1)
runs_last_3_overs = st.number_input("Runs in Last 3 Overs", min_value=0, step=1)
crrr = st.number_input("Enter Current Run Rate (CRR)", min_value=0.0, step=0.01)

# -------------------
# Create DataFrame
# -------------------
X_new = pd.DataFrame([{
    'batting_team': batting_team,
    'bowling_team': bowling_team,
    'city': city,
    'current_score': current_score,
    'balls_bowled': balls_bowled,
    'wickets_left': wickets_left,
    'runs_last_3_overs': runs_last_3_overs,
    'crr': crr   # Matches pipeline column
}])

# -------------------
# Predict using pipeline
# -------------------
predicted_runs = pipeline.predict(X_new)[0]
st.write(f"Predicted Runs: {predicted_runs:.1f}")
