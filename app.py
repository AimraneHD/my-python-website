import streamlit as st

# Customizing the page layout
st.set_page_config(page_title="My First App", page_icon="🚀")

# Title and introduction
st.title("Welcome to My Python-Only Website!")
st.write("Built entirely in PyCharm, hosted completely for free.")

# Add an interactive text input
name = st.text_input("Enter your name to unlock a greeting:")

# Logic based on user input
if name:
    st.success(f"Hello {name}! This website is executing Python logic in real-time.")

    # Add a fun interactive widget
    celebrate = st.button("Click to Celebrate 🎉")
    if celebrate:
        st.balloons()