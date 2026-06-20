import streamlit as st
import watermark_remover as wr
import pandas as pd
import time
import random

# Clear the watermarks
wr.remove_watermark()

st.title("Strict 2-Minute Data Feed ⏱️")

# --- THE MAGIC MEMORY FUNCTION ---
# ttl=120 means "Time To Live is 120 seconds". 
# It locks the generated data for exactly two real-world minutes.
@st.cache_data(ttl=120)
def get_random_data():
    return pd.DataFrame({
        'Column 1': [random.randint(1, 100), random.randint(1, 100)], 
        'Column 2': [random.randint(1, 100), random.randint(1, 100)]
    })

# Create an empty placeholder box on the website
placeholder = st.empty()

# Start your infinite loop
while True:
    # Fetch the data from our cached function
    new_table = get_random_data()
    
    # Overwrite the placeholder box with the table
    with placeholder.container():
        st.write("This table is locked. It will only change every 2 real minutes!")
        st.write(new_table)
        
    # We only sleep for 1 second now!
    # The loop runs constantly, but the data it pulls from get_random_data() 
    # will remain identical until the 120-second cache timer expires.
    time.sleep(1)
