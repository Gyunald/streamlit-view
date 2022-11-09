import streamlit as st
import pandas as pd

@st.cache(allow_output_mutation=True)
def Nums():
    return {}

nums = Nums()

if 'nums' not in st.session_state:
    st.session_state.nums = nums

st.subheader("Please enter a value.")

col1, col2, col3 = st.columns([0.9,1,.5])

with col1:
    num = st.number_input("😎",value=1.0,format="%f ",) # f뒤에 공백!
    delete = st.button('DELETE')
    clear = st.button('CLEAR')
    st.info("""
    TOLERANCES ⚡\n
    .0  ± 2.54\n
    .00  ± 0.762\n
    .000  ± 0.254
    """)
    nums[num] = num * 25.4

if delete:
    del nums[num]
if clear :
    nums.clear()

with col2:
    df =pd.DataFrame({'inch' : nums.keys(), 'mm' : nums.values()})
    hide_table_row_index = """
        <style>
        thead tr th:first-child {display:none}
        tbody th {display:none}
        </style>
        """
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
    st.table(df.style.format("{:.3f}"))