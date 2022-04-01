# HackOverFlow - Team QUINN
import streamlit as st
from datetime import date
import Rpi.GPIO as GPIO
import pandas as pd
import numpy as np
import plotly.express as px
import time

#Raspberry pi gpio numbers
SPICLK=
SPIMISO=
SPICS=
SPIMOSI=
#sensor pin numbers
mq135_dpin=
mq135_apin=


# st.markdown("<script src='https://kit.fontawesome.com/ad34c27ecf.js' crossorigin='anonymous'></script>")
st.set_page_config(layout="wide" , page_icon="💬" , page_title="Air Quality Checker app")
st.markdown("<h2 style='text-align: center; color: #ccc; margin-top : -85px; margin-bottom: 20px'>Air Quality Checker</h2>", unsafe_allow_html=True)

today = date.today()

# Getting Datetime from timestamp
name_col,profile_col = st.columns([5,2])
with name_col:
    user_name = st.write("Hai Kiton,")
with profile_col:
    ("Date:", today)
    st.markdown("<p style='color: #ccc; font-size: 12px; margin-top: -15px'>Name : Kiton</p>", unsafe_allow_html=True)
    st.markdown("<p style='color: #ccc; font-size: 12px; margin-top: -20px'>Age : 30</p>", unsafe_allow_html=True)
st.markdown("<div style='margin-bottom : 50px'></div>", unsafe_allow_html=True)
