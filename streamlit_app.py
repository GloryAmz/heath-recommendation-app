import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd

# Load the dataset
def load_data():
    data = pd.read_csv('update_data.csv')
    return data

data = load_data()

# Title and description
st.title("Health Recommendation App")
st.write("""
This app provides personalized health recommendations based on your activity and dietary metrics. 
Upload your data or input your stats to receive insights.
""")

# Display the dataset
if st.checkbox("Show Dataset"):
    st.write(data)

# User input section
st.header("Enter Your Details")

# Create input fields for user metrics
steps = st.number_input("Steps Walked", min_value=0, value=10000)
intensity = st.slider("Workout Intensity (1-10)", min_value=1, max_value=10, value=5)
duration = st.number_input("Workout Duration (minutes)", min_value=0, value=30)
bmi = st.number_input("Body Mass Index (BMI)", min_value=0.0, value=25.0)
goal = st.selectbox("Your Fitness Goal", options=["Cardio Improvement", "Muscle Gain", "Endurance", "Weight Loss"])

# Recommendations
st.header("Health Recommendations")

if st.button("Get Recommendations"):
    st.write("Based on your input:")
    if goal == "Cardio Improvement":
        st.write("- Aim for 10,000 steps daily.")
        st.write("- Keep workout intensity moderate (5-7).")
    elif goal == "Muscle Gain":
        st.write("- Include strength training in your routine.")
        st.write("- Ensure high protein intake.")
    elif goal == "Endurance":
        st.write("- Increase workout duration gradually.")
        st.write("- Focus on consistent cardio activities.")
    elif goal == "Weight Loss":
        st.write("- Create a calorie deficit through balanced meals and exercise.")
        st.write("- Monitor your BMI regularly.")

# Visualizations
st.header("Data Insights")
if st.checkbox("Show Average Stats"):
    avg_steps = data["steps"].mean()
    avg_bmi = data["bmi"].mean()
    st.write(f"Average Steps: {avg_steps:.2f}")
    st.write(f"Average BMI: {avg_bmi:.2f}")
