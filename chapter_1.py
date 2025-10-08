import streamlit as st

st.title("Hello Chai App")
st.subheader("This is a simple Streamlit app integrated with Chai.")
st.text("Welcome to the Chai-Streamlit integration example!")
st.write("Choose your favourite variety of chai")


chai = st.selectbox("Your Favourite Chai: ",[
    "Masal Chai",
    "Adrak Chai",
    "Lemon Chai",
    "Kesar Chai"
])

st.write(f"You selected: {chai}. Excellent Choice")

st.success("Your Chai has been brewed! Enjoy your drink!")