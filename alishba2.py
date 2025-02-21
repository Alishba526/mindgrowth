import streamlit as st
 


st.set_page_config(page_title="Data sweeper🌟 ", page_icon="🧊", layout="wide")
st.title("Data Sweeper")
# quote
st.header("Data Sweeper is a tool  that helps you to clean your data and make it ready for analysis.")
st.write("Upload your data and get it cleaned in seconds.")

st.header("what your challenge?")
user_input = st.text_input("Enter your challenge here")

# condition
if user_input:
    st.success(f"Your facing {user_input}")

else:
    st.warning("Please enter your challenge")

# reflection
st.header("What do you want to achieve?")
reflection = st.text_area("Enter your reflection here")



if reflection:
    st.success(f"Your reflection has been saved as: {reflection}")
else:
    st.info("Please enter your reflection ✅")

# achievement
st.header("celebrate your achievement🏆")
achievement = st.text_input("Enter your achievement here")

if achievement:
    st.success(f"Your achievement has been saved as: {achievement} ❤️")
else:
    st.info("Please enter your achievement")


# footer
st.write("Data Sweeper is a tool that helps you to clean your data and make it ready for analysis.")
st.write("© 2021 Data Sweeper. All rights reserved.")
st.write("Privacy Policy | Terms of Service | Contact Us")
st.write("Made with ❤️ by Alishba")






