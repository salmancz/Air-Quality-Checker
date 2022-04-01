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
def init():
    GPIO.setwarnings(False)
    GPIO.cleanup()		
    GPIO.setmode(GPIO.BCM)		
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

oxygen_col, carbon_col, monoxide_col = st.columns([3,3,1])
with oxygen_col:
    st.metric(label="Oxygen", value="69ppm", delta="1.2%")
with carbon_col:
    st.metric(label="Carbon-dioxide", value="110ppm", delta="-0.2%")
with monoxide_col:
    st.metric(label="Carbon-monoxide", value="32ppm", delta="-2.1%")
st.markdown("<div style='margin-bottom :30px'></div>", unsafe_allow_html=True)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['Oxygen', 'Carbon-dioxide', 'Carbon-monoxide'])

st.line_chart(chart_data)
level_col, risk_col = st.columns(2)
with level_col:
    st.markdown("<div style='margin-bottom :30px'></div>", unsafe_allow_html=True)
    st.text("Oxygen Level : 12%")
    st.text("Carbon-dioxide Level : 12%")
    st.text("Carbon-monoxide Level : 12%")
    
    st.markdown("<div style='margin-bottom :30px'></div>", unsafe_allow_html=True)
    st.subheader("Heartbeat rate : 56/s-")
   
    
with risk_col:
    st.markdown("<h5 style='color: crimson; margin-top : 30px; margin-left: 40px; margin-bottom: 20px'>Risk Level: ⚠️</h5>", unsafe_allow_html=True)
 
