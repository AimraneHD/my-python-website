import streamlit as st
from streamlit.components.v1 import html

st.write("test")
# --- HIDE NATIVE STREAMLIT BRANDING (Footer, Menu, Header) ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- DESTROY THE STREAMLIT.IO CLOUD WATERMARK ---
html('''
<script>
window.top.document.querySelectorAll(`[href*="streamlit.io"]`).forEach(e => e.setAttribute("style", "display: none;"));
</script>
''', width=0, height=0)
