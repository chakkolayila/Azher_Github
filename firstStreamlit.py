import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name:")
st.write("Hello,", name)
# Number input
age = st.number_input("Enter your age:")
st.write("Your age is", age)
if st.button("Click Me"):
    st.write("You clicked the button! 🎉")
    # slider(label, min, max)
number = st.slider("Pick a number", 0, 100)
st.write("You picked:", number)
# Dropdown
city = st.selectbox("Choose your city", ["Chennai", "Delhi", "Mumbai"])
st.write("You selected:", city)

# Checkbox
agree = st.checkbox("I agree to the terms")
if agree:
    st.write("Thank you for agreeing!")
    st.success("This is a success message (green).")
st.info("This is an info message (blue).")
st.warning("This is a warning message (yellow).")
st.error("This is an error message (red).")