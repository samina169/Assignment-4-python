import streamlit as st

# Title of the app
st.title("Square a Number")

# Input field for the number
number = st.number_input("Enter a number:", min_value=0.0)

# Button to calculate the square
if st.button("Calculate Square"):
    square = number ** 2
    st.write(f"The square of {number} is: {square:.2f}")
