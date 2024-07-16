import streamlit as st
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Choice': ['No', 'No', 'No']  # Initial choice ('Yes' or 'No')
}
df = pd.DataFrame(data)
st.set_page_config(layout="wide")

# Custom CSS styling
# Custom CSS styling
st.markdown(
    """
    <style>
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        margin: 10px 0;
        font-size: 0.9em;
        font-family: Arial, sans-serif;
    }
    .styled-table th, .styled-table td {
        padding: 10px;
        text-align: center;
        border: 1px solid #ddd;
    }
    .styled-table th {
        background-color: #f2f2f2;
        color: #333;
    }
    .radio-container {
        display: row;
        justify-content: center;
    }
    /* Adjust the radio button alignment */
    div[data-testid="stRadio"] > div {
        flex-direction: row;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Function to update the DataFrame based on button clicks
def update_dataframe():
    for index, row in df.iterrows():
        if radio_options[index] == 'Yes':
            df.at[index, 'Choice'] = 'Yes'
        elif radio_options[index] == 'No':
            df.at[index, 'Choice'] = 'No'

# Initialize radio options dictionary with default choices
radio_options = {index: df.at[index, 'Choice'] for index in df.index}

# Title
st.title('Styled DataFrame with Yes/No Buttons')

# Display the DataFrame with buttons using the styled table
st.markdown('<h3>DataFrame with Yes/No Buttons</h3>', unsafe_allow_html=True)
st.markdown('<table class="styled-table">', unsafe_allow_html=True)

# Display headers in styled table
st.markdown('<thead><tr><th>Name</th><th>Age</th><th>City</th><th>Choice</th></tr></thead>', unsafe_allow_html=True)
st.markdown('<tbody>', unsafe_allow_html=True)

# Display data rows with buttons in styled table
for index, row in df.iterrows():
    st.markdown('<tr>', unsafe_allow_html=True)
    st.markdown(f'<td>{row["Name"]}</td><td>{row["Age"]}</td><td>{row["City"]}</td>', unsafe_allow_html=True)
    st.markdown('<td class="styled-radio">', unsafe_allow_html=True)
    # Set initial selection based on current value in the DataFrame
    initial_selection = 1 if df.at[index, 'Choice'] == 'Yes' else 0
    st.markdown('<div class="radio-container">', unsafe_allow_html=True)
    radio_options[index] = st.radio('', ['No', 'Yes'], index=initial_selection, key=index)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</td>', unsafe_allow_html=True)
    st.markdown('</tr>', unsafe_allow_html=True)

st.markdown('</tbody></table>', unsafe_allow_html=True)

# Update the DataFrame based on radio button selections
update_dataframe()

# Display the updated DataFrame
st.write('Updated DataFrame')
st.dataframe(df)



# Using CSS to display radio buttons horizontally


