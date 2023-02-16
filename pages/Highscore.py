import streamlit as st
import json
import requests
from PIL import Image
import pandas as pd
from streamlit_lottie import st_lottie


# load Emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Space Invadors", page_icon=":alien:", layout="wide")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


header = st.container()
dataset = st.container()



with header:
    st.title("Highscore")
    st.subheader("Hier werden Eure Ergebnisse angezeigt!:alien:")
   
    # Highscore Liste als CSV importieren 
    taxi_data = pd.read_csv("E:\Webpage\Webpage\highscore\highscore.csv", delimiter=';', quotechar='"')
    st.write(taxi_data.head(10))


# load Assets: LottieFiles: https://lottiefiles.com/
lottie_coding = load_lottiefile("E:\\Webpage\\Webpage\\lottie\\118361-space-runner.json")
lottie_coding1 =  load_lottiefile("E:\\Webpage\\Webpage\\lottie\\alien_1.json")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(
            lottie_coding,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            #renderer="canvas", # canvas
            height=300,
            width=None,
            key=None,
            )
    with right_column:
        st_lottie(
            lottie_coding1,
            speed=1,
            reverse=False,
            loop=True,
            quality="low", # medium ; high
            #renderer="canvas", # canvas
            height=300,
            width=None,
            key=None,
            )


