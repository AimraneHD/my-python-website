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
st.write("""$$\n
\\begin{equation}\n
e=-\\frac{d\\phi}{dt}=\\oint(\\vec{E}+\\vec{v}\\times\\vec{B}).\\vec{dl}\n
\\end{equation}\n
$$""")
st.write("i dont want it to put a number next to an equation though")
st.write("one more thing, what if i...")
st.write("""
| full name | Massar code | Ensam code | Current grade |
|-----------|-------------|------------|---------------|
| Aimrane Haddou | B136070002 | M24401 | 2nd year |
""")
st.write("wait hold on..., i can just write everything in one whole string like i would in a markdown file without having to write \"st.write\" over and over again")
st.write("""
Hello, my name is Aimrane Haddou, I am currently a second year student, well..., was a second year student, but not officially a 3rd year one yet, summer just started\n
Here is my totally real ensam code: $M24401$\n
Here is my totally real Massar code as well: $B136070002$\n
and here is everything i mentioned above in a table:\n
| full name | Massar code | Ensam code | Current grade|
|---|---|---|---|
| Aimrane Haddou | B136070002 | M24401 | 2nd year |

i dont know how to escape this table\n
here is also a math block for no reason:\n
$$
\\begin{equation}
e=-\\frac{d\\phi}{dt}=\\oint(\\vec{E}+\\vec{v}\\times\\vec{B}).\\vec{dl}\n
\\end{equation}
$$
""")
st.write({"Name" : "Gemini", "Role": "AI"})
