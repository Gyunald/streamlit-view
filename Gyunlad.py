import streamlit as st
import random

st.title('Lucky 6')
st.write(*sorted(random.sample(range(1,46),6)))
