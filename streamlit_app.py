import streamlit as st
import pandas as pd

st.title('Health Recommendation app')

st.write('This is a health prediction app')

df = pd.read_csv('user_data.csv')
df

