import streamlit as st
from streamlit.components.v1 import html

# --- 1. HIDE THE NATIVE STREAMLIT BRANDING ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- 2. NUKE THE "CREATED BY" CLOUD VIEWER BADGE ---
html('''
<script>
    // Reach outside the iframe into the main browser window
    const parentElements = window.parent.document.querySelectorAll('[class*="viewerBadge"]');
    
    // Forcefully hide any container associated with the viewer badge
    parentElements.forEach(function(element) {
        element.style.display = 'none';
    });
</script>
''', width=0, height=0)

# --- Your app code starts here ---
st.title("My 100% Custom Website")
st.write("Look closely... there are no watermarks left.")

# Your normal code continues down here...
st.write("Look mom, no watermarks!")
"""
Hello world\n
My name is Aimrane Haddou, I'm a 2nd year student, and will be a 3rd year one in a few months\n
Let's see what happens\n
$$
\\boxed{\\text{Here's a random maxwell equation} \\implies \\boxed{ \\vec{rot}(\\vec{E})=-\\frac{ \\partial\\vec{B} }{ \\partial t }}}\n
$$
fixed it, kind of\n

$$ Experiment\\ number\\ two\\ \\text{(i love latex's italic computer modern font instead of the normal one)} $$

"""
