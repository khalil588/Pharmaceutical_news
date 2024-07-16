import streamlit as st
import pandas as pd
from bd_connection import get_pharmaceutical_companies,update_pharmaceutical_companies

# Define the update function
def update_function(company_name, selected_option,symbol):
    # Your update logic here
    update_pharmaceutical_companies(symbol,int(selected_option))
    #st.write(f"Updating {company_name} to {'Yes' if selected_option == 1 else 'No'}")

def competition_pharma():
    # Create a DataFrame
    df = get_pharmaceutical_companies()
    df = df[['Ranking' ,'Company Name', 'Symbol', 'Market Cap', 'country','search_news']]
    # Define options for the radio buttons
    options = ['Yes', 'No']

    # Create a dictionary to store the updated 'search_news' column values
    updated_selected = df['search_news'].copy()

    # CSS for styling
    st.markdown(
        """
        <style>
        .header {
            font-weight: bold;
            background-color: #f0f2f6;
            padding: 10px;
        }
        .row {
            padding: 10px;
            border-bottom: 1px solid #f0f2f6;
        }
        .cell {
            padding: 5px;
        }
        .radio-buttons {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the DataFrame with radio buttons
    st.markdown('<div class="header">Pharma Competition</div>', unsafe_allow_html=True)

    # Create header
    header_cols = st.columns(len(df.columns))
    for i, col in enumerate(header_cols[:-2]):
        col.markdown(f'<div class="header">{df.columns[i]}</div>', unsafe_allow_html=True)
    header_cols[-1].markdown('<div class="header">Options</div>', unsafe_allow_html=True)

    # Display rows
    for index, row in df.iterrows():
        row_cols = st.columns(len(df.columns) )
        for i, col in enumerate(row_cols[:-2]):
            col.markdown(f'<div class="cell">{row[i]}</div>', unsafe_allow_html=True)
        with row_cols[-1]:
            selected_option = st.radio(
                "",
                options,
                index=0 if row['search_news'] == 1 else 1,
                key=f"radio_{row['Company Name']}",
                horizontal=True
            )
            # Update the selected value based on radio button
            updated_selected[index] = 1 if selected_option == 'Yes' else 0
            # Call the update function
            update_function(row['Company Name'], updated_selected[index],row['Symbol'])

    # Update the DataFrame
    df['search_news'] = updated_selected
"""    # Display the updated DataFrame
    st.markdown('<div class="header">Updated DataFrame:</div>', unsafe_allow_html=True)
    st.dataframe(df.style.set_properties(**{'text-align': 'center'}).set_table_styles({
        'Name': [{'selector': 'td', 'props': [('text-align', 'center')]}],
        'Age': [{'selector': 'td', 'props': [('text-align', 'center')]}],
        'search_news': [{'selector': 'td', 'props': [('text-align', 'center')]}]
    }))
"""