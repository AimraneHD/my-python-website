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
