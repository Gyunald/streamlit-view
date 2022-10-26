import streamlit as st

st.title('Session State Basics')
'st.session_state object:', st.session_state

if 'a_counter' not in st.session_state:
    st.session_state.a_counter = 0

if 'boolean' not in st.session_state:
    st.session_state.boolean = False
st.write(st.session_state)

st.write('a_counter is:', st.session_state.a_counter)
st.write('boolean is:', st.session_state.boolean)

for the_key in st.session_state.keys():
    st.write(the_key)
    
for the_values in st.session_state.values():
    st.write(the_values)
    
for item in st.session_state.items():
    item

button = st.button('Update State')
'before pressing button', st.session_state

if button:
    st.session_state.a_counter += 1
    st.session_state.boolean = not st.session_state.boolean
    'after pessing button', st.session_state
    
for key in st.session_state.keys():
    del st.session_state[key]
    
st.session_state

number = st.slider('A number,',1,10,key='slider')
st.write(st.session_state)

col1, buff, col2 = st.columns([1,0.5,3])
option_names = ['a','b','c']
next = st.button('Next option')

if next:
    if st.session_state.radio_option == 'a':
        st.session_state.radio_option = 'b'
    elif st.session_state.radio_option == 'b':
        st.session_state.radio_option = 'c'
    else:
        st.session_state.radio_option = 'a'

option = col1.radio('Pick an option', option_names, key='radio_option')
st.session_state

if option == 'a':
    col2.write('You picked "a" :smile:')
elif option == 'b':
    col2.write('You picked "b" :heart:')
else:
    col2.write('You picked "c" :rocket:')

def mm_to_inch():
    st.session_state.inch = st.session_state.mm*25.4
    
def inch_to_mm():
    st.session_state.mm = st.session_state.inch/25.4

col1, buff, col2 = st.columns([2,1,2])
with col1:
    a = st.number_input('mm :', key='mm', on_change=mm_to_inch)
with col2:
    b = st.number_input('inch :', key='inch', on_change=inch_to_mm)