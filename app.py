import streamlit as st
import watermark_remover as wr
import pandas as pd
import time
import random

wr.remove_watermark()

while True:
    st.write(pd.DataFrame({'Column 1': [random.choice(range(100)), random.choice(range(100))], 'Column 2': [random.choice(range(100)), random.choice(range(100))]}))
    time.sleep(60*2)
