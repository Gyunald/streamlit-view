import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def Nums():
    return {}

nums = Nums()

if 'nums' not in st.session_state:
    st.session_state.nums = nums

st.subheader("Please enter a value.")
num = st.number_input("😎",1.0)
st.session_state.nums = nums[num] = num * 25.4

col1, col2, col3 = st.columns([1,1,8])
with col1:
    delete = st.button('Delete')
with col2:
    clear = st.button('Clear')

if delete:
    del nums[num]
if clear :
    nums.clear()

df =pd.DataFrame({'inch' : nums.keys(), 'mm' : nums.values()})
st.table(df)