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
