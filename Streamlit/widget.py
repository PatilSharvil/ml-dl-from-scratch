import streamlit as st
import pandas as pd 

st.title('Streamlit Text input')

name = st.text_input("Enter your name : ")

age = st.slider("Select your age : ", 0, 100, 25)

st.write(f'your age is {age}')

options = ['Python', 'Java', 'C++', 'C']
choice = st.selectbox('Choose your favorite language : ', options)
st.write(f'your fav language is {choice}')


if name :  
    st.write(f'Hello {name}')
    
upload_file = st.file_uploader('Choose a csv file: ', type='csv')

if upload_file is not None: 
    df = pd.read_csv(upload_file)
    st.write(df)