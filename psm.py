import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker By Areesha Sheikh", page_icon="🔐", layout="centered")
# custom css
st.markdown("""
<style>
    .main {text-align: center; }
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 50%; background-color #2CAF50; color: white; font-size: 18px; }
    .stButton button:hover { background-color: blue; color: black }
</style>
""", unsafe_allow_html=True)

#Page title and description
st.title("🔒 Password strength Generator")
st.write("Enter your password below to check its security level.✅ ")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 
    else:
        feedback.append("❎Password should be **atleast 8 character long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❎Password should include **Both uppercase (A-Z) an lowercase(a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❎Password should include **at least one number (0-9)**.")

    #special charac
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❎Include **at least one special character (!@#$%^&*)**.")

    #display password strength results
    if score == 4:
        st.success("⭕ **Strong password** your password is secure.")
    elif score ==3:
        st.info("➡️**Moderate Password** Consider imoroving security by adding some features.")
    else:
        st.error("➡️**Week Password** Follow the suggestion below to strength it.")

    #feedback
    if feedback:
        with st.expander("➡️**Improve Your Password** "):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter Your Password:", type="password",help="Enter your password is strong")

#button working
if st.button("Check button"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️Please enter a password first!")
