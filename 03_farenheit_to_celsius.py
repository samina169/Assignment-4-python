import streamlit as st

# Title of the app
st.title("Fahrenheit to Celsius Converter")

# Input field for the temperature in Fahrenheit
fahrenheit = st.number_input("Enter temperature in Fahrenheit:")

# Button to perform the conversion
if st.button("Convert"):
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    st.write(f"The temperature in Celsius is: {celsius:.2f} °C")
