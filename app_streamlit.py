import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load the trained ML pipeline
pipeline = joblib.load("cricket_pipeline.pkl")

st.set_page_config(page_title="Cricket Score Predictor", page_icon="🏏")
st.title("🏏 Cricket Score Predictor")
# Cricket Logo (place any image URL or file path)


"""
st.markdown(page_bg, unsafe_allow_html=True)

st.markdown('<p class="title-text">Cricket Score Prediction App</p>', unsafe_allow_html=True)

st.markdown("Predict the final score of an innings based on current match situation.")

# Teams and cities
teams = ["Sri Lanka", "India", "Pakistan", "Australia"]
cities = ["Lahore", "Dubai", "Mumbai", "Karachi"]

# ====== Interactive Inputs ======
batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)
current_score = st.slider("Current Score", 0, 400, 100, help="Score at current moment")
balls_bowled = st.slider("Balls Bowled", 0, 120, 60, help="Total balls bowled so far")
wickets_left = st.slider("Wickets Left", 0, 10, 5, help="Wickets remaining")
runs_last_3_overs = st.slider("Runs in Last 3 Overs", 0, 60, 20)
crr = st.number_input("Current Run Rate (CRR)", min_value=0.0, value=6.5, step=0.01)
city = st.selectbox("City", cities)

# ====== Predict Button ======
if st.button("Predict Final Score"):
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
    
    predicted_runs = int(round(pipeline.predict(df)[0]))
    
    # ====== Display Result with Color ======
    if predicted_runs > 200:
        st.success(f"🏏 Predicted Final Runs: {predicted_runs}")
    else:
        st.warning(f"🏏 Predicted Final Runs: {predicted_runs}")
    
    # ====== Projected Score Line Chart ======
    projected_scores = [current_score + i*(predicted_runs-current_score)//5 for i in range(6)]
    plt.figure(figsize=(8,4))
    plt.plot(range(len(projected_scores)), projected_scores, marker='o', color='orange')
    plt.title("Projected Score Progression")
    plt.xlabel("Over Segments")
    plt.ylabel("Runs")
    plt.grid(True)
    st.pyplot(plt)
    
    # ====== Bar Chart: Current vs Predicted ======
    st.bar_chart({"Current Score": [current_score], "Predicted Final Score": [predicted_runs]})
