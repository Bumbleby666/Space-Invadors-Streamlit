import streamlit as st
from PIL import Image
import json
import requests
from streamlit_lottie import st_lottie

# Einbindung von Emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Space Invadors", page_icon=":alien:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ----Load Assets: https://lottiefiles.com/
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_JjzZIq.json")
lottie_coding1 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_toat7wol.json")



#----Header Selection-----
with st.container():
    st.subheader("Hallo, erste Versuche mit Space Invadors! :alien:")
    st.title(" Wir sind die Gruppe Delhi")



#---- 2 Columns -----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st_lottie(lottie_coding, height=400, key="coding")
    with right_column:
        st_lottie(lottie_coding1, height=600, key="coding1")
 
     
