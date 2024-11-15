import streamlit as st
import pandas as pd

st.title('Health Recommendation app')

st.write('This is a health prediction app')

with st.expander('Data:'):
  st.write('**Raw Data**')
df = pd.read_csv('https://github.com/GloryAmz/heath-recommendation-app/blob/master/user_data.csv')
df
st.write('**X**')
X_raw = df.drop('names', axis = 1)
X_raw

st.write('**Y**')
Y_raw = df.names
Y_raw

