import streamlit as st
import watermark_remover as wr
import pandas as pd
import time
import random

# Clear the watermarks
wr.remove_watermark()

st.title("Live Data Feed 📡")
st.write("This table updates every two minutes.")

# 1. Create an empty placeholder box on the website
placeholder = st.empty()

# 2. Start your infinite loop
while True:
    # Create the new table with actual random integers
    new_table = pd.DataFrame({
        'Column 1': [random.randint(1, 100), random.randint(1, 100)], 
        'Column 2': [random.randint(1, 100), random.randint(1, 100)]
    })
    
    # Overwrite the placeholder box with the new table
    with placeholder.container():
        st.write(new_table)
        
    # Pause the loop for 2 minutes (120 seconds) before running again
    time.sleep(120)
