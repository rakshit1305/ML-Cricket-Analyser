import streamlit as st
import pandas as pd
import pickle

# Load trained pipeline
with open('cricket_pipeline_bits.pkl', 'rb') as f:
    pipeline = pickle.load(f)

# Teams and cities
teams = [
    'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 
    'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
]

cities = [
    'Colombo', 'Kandy', 'Dambulla', 'Hambantota',  # Sri Lanka
    'Napier', 'Mount Maunganui', 'Auckland', 'Wellington', 'Hamilton', 'Christchurch', 'Dunedin', 'Nelson', 'Queenstown',  # NZ
    'Dhaka', 'Chattogram', 'Sylhet', 'Mirpur',  # Bangladesh
    'Southampton', 'Taunton', 'Cardiff', 'Chester-le-Street', 'Birmingham', 'Manchester', 'Nottingham', 'Leeds', 'Bristol', 'London',  # England
    'Bloemfontein', 'Potchefstroom', 'East London', 'Durban', 'Port Elizabeth', 'Gqeberha', 'Centurion', 'Cape Town', 'Paarl',  # South Africa
    'Kanpur', 'Nagpur', 'Bangalore', 'Bengaluru', 'Ranchi', 'Guwahati', 'Delhi', 'Rajkot', 'Thiruvananthapuram', 'Cuttack', 'Indore',
    'Mumbai', 'Kolkata', 'Lucknow', 'Chennai', 'Visakhapatnam', 'Hyderabad', 'Chandigarh', 'Pune', 'Jaipur', 'Dharamsala',  # India
    'Lahore', 'Karachi', 'Rawalpindi',  # Pakistan
    'Hobart', 'Adelaide', 'Melbourne', 'Sydney', 'Canberra', 'Perth', 'Darwin', 'Cairns',  # Australia
    'Barbados', 'Trinidad', 'Jamaica', 'St Kitts', 'Gros Islet', 'Basseterre', 'Coolidge', 'Bridgetown', "St George's",
    'Tarouba', 'Kingstown', 'St Lucia', 'Antigua', 'St Vincent', 'Providence', 'Guyana'  # West Indies
]

# Streamlit app title
st.title("Cricket Runs Prediction")

# Dropdowns for teams and cities
batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)
city = st.selectbox("City", cities)

# Numeric inputs
current_score = st.number_input("Current Score", min_value=0, max_value=500, value=100)
balls_bowled = st.number_input("Balls Bowled", min_value=0, max_value=300, value=60)
wickets_left = st.number_input("Wickets Left", min_value=0, max_value=10, value=5)
runs_last_3_overs = st.number_input("Runs in Last 3 Overs", min_value=0, max_value=100, value=20)
crr = st.number_input("Current Run Rate", min_value=0.0, max_value=20.0, value=6.0)

# Predict button
if st.button("Predict Runs"):
    X_new = pd.DataFrame([{
        'batting_team': batting_team,
        'bowling_team': bowling_team,
        'city': city,
        'current_score': current_score,
        'balls_bowled': balls_bowled,
        'wickets_left': wickets_left,
        'runs_last_3_overs': runs_last_3_overs,
        'crr': crr
    }])
    
    predicted_runs = pipeline.predict(X_new)[0]
    st.success(f"Predicted Total Runs: {predicted_runs:.2f}")
