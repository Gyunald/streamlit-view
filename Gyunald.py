import streamlit as st
import random

st.secrets.username
st.secrets.password

st.title('Lucky 6')
st.write(*sorted(random.sample(range(1,46),6)))

st.write(st.secrets.username)