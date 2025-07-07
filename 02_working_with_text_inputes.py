import streamlit as st

# Title
st.title("Streamlit Text Input Examples")

# Text Input
name = st.text_input("Enter your name:")

if name == "":
    st.warning("⚠️ Bạn cần nhập tên để tiếp tục.")

# Text Area
feedback = st.text_area("Enter your feedback:", "", height=200)

if feedback == "":
    st.warning("⚠️ Bạn cần nhập feedback để tiếp tục.")

# Number Input
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)
if age == 0:
    st.warning("⚠️ Bạn cần nhập tuổi để tiếp tục.")

# Date Input
date = st.date_input("Select a date:")

# Time Input
time = st.time_input("Select a time:", step=300) # 300s = 5p

# Color picker
color = st.color_picker("Pick a color:")

# Display inputs
st.markdown("##### This is my info:")
if name!="" and feedback!="" and age!=0:
    st.write("- Name:", name)
    st.write("- Feedback:", feedback)
    st.write("- Age:", age)
    st.write("- Date:", date)
    st.write("- Time:", time)
    st.write("- Color:", color)
