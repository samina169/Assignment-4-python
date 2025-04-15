import streamlit as st
from datetime import datetime

# Title of the app
st.title("How Old Are They?")

# Input field for the birthdate
birthdate = st.date_input("Select your birthdate:")

# Button to calculate age
if st.button("Calculate Age"):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    st.write(f"You are {age} years old.")
