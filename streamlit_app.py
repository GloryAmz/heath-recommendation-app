import streamlit as st
import pandas as pd
import numpy as np


st.title('Health Recommendation app')

st.write('This is a health prediction app')

with st.expander('Data:'):
  st.write('**Raw Data**')
df = pd.read_csv('update_data.csv')
df



