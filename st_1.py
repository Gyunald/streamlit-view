import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def Nums():
    return {}

nums = Nums()

if 'nums' not in st.session_state:
    st.session_state.nums = nums

st.subheader("Please enter a value.")

col1, col2, col3 = st.columns([1,1,1])
with col1:
    num = st.number_input("😎",value=1.0, min_value=0.01)
    st.session_state.nums = nums[num] = num * 25.4
    delete = st.button('Delete')
    clear = st.button('Clear')
    if delete:
        del nums[num]
    if clear :
        nums.clear()
# with col2:
with col2:
    df =pd.DataFrame({'inch' : nums.keys(), 'mm' : nums.values()})
    st.table(df)
    

