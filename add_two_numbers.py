import streamlit as st

# Title of the app
st.title("Add Two Numbers")

# Input fields for the two numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# Button to perform the addition
if st.button("Add"):
    result = num1 + num2
    st.write(f"The result is: {result}")
