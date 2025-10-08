# Assignment : Age calculator

import streamlit as st
from datetime import datetime,date
# """
# datetime.datetime

# Represents both date and time.

# Has year, month, day, hour, minute, second, microsecond.


# Represents only the date, no time.

# Has year, month, day only.

# """
st.title("Age Calculator App")
st.subheader("Calculate your age based on your date of birth.")


# today = datetime.now().strftime("%Y/%m/%d") dont do else string - date object will be done 
dob = st.date_input("Enter your Date of Birth")
today = date.today()
age = (today-dob).days//365
days = (today-dob).days
st.success("Your Age is calculated")
st.write(f"Your Age is: {age} and days: {days} days")


