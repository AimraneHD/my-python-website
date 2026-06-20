import streamlit as st
import watermark_remover as wr
import pandas as pd
import time
import random

wr.remove_watermark()

placeholder = st.empty()

while True:
    new_table = pd.DataFrame({
        'Column 1': [random.randint(100), random.randint(100)],
        'Column 2': [random.randint(100), random.randint(100)]
    })
    
    with placeholder.container():
        st.write(new_table)
    
    time.sleep(60*2)
