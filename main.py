# HackOverFlow - Team QUINN
import streamlit as st
from datetime import date
import Rpi.GPIO as GPIO


#Raspberry pi gpio numbers
SPICLK=
SPIMISO=
SPICS=
SPIMOSI=
#sensor pin numbers


# st.markdown("<script src='https://kit.fontawesome.com/ad34c27ecf.js' crossorigin='anonymous'></script>")
st.set_page_config(layout="wide" , page_icon="💬" , page_title="Air Quality Checker app")

today = date.today()
st.markdown("<h2 style='text-align: center; color: #ccc; margin-top : -85px; margin-bottom: 20px'>Air Quality Checker</h2>", unsafe_allow_html=True)
