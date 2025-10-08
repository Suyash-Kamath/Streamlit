import streamlit as st


st.title("Programming Language Selector")
st.subheader("Choose your favorite programming language from the list below.")
st.text("This app helps you select a programming language you like.")
st.write("Select your favorite programming language:")

language = st.selectbox("Your Favourite Programming Language: ", [
    "Python",
    "JavaScript",
    "Java",
    "C++",
    "Ruby",
    "Go",
    "Swift",
    "Kotlin"
])

st.write("You selected: ", language)
st.success("Great choice! Happy coding!")