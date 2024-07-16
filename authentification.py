import streamlit as st
import streamlit_authenticator as stauth

# Define user credentials in a YAML file (replace with your actual data)
credentials = {'user1': {'name': 'John Doe', 'password': 'hashed_password1'},
              'user2': {'name': 'Jane Doe', 'password': 'hashed_password2'}}

# Configuration for Streamlit Authenticator
cookie_name = "auth_cookie"
cookie_key = "SecretKey"
authentication_required = True
preauthorized = []

# Update `streamlit-authenticator` if necessary (recommended)
# pip install --upgrade streamlit-authenticator

# Create the authenticator object with cookie configuration in credentials
authenticator = stauth.Authenticate(
    credentials={'credentials': credentials},
    cookie_name=cookie_name,
    cookie_key=cookie_key,
    preauthorized=preauthorized
)

# Login form and session state management
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    # Display content only if user is authenticated
    st.write(f'Welcome, {name}!')
    st.sidebar.success("You are logged in as " + username)

    # Your app's main content goes here

    # Logout button
    if st.button("Logout"):
        authenticator.logout('main')
        st.sidebar.warning("You are logged out.")
        st.experimental_rerun()  # Reset app state

elif authentication_required:
    st.warning("Please log in to access this app.")
    st.experimental_rerun()  # Reset app state to login form

# No need for hidden cookie storage as handled by Streamlit Authenticator
