import streamlit as st
import pandas as pd
import pickle

# -------------------
# Load pipeline
# -------------------
with open('cricket_pipeline_bits.pkl', 'rb') as f:
    pipeline = pickle.load(f)

# -------------------
# User inputs
# -------------------
batting_team = st.selectbox("Select Batting Team", 
    ['Australia', 'India', 'Bangladesh', 'New Zealand',
     'South Africa', 'England', 'West Indies', 
     'Afghanistan', 'Pakistan', 'Sri Lanka'])

bowling_team = st.selectbox("Select Bowling Team", 
    ['Australia', 'India', 'Bangladesh', 'New Zealand',
     'South Africa', 'England', 'West Indies', 
     'Afghanistan', 'Pakistan', 'Sri Lanka'])

city = st.selectbox("Select City", [
    'Colombo', 'Kandy', 'Dambulla', 'Hambantota',
    'Napier', 'Mount Maunganui', 'Auckland', 'Wellington', 'Hamilton',
    'Christchurch', 'Dunedin', 'Nelson', 'Queenstown',
    'Dhaka', 'Chattogram', 'Sylhet', 'Mirpur',
    'Southampton', 'Taunton', 'Cardiff', 'Chester-le-Street', 'Birmingham',
    'Manchester', 'Nottingham', 'Leeds', 'Bristol', 'London',
    'Bloemfontein', 'Potchefstroom', 'East London', 'Durban',
    'Port Elizabeth', 'Gqeberha', 'Centurion', 'Cape Town', 'Paarl',
    'Kanpur', 'Nagpur', 'Bangalore', 'Bengaluru', 'Ranchi', 'Guwahati',
    'Delhi', 'Rajkot', 'Thiruvananthapuram', 'Cuttack', 'Indore',
    'Mumbai', 'Kolkata', 'Lucknow', 'Chennai', 'Visakhapatnam',
    'Hyderabad', 'Chandigarh', 'Pune', 'Jaipur', 'Dharamsala',
    'Lahore', 'Karachi', 'Rawalpindi',
    'Hobart', 'Adelaide', 'Melbourne', 'Sydney', 'Canberra',
    'Perth', 'Darwin', 'Cairns',
    'Barbados', 'Trinidad', 'Jamaica', 'St Kitts', 'Gros Islet',
    'Basseterre', 'Coolidge', 'Bridgetown', "St George's",
    'Tarouba', 'Kingstown', 'St Lucia', 'Antigua', 'St Vincent',
    'Providence', 'Guyana'
])

current_score = st.number_input("Current Score", min_value=0, step=1)
balls_bowled = st.number_input("Balls Bowled", min_value=18, max_value=120, step=1)
wickets_left = st.number_input("Wickets Left", min_value=0, max_value=10, step=1)
runs_last_3_overs = st.number_input("Runs in Last 3 Overs", min_value=0, step=1)

# -------------------
# Predict button
# -------------------
if st.button("Predict Score"):
    # Create DataFrame for prediction
    X_new = pd.DataFrame([{
        'batting_team': batting_team,
        'bowling_team': bowling_team,
        'city': city,
        'current_score': current_score,
        'balls_bowled': balls_bowled,
        'wickets_left': wickets_left,
        'runs_last_3_overs': runs_last_3_overs,
        'crrr': (current_score / balls_bowled) * 6  # run rate per over
    }])

    # Predict using pipeline
    predicted_runs = pipeline.predict(X_new)[0]
    st.success(f"Predicted Runs: {predicted_runs:.1f}")
