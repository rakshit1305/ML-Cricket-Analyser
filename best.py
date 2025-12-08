import streamlit as st
import pickle
import pandas as pd

# Load trained pipeline (with preprocessing included)
pipeline = pickle.load(open('pipeline_ordinal_nik.pkl', 'rb'))

st.title('Cricket Score Predictor')

# Full list of teams and cities
teams = [
    'Australia', 'India', 'Bangladesh', 'New Zealand', 'South Africa', 
    'England', 'West Indies', 'Afghanistan', 'Pakistan', 'Sri Lanka'
]

cities = [
    # Sri Lanka
    'Colombo', 'Kandy', 'Dambulla', 'Hambantota',
    # New Zealand
    'Napier', 'Mount Maunganui', 'Auckland', 'Wellington', 'Hamilton', 'Christchurch', 'Dunedin', 'Nelson', 'Queenstown',
    # Bangladesh
    'Dhaka', 'Chattogram', 'Sylhet', 'Mirpur',
    # England
    'Southampton', 'Taunton', 'Cardiff', 'Chester-le-Street', 'Birmingham', 'Manchester', 'Nottingham', 'Leeds', 'Bristol', 'London',
    # South Africa
    'Bloemfontein', 'Potchefstroom', 'East London', 'Durban', 'Port Elizabeth', 'Gqeberha', 'Centurion', 'Cape Town', 'Paarl',
    # India
    'Kanpur', 'Nagpur', 'Bangalore', 'Bengaluru', 'Ranchi', 'Guwahati', 'Delhi', 'Rajkot', 'Thiruvananthapuram', 'Cuttack', 'Indore',
    'Mumbai', 'Kolkata', 'Lucknow', 'Chennai', 'Visakhapatnam', 'Hyderabad', 'Chandigarh', 'Pune', 'Jaipur', 'Dharamsala',
    # Pakistan
    'Lahore', 'Karachi', 'Rawalpindi',
    # Australia
    'Hobart', 'Adelaide', 'Melbourne', 'Sydney', 'Canberra', 'Perth', 'Darwin', 'Cairns',
    # West Indies / Caribbean
    'Barbados', 'Trinidad', 'Jamaica', 'St Kitts', 'Gros Islet', 'Basseterre', 'Coolidge', 'Bridgetown', "St George's",
    'Tarouba', 'Kingstown', 'St Lucia', 'Antigua', 'St Vincent', 'Providence', 'Guyana'
]

# User inputs
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select batting team', teams)
with col2:
    bowling_team = st.selectbox('Select bowling team', teams)

city = st.selectbox('Select city', cities)

col3, col4, col5 = st.columns(3)
with col3:
    current_score = st.number_input('Current Score', min_value=0)
with col4:
    balls_bowled = st.number_input('Balls Bowled', min_value=1)
with col5:
    wickets_left = st.number_input('Wickets Left', min_value=0, max_value=10)

runs_last_3_overs = st.number_input('Runs scored in last 3 overs', min_value=0)

if st.button('Predict Score'):
    # Calculate CRR (Current Run Rate)
    crr = (current_score / balls_bowled) * 6

    # Build input DataFrame exactly as used in training
    input_df = pd.DataFrame([{
        'batting_team': batting_team,
        'bowling_team': bowling_team,
        'current_score': current_score,
        'balls_bowled': balls_bowled,
        'wickets_left': wickets_left,
        'runs_last_3_overs': runs_last_3_overs,
        'crr': crr,
        'city': city
    }])

    # Show input
    st.subheader("Input Data")
    st.write(input_df)

    # Predict using pipeline
    result = pipeline.predict(input_df)

    st.header("Predicted Score: " + str(int(result[0])))
