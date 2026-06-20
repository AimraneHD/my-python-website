import streamlit as st
import pandas as pd

st.write("Hello world")
st.write("## This is a heading")
st.write("### wonder what happens here")
st.write("#### this is interesting")
st.write("##### is this where it stops?")
st.write("###### lets see")

st.write("alr lets see what happens")
hashtags = ""
for i in range(10):
  hashtags += "#"
  st.write(f"{hashtags} alr lets see what happens: {i + 1} headings")

st.write("so 7's the limit, interesting")

st.write(pd.DataFrame({'A': [1, 2], 'B': [3, 4]}))
st.write("hmm")

st.write("i noticed this text format almost looks like markdown, i wonder if i can...")
st.write("""$\\begin{equation}
  e=-\\frac{d\\phi}{dt}=\\oint(\\vec{E}+\\vec{v}\\times\\vec{B}).\\vec{dl}$
\\end{equation}""")
