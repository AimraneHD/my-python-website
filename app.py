import streamlit as st
import watermark_remover as wr
import pandas as pd
import time
import random

wr.remove_watermark()

while True:
    st.write(pd.DataFrame({'Column 1': [random.Random(100), random.Random(100)], 'Column 2': [random.Random(100), random.Random(100)]}))
    time.sleep(60*2)
