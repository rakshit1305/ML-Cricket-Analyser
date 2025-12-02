import streamlit as st
from PIL import Image

# -----------------------------
# CUSTOM CRICKET THEME STYLING
# -----------------------------
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://wallpapers.com/images/hd/cricket-stadium-4k-abstract-io9w4r2l2qslm4ke.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

.custom-box {
    background: rgba(255, 255, 255, 0.85);
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
}

.title-text {
    font-size: 40px;
    font-weight: 700;
    text-align: center;
    color: white;
    text-shadow: 3px 3px 6px black;
}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)
# Cricket Logo (place any image URL or file path)
st.image("https://1000logos.net/wp-content/uploads/2022/09/Cricket-League-Logo.png", width=140)

st.markdown('<p class="title-text">Cricket Score Prediction App</p>', unsafe_allow_html=True)
with st.container():
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)

    batting_team = st.selectbox("Batting Team", team_list)
    bowling_team = st.selectbox("Bowling Team", team_list)
    city = st.selectbox("City", city_list)

    current_score = st.number_input("Current Score")
    balls_bowled = st.number_input("Balls Bowled")
    wickets_left = st.number_input("Wickets Left")
    runs_last_3 = st.number_input("Runs in Last 3 Overs")
    crr = st.number_input("Current Run Rate")

    if st.button("Predict Final Score"):
        input_df = pd.DataFrame([{
            "batting_team": batting_team,
            "bowling_team": bowling_team,
            "city": city,
            "current_score": current_score,
            "balls_bowled": balls_bowled,
            "wickets_left": wickets_left,
            "runs_last_3_overs": runs_last_3,
            "crr": crr
        }])

        result = model.predict(input_df)[0]
        st.success(f"Predicted Final Score: {int(result)}")

    st.markdown('</div>', unsafe_allow_html=True)

