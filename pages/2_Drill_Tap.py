import streamlit as st

col1, col2 = st.columns([1,1])
col3, col4 = st.columns([1,1])

with col1:
    drill_pi = st.number_input("DRILL PI",1.0)
    st.write(round(25.4 * drill_pi,2))

with col2:
    hole = st.number_input("HOLES",1)
    st.write(round(360 / hole,3), 'x', hole)
    st.write(round(360 / hole,3) / 2)

with col3:
    with st.form("my_form",clear_on_submit=False):
        tap = st.text_input("TAP",placeholder='ex) 1, 3/8')
        nums = st.number_input("THREADS",0)
        conversion = st.form_submit_button("CONVERSION")
            
        if not tap.isdigit():
            if conversion:
                st.write(
                round(int(tap[:tap.index('/')]) / int(tap[tap.index('/')+1:]) * 25.4 , 3),
                round((int(tap[:tap.index('/')]) / int(tap[tap.index('/')+1:]) * 25.4) - (25.4 / nums),2),
                round(25.4 / nums, 3))
                    
        if tap.isdigit():
            if conversion:
                st.write(
                round(int(tap) * 25.4, 2),
                round((int(tap) * 25.4) - (25.4 / nums),2),
                round(25.4 / nums,3),
                )