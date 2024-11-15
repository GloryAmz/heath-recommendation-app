import streamlit as st
import pandas as pd
import numpy as np


st.title('Health Recommendation app')

st.write('This is a health prediction app')

with st.expander('Data:'):
  st.write('**Raw Data**')
df = pd.read_csv('update_data.csv')
df
def add_aggregate_metrics(df):
    df['avg_daily_steps'] = df.groupby('user_id')['steps'].transform('mean')
    df['avg_weekly_calories'] = df.groupby('user_id')['calories'].transform(lambda x: x.rolling(7).mean())
    return df

def add_health_ratios(df):
    # Example: Adding BMI or activity-to-rest ratio
    df['activity_to_rest_ratio'] = df['steps'] / df['rest']
    return df



