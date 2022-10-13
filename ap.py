import streamlit as st

st.write("id", st.secrets["gyunald"])

import os
st.write("hi",os.environ["gyunald"] == st.secrets["gyunald"])
st.write(st.secrets["rbskfem"])
st.header("st.button") 

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
    

