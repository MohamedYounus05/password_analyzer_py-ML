import streamlit as st
import pickle
import os

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))

st.set_page_config(page_title="Password Strength Analyzer", page_icon="🔐")

st.title("🔐 Password Strength Analyzer")
st.markdown("### Made by - Mohamed Younus")

password = st.text_input("Enter your password", type="password")

if password:
    password_vector = vectorizer.transform([password])
    prediction = model.predict(password_vector)[0]

    if prediction == 0:
        st.error("Weak Password 🔴")
    elif prediction == 1:
        st.warning("Medium Password 🟡")
    else:
        st.success("Strong Password 🟢")