import streamlit as st

# Title of the app
st.title("Agreement Bot")

# Input fields for agreement details
agreement_title = st.text_input("Agreement Title:")
party_one = st.text_input("Party One:")
party_two = st.text_input("Party Two:")
agreement_terms = st.text_area("Agreement Terms:")

# Button to generate the agreement
if st.button("Generate Agreement"):
    agreement = f"""
    **Agreement Title:** {agreement_title}
    
    **Party One:** {party_one}
    
    **Party Two:** {party_two}
     **Terms:**
    {agreement_terms}
    """
    st.write(agreement)
