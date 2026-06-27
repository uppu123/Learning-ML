import streamlit as st
import pandas as pd
import numpy as np


st.title("My First Streamlit App")

# display a simple text
st.write("Hello, This is my First Streamlit App")

df = pd.DataFrame({
    'first column' : [1, 2], 
    'second column' : [10, 20]
})

st.write("DataFrame")
st.write(df)

# display a line chart

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns= ['a', 'b', 'c']
)

st.line_chart(chart_data)


# display some widgets

name = st.text_input("Enter Your Name")
if name:
    st.write(f"Hello {name}")


age = st.slider("Enter your Age", 0, 100, 25)


# selectbox
options = ['C++', 'Python', 'Java', 'AC']
choice = st.selectbox("Please Choose", options)
st.write(f"You have Selected: {choice}")


data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [22, 25, 23, 24],
    "Marks": [85, 90, 78, 88]
}



df = pd.DataFrame(data)
st.write(df)


upload_file = st.file_uploader("Upload a CSV file", type = "csv")
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df) 