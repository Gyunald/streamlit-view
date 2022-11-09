import streamlit as st

col1, col2 = st.columns([1,1])
col3, col4 = st.columns([1,1])

with col1:
    drill_pi = st.number_input("Drill Pi",1.0)
    st.write(round(25.4 * drill_pi,2))

with col2:
    hole = st.number_input("Holes Angle",1)
    st.write(round(360 / hole,3), 'x', hole)
    st.write(round(360 / hole,3) / 2)

with col3:
    with st.form("my_form",clear_on_submit=False):
        tap = st.text_input("Inch Tap",placeholder='ex) 1-8, 7/8-9')
        rpm = st.text_input("RPM",value=100)
        conversion = st.form_submit_button("CONVERSION")
        
        if conversion:
            if tap and rpm != "" and '-' in tap:
                if '/' not in tap:
                    denominator = int(tap[:tap.index('-')])
                    tap_thread = int(tap[tap.index('-')+1:])
                    drill = denominator * 25.4
                    tap = (denominator * 25.4) - (25.4 / tap_thread)
                    pitch = 25.4 / tap_thread
                    feed = round(int(rpm)*pitch,2)

                    st.write(round(drill,3))
                    st.write(round(tap,2))
                    st.write(round(pitch,3))
                    st.write('s',int(rpm),'f',feed)

                else:
                    numerator = int(tap[:tap.index('/')])
                    denominator = int(tap[tap.index('/')+1 : tap.index('-')])
                    tap_thread = int(tap[tap.index('-')+1:])
                    drill = (numerator / denominator) * 25.4
                    tap = (numerator / denominator) * 25.4 - (25.4 / tap_thread)
                    pitch = 25.4 / tap_thread
                    feed = round(int(rpm)*pitch,2)

                    st.write(round(drill,2))
                    st.write(round(tap,2))
                    st.write(round(pitch,3))
                    st.write('s',int(rpm),'f',feed)

            else:
                st.warning('나사산을 입력하세요. ex) 1-8')

with col4:
    with st.form("time",clear_on_submit=False):
        holes = st.number_input('Holes',1)
        f = st.number_input('Feed',value=100, step=10)
        z = st.number_input('Z',value=10.0, step=0.1)
        q = st.number_input('Q',value=0.5, step=0.1)
        r = st.number_input('R',value=0.1,step=0.1)
        t = r * (z//q)
        move_time = 1
        time = (((z / (f / 60))) * (holes * move_time)) 
        time2 = (((z + t) / (f / 60))  * (holes * (move_time))) 

        conversion1 = st.form_submit_button("G81")
        conversion2 = st.form_submit_button("G73")

        if conversion1:
            st.write(int(time/60) // 60,'h',int(time/60) % 60,'m',int(time % 60),'s')
        
        if conversion2:
            st.write(int(time2 / 60) // 60,'h',int(time2/60) % 60,'m',int(time2 % 60),'s')