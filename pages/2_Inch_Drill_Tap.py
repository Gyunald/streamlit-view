import streamlit as st

col1, col2 = st.columns([1,1])
col3, col4 = st.columns([1,1])

with col1:
    drill_pi = st.number_input("Drill pi",1.0)
    st.write(round(25.4 * drill_pi,2))

with col2:
    hole = st.number_input("Angle",1)
    st.write(round(360 / hole,3), 'x', hole)
    st.write(round(360 / hole,3) / 2)

with col3:
    with st.form("my_form",clear_on_submit=False):
        tap = st.text_input("Inch Tap",placeholder='ex) 1, 3/8')
        nums = st.number_input("Threads",0)
        rpm = st.number_input("RPM",0)

        conversion = st.form_submit_button("CONVERSION")
            
        if not tap.isdigit():
            if conversion:
                st.write(
                round(int(tap[:tap.index('/')]) / int(tap[tap.index('/')+1:]) * 25.4 , 2),
                round((int(tap[:tap.index('/')]) / int(tap[tap.index('/')+1:]) * 25.4) - (25.4 / nums),2),
                round(25.4 / nums, 2))
                st.write('s',rpm, 'p',round(25.4 / nums,2), 'f',round(rpm *25.4 / nums,2))
        if tap.isdigit():
            if conversion:
                st.write(
                round(int(tap) * 25.4, 2),
                round((int(tap) * 25.4) - (25.4 / nums),2),
                round(25.4 / nums,3))            
                st.write('s',rpm, 'p',round(25.4 / nums,2), 'f',round(rpm *25.4 / nums,2))
with col4:
    with st.form("time",clear_on_submit=False):
        holes = st.number_input('Hole Times',1)
        f = st.number_input('Feed',value=100.0, step=0.1)
        z = st.number_input('Z',value=10.0, step=0.1)
        q = st.number_input('Q',value=0.5, step=0.1)
        r = st.number_input('R',value=0.1,step=0.1)
        t = r * (z//q)
        next = (holes - 1) * 1
        
        time = ((z / (f / 60)) + next) * (holes)
        time2 = ((((z + t) / (f / 60)) + ((z//q) * 0.4)) + next) * holes

        conversion1 = st.form_submit_button("G81")
        conversion2 = st.form_submit_button("G73")

        if conversion1:
            st.write(int(time/60) // 60,'h',int(time/60) % 60,'m',int(time % 60),'s')
        
        if conversion2:
            st.write(int(time2 / 60) // 60,'h',int(time2/60) % 60,'m',int(time2 % 60),'s')