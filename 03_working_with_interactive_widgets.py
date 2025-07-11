import streamlit as st

# Title
st.title("Streamlit Interactive Widget Examples")

# Button
button = st.button("Click me!")
if button:
    st.write("Button clicked!")

# Check box
checkbox_state = st.checkbox("Check me to enable something")
if checkbox_state:
    st.write("Checkbox is checked!")

# Radio button
radio_selection = st.radio("Choose an option:", ["NLP", "CV", "DL", "ML"])
st.write("You selected:", radio_selection)

# Select box
selectbox_selection = st.selectbox("Choose an item:", ["NLP", "CV", "DL", "ML"])
st.write("You selected:", selectbox_selection)

# Multiselect 
multiselect_selection = st.multiselect("Choose multiple items:", ["NLP", "CV", "DL", "ML"])
st.write("You selected:", multiselect_selection)

# Slider
slider_value = st.slider("Select a value:", min_value=0, max_value=10, value=5, step=1)
st.write("Slider value:", slider_value)

# Select slider
select_slider_value = st.select_slider("Select a value:", options=range(11))

st.write("Selected slider value:", select_slider_value)

select_slider_value = st.select_slider("Select a value:", options=[0, "NLP", "CV", "DL", "ML"])

st.write("Selected slider value:", select_slider_value)