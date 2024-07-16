import streamlit as st
from bd_connection import * 
import re
#from streamlit.elements import button
def is_valid_email(email):
    # Basic regex for email validation
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email)
def user():
    st.title("User Information Management")
    
    users_df = get_users()  # Retrieve users from database
    
    st.subheader("Current Users")
    
    # Custom styling for the table
    st.markdown(
        """
        <style>
        .user-table {
            width: 100%;
            border-collapse: collapse;
        }
        .user-table th, .user-table td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
            width: 16.66%;  /* Each column will take up equal width (100% / 6 columns) */
        }
        .user-table th {
            background-color: #f2f2f2;
        }
        .user-table tr:nth-child(even) {
            background-color: #f9f9f9;
        }
        .user-table tr:hover {
            background-color: #f1f1f1;
        }
        .delete-button {
            background-color: #ff4b4b;
            color: white;
            border: none;
            padding: 5px 10px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 14px;
            cursor: pointer;
            border-radius: 4px;
        }
        .delete-button:hover {
            background-color: #d9534f;
        }
        </style>
        """
    , unsafe_allow_html=True)
    
    st.markdown(
        """
        <table class="user-table">
            <thead>
                <tr>
                    <th>Full Name</th>
                    <th>Email</th>
                    <th>Age</th>
                    <th>Position</th>
                    <th>Phone Number</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
        """
    , unsafe_allow_html=True)
    
    # Display users in a table format with delete buttons
    for index, row in users_df.iterrows():
        col1, col2, col3, col4, col5, col6 = st.columns([2, 3, 1, 2, 2, 1])
        with col1:
            st.write(row['Full_name'])
        with col2:
            st.write(row['Email'])
        with col3:
            st.write(row['Age'])
        with col4:
            st.write(row['Position'])
        with col5:
            st.write(row['Phone_Number'])
        with col6:
            if st.button("Delete", key=f"delete_{index}"):
                delete_user(row['Email'])
                st.experimental_rerun()  # Rerun to refresh the UI after deletion
    
    st.markdown(
        """
            </tbody>
        </table>
        """
    , unsafe_allow_html=True)

#############################Form##############################################""

    st.title("User Information Form")
    
    # Input fields
    full_name = st.text_input("Full Name", max_chars=100)
    email = st.text_input("Email",  max_chars=100)
    age = st.number_input("Age", min_value=0, max_value=150)
    position = st.text_input("Position", max_chars=100)
    phone_number = st.text_input("Phone Number", max_chars=20)
    
    # Validate form submission
    if st.button("Submit"):
        if not full_name:
            st.warning("Please enter your full name.")
        elif not email:
            st.warning("Please enter your email address.")
        elif not is_valid_email(email): 
            st.error("Invalid email address")
        elif not age:
            st.warning("Please enter your age.")
        elif not phone_number:
            st.warning("Please enter your phone number.")
        elif not position:
            st.warning("Please enter your position.")
        else:
            st.success("Form submitted successfully!")
            add_user(full_name,email,age,position,phone_number)
            st.experimental_rerun()
            # Process form data here
            # You can save to database, send emails, etc.

