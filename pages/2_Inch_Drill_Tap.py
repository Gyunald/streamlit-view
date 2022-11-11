import streamlit as st

col1, col2 = st.columns([1,1])
col3, col4 = st.columns([1,1])

def output_1():
    return \
            st.write('D',round(drill,2)),\
            st.write('T',tap_pi),\
            st.write('P',round(pitch,3)),\
            st.write('S',int(rpm),'F',feed),\
            st.write('Z',round(-z1,2),round(-z2,2))
def output_2():
    return \
        st.write('D',round(drill,2)),\
        st.write('T',tap_pi),\
        st.write('P',round(pitch,3)),\
        st.write('S',int(rpm),'F',feed),\
        st.write('Z',round(-z1,2))

with col1:
    drill_pi = st.number_input("Diameter",1.0)
    st.write('ø',round(25.4 * drill_pi,2))

with col2:
    hole = st.number_input("Split Angle",1)
    st.write('c',round(360 / hole,3) / 2,'˚')
    st.write('h',round(360 / hole,3), '˚','x', hole)

with col3:
    with st.form("my_form",clear_on_submit=False):
        tap = st.text_input("Inch Tap",placeholder='ex) 1-8, 7/8-9')
        deep = st.text_input("Deep",placeholder='ex) 1.5-2.5')
        rpm = st.text_input("RPM",value=100)
        conversion = st.form_submit_button("CONVERSION")
        
        try:
            if conversion:
                if '/' in tap :
                    numerator = int(tap[:tap.index('/')])
                    denominator = int(tap[tap.index('/')+1 : tap.index('-')])
                    tap_thread = int(tap[tap.index('-')+1:])
                    tap_pi = (numerator / denominator) * 25.4
                    drill = (numerator / denominator) * 25.4 - (25.4 / tap_thread)
                    pitch = 25.4 / tap_thread
                    feed = round(int(rpm)*pitch,3)
                    if '-' in deep :
                        z1 = float(deep[:deep.index('-')]) * 25.4
                        z2 = float(deep[deep.index('-')+1:]) * 25.4
                        output_1()
                    else:
                        z1 = float(deep) * 25.4
                        output_2()
                    
                else:  
                    integer = int(tap[:tap.index('-')])
                    tap_thread = int(tap[tap.index('-')+1:])
                    tap_pi = integer * 25.4
                    drill = (integer * 25.4) - (25.4 / tap_thread)
                    pitch = 25.4 / tap_thread
                    feed = round(int(rpm)*pitch,2)
                    if '-' in deep :
                        z1 = float(deep[:deep.index('-')]) * 25.4
                        z2 = float(deep[deep.index('-')+1:]) * 25.4
                        output_1() 
                    else:
                        z1 = float(deep) * 25.4
                        output_2()
        except ValueError:
            st.warning('Please enter a value.')

with col4:
    with st.form("time",clear_on_submit=False):
        holes = st.number_input('Holes Time',1)
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