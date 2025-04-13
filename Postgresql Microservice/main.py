import streamlit as st   #pip install streamlit
import psycopg2          #pip install psycopg2-bina

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",    # Use 'localhost' if running locally
    port=5432,           # Default PostgreSQL port
    database="dummy",   # Database name
    user="admin",        # Database username
    password="adminpassword"  # Database password
)

cursor = conn.cursor()

# Streamlit app title
st.title('Hello World')

# Input field for name
name = st.text_input('Your name', 'Type here')

# Button to save data
if st.button("Save"):
    if name.strip():  # Ensure name is not empty
        cursor.execute("INSERT INTO test (name) VALUES (%s)", (name,))
        conn.commit()
        st.success("Name saved to the database!")
    else:
        st.error("Name cannot be empty!")

# Display user input
st.write('You entered:', name)

st.write('Click the **Save** button to save your name to the database')

