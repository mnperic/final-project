import streamlit as st
import pandas as pd
#import mymodel as m
#import time
#import numpy as np

st.write("""
# My first app
Hello *world!*
""")

df = pd.read_csv("../Resources/crude_oil_forecasted.csv")
st.line_chart(df)

#window = st.slider("Forecast window")
#st.write(m.run(window=15))