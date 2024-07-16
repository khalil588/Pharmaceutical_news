import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import pymongo
from app3 import *
from Users import *
from top_news import *
from pharmaceutical_news import pharmaceutical_news
from inserting_news import add_pharmacutical_news_to_db, add_top_news_to_db
from sending_email import sending_email
import schedule
import time
import threading
####################################################

# Retrieving data from and sending it to DB

def job(): 
    add_top_news_to_db()
    add_pharmacutical_news_to_db()
    #sending_email
    print("Done!")

# Schedule the job every hour
schedule.every().hour.do(job)

# Function to run the schedule in a separate thread
def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the scheduling thread
schedule_thread = threading.Thread(target=run_schedule)
schedule_thread.start()


#######################################

st.set_page_config(layout="wide")
#st.image('assets/logo.jpg',width=100)
st.markdown("<h1 style='text-align: center; color: #1E90FF;'>Pharmaceutical Companies' News Summarizer</h1>", unsafe_allow_html=True)



st.title(" ")
# Function for Home page content
def home():
    st.title("Home")
    st.write("Welcome to the Home page!")

# Function for About page content
def about():
    st.title("About")
    st.write("This is the About page.")

# Function for Contact page content
def contact():
    st.title("Contact")
    st.write("This is the Contact page.")
        # Set up the form
    st.title("Simple Form Example")

    # Create a form
    with st.form(key='my_form'):
        # Add form elements
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=0, max_value=120)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        hobbies = st.multiselect("Hobbies", ["Reading", "Traveling", "Sports", "Cooking", "Others"])

        # Add a submit button
        submit_button = st.form_submit_button(label='Submit')

    # Handle form submission
    if submit_button:
        st.write("Form Submitted!")
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Gender: {gender}")
        st.write(f"Hobbies: {', '.join(hobbies)}")

# Horizontal menu
selected = option_menu(
    menu_title=None,  # required
    options=["Home", "Users", "Top News","Competition"],  # required
    #icons=["house", "profile", "envelope"],  # optional
    #menu_icon="cast",  # optional
    default_index=0,  # optional
    orientation="horizontal",
)

# Display the selected page
if selected == "Home":
    pharmaceutical_news()
elif selected == "Users":
    user()
elif selected == "Top News":
    top_news()
elif selected == "Competition":
    competition_pharma()


