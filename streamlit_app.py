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
from sklearn.cluster import KMeans

def cluster_users(df, num_clusters=3):
    kmeans = KMeans(n_clusters=num_clusters)
    df['fitness_profile'] = kmeans.fit_predict(df[['avg_daily_steps', 'BMI', 'calorie_intake']])
    return df
  def collaborative_filtering_recommendation(user_data):
    # Placeholder function: Implement collaborative filtering if possible
    pass

def rule_based_recommendation(user_row):
    if user_row['fitness_profile'] == 0:
        return "Increase daily steps, try light activities like walking, and reduce calorie intake."
    elif user_row['fitness_profile'] == 1:
        return "Maintain current activity level, add strength training twice a week, keep balanced diet."
    elif user_row['fitness_profile'] == 2:
        return "Focus on recovery with stretching and hydration, increase protein intake for muscle repair."
    else:
        return "Custom recommendation based on goals."

def apply_recommendations(df):
    df['recommendation'] = df.apply(rule_based_recommendation, axis=1)
    return df





