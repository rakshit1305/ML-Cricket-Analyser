import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import VotingRegressor

-----------------------------
LOAD PIPELINE OR MODELS
-----------------------------
Assuming you have your trained Voting Regressor saved as 'voting_reg.pkl'
And encoders/scalers saved as 'batting_team_encoder.pkl', etc.

voting_reg = pickle.load(open("voting_reg.pkl", "rb"))
batting_team_encoder = pickle.load(open("batting_team_encoder.pkl", "rb"))
bowling_team_encoder = pickle.load(open("bowling_team_encoder.pkl", "rb"))
city_encoder = pickle.load(open("city_encoder.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

-----------------------------
CUSTOM CRICKET THEME STYLING
-----------------------------

page_bg = """

"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("🏏 Cricket Match Runs Prediction")

-----------------------------
USER INPUTS
-----------------------------

st.header("Enter Match Details")

batting_team = st.selectbox("Batting Team",
["Australia","India","Pakistan","England","Sri Lanka","Bangladesh","South Africa","New Zealand","Afghanistan","West Indies"])
bowling_team = st.selectbox("Bowling Team",
["Australia","India","Pakistan","England","Sri Lanka","Bangladesh","South Africa","New Zealand","Afghanistan","West Indies"])
city = st.selectbox("City", ["Mumbai", "Delhi", "Chennai", "Kolkata", "Bangalore", "Lahore", "Karachi", "Sydney", "Auckland", "Colombo"])

current_score = st.number_input("Current Score", min_value=0, max_value=500, value=100)
balls_bowled = st.number_input("Balls Bowled", min_value=0, max_value=120, value=60)
wickets_left = st.number_input("Wickets Left", min_value=0, max_value=10, value=5)
runs_last_3_overs = st.number_input("Runs in Last 3 Overs", min_value=0, max_value=60, value=20)

Calculate CRR

crr = (current_score / (balls_bowled / 6)) if balls_bowled != 0 else 0

-----------------------------
PREDICTION
-----------------------------

if st.button("Predict Final Score"):

# Encode categorical variables
batting_encoded = batting_team_encoder.transform([batting_team])[0]
bowling_encoded = bowling_team_encoder.transform([bowling_team])[0]
city_encoded = city_encoder.transform([city])[0]

# Prepare DataFrame
X_new = pd.DataFrame([{
    'batting_team': batting_encoded,
    'bowling_team': bowling_encoded,
    'current_score': current_score,
    'balls_bowled': balls_bowled,
    'wickets_left': wickets_left,
    'runs_last_3_overs': runs_last_3_overs,
    'crr': crr,
    'city': city_encoded
}])

# Scale numeric features (if your pipeline requires)
numeric_features = ['current_score', 'balls_bowled', 'wickets_left', 'runs_last_3_overs', 'crr']
X_new[numeric_features] = scaler.transform(X_new[numeric_features])

# Predict
predicted_runs = voting_reg.predict(X_new)[0]
st.success(f"🏏 Predicted Final Score: {predicted_runs:.2f} runs")
