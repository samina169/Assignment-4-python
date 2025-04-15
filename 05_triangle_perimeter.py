import streamlit as st

# Title of the app
st.title("Triangle Perimeter Calculator")

# Input fields for the lengths of the triangle sides
side_a = st.number_input("Enter the length of side A:", min_value=0.0)
side_b = st.number_input("Enter the length of side B:", min_value=0.0)
side_c = st.number_input("Enter the length of side C:", min_value=0.0)

# Button to calculate the perimeter
if st.button("Calculate Perimeter"):
    perimeter = side_a + side_b + side_c
    st.write(f"The perimeter of the triangle is: {perimeter:.2f}")
