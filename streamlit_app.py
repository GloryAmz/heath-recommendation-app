import streamlit as st
import pandas as pd

st.title('Health Recommendation app')

st.write('This is a health prediction app')

with st.expander('Data:'):
  st.write('**Raw Data**')
df = pd.read_csv('https://github.com/GloryAmz/heath-recommendation-app/blob/master/user_data.csv')
df
st.write('**X**')
X = df.drop('name', axis = 1)
X

st.write('**Y**')
Y = df.name
Y

