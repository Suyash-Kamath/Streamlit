# Widgets : 

"""
Widgets = interactive components that let users provide input or interact with your Streamlit app.

Just like in a website you have buttons, sliders, or dropdowns — Streamlit gives you these same tools, but directly in Python code.

"""

import streamlit as st

st.title("Interactive Widgets in Streamlit")

if st.button("Make Chai"):
    st.success("Your Chai is being brewed")


add_masala=st.checkbox("Add Masala")

if add_masala:
    st.write("Masala added to your Chai")

tea_type=st.radio("Pick your chai base: ",
                  [
                      "Milk",
                      "Water",
                      "Almond Milk"
                  ])

st.write(f"Selected base: {tea_type}")

flavours = st.selectbox("Choose Flavour: ",
[
    "Adrak",
    "Kesar",
    "Tulsi"
])

st.write(f"You selected: {flavours}")

sugar=st.slider("Sugar Level (Spoon)", 0,5,2)
st.write(f" Selected  Sugar level : {sugar}")

cups=st.number_input("How many cups of Chai would you like?",min_value=1,max_value=10,step=1)

st.write(f"Selected Sugar Levels (Cups) {cups}")

name = st.text_input("Enter your name: ")

if name:
    st.write(f"Hello, {name}! Your Chai will be ready soon.")

dob=st.date_input("Select your Date of Birth")
st.write(f"Your Date of Birth is: {dob}")