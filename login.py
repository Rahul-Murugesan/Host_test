import streamlit as st

# Set the page title and layout
st.set_page_config(page_title="Login Page", layout="centered")

# Initialize a session state to track login status
if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False

# Dummy username and password (for demo purposes)
correct_username = "admin"
correct_password = "password123"

# Create a function to handle login
def login(username, password):
    if username == correct_username and password == correct_password:
        st.session_state['login_status'] = True
        st.success("Logged in successfully!")
    else:
        st.error("Incorrect username or password")

# Login form
if not st.session_state['login_status']:
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        login(username, password)
else:
    st.title("Welcome to the Dashboard!")
    st.write("You are logged in.")
    logout_button = st.button("Logout")

    if logout_button:
        st.session_state['login_status'] = False
        st.experimental_rerun()
