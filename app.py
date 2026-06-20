import streamlit as st
import random

# Customizing the page layout
st.set_page_config(page_title="My Updated App", page_icon="✨")

# --- NEW FEATURE: A Sidebar ---
st.sidebar.header("Control Panel")
st.sidebar.write("This is a sidebar! You can put menus or controls over here.")
st.sidebar.info("Version 2.0 Live")

# Updated Title
st.title("Welcome to My V2 Website! 🚀")
st.write("If you are reading this on the live link, your GitHub update worked perfectly.")

# --- NEW FEATURE: Interactive Data & Graph ---
st.subheader("Interactive Python Graph")
st.write("Drag the slider to change the amount of data displayed.")

# A slider that returns a number
num_points = st.slider("How many data points?", min_value=10, max_value=100, value=50)

# Generate some random numbers using pure standard Python
data = [random.randint(1, 100) for _ in range(num_points)]

# Streamlit magically turns this simple Python list into a line chart!
st.line_chart(data)

# --- THE ORIGINAL FEATURE (Slightly Upgraded) ---
st.divider()
name = st.text_input("Enter your name to verify the update:")

if name:
    st.success(f"Excellent job, {name}! You successfully updated your app via the cloud.")
    
    if st.button("Celebrate V2! 🎉"):
        st.balloons()
