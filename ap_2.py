import secrets
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
from datetime import datetime, time
import time

# # 1 헤더 텍스트를 만듭니다.
# st.header('st.write') 

# # 2 ** 기울기, :: 이모티콘
# st.write('Hello, *World!* :sunglasses:') 

# # 3 숫자와 같은 다른 데이터 형식을 표시하는 데에도 사용할 수 있습니다.
# st.write(1234)

# # 4 DataFrames는 다음과 같이 표시될 수도 있습니다.
# df = pd.DataFrame({ 
#     'fitst column' : [1,2,3,4],
#     'second column' : [10,20,30,40]
# })
# st.write(df)

# # 5 여러 인수를 전달할 수 있습니다.
# st.write('Below is a DateFrame:', df, 'Above is a dataframe.')

# # 6 변수에 전달하여 플롯도 표시할 수 있습니다.
# df2 = pd.DataFrame(
#     np.random.randn(200,3),
#     columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(
#     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# st.write(c)

# st.caption('This is a string that explains something above.')

# Slider
# st.header('st.slider')

# st.subheader("Slider")
# age = st.slider('How old are you?',1,100,20,3,) # 내용,최소,최대,기본값,스텝
# st.write("I'm ", age, 'years old')

# st.subheader('Range slider')
# value = st.slider(
#     'Select a range of values',0.0, 100.0, (25.0, 75.0)) # 튜플로 기본값 설정
# st.write('Values: ', value)

# st.subheader('Range time slider')
# appointment = st.slider(
#     "Schedule your appointment:",
#     value=(time(8,30),time(12,00))
# )
# st.write("You're scheduled for: ", appointment[0],appointment[1])

# start_time = st.slider(
#     "When do you start?",
#     value = datetime(2022,1,1,9,30),
#     format="MM/DD/YY - hh:mm"
# )
# st.write("Start time:", start_time)

# st.line_chart

# st.header('Line chart')
# chart_data = pd.DataFrame(
#     np.random.randn(20,3),
#     columns=['a','b','c'],
# )
# st.line_chart(chart_data)

# st.selectbox

# st.header('st.selectbox')
# option = st.selectbox(
#     'What is your favorite color?',
#     ('Blue','Red','Green'),
# )
# st.write('your favorite color is ', option)

# st.header('st.multiselect')
# options = st.multiselect(
#     'What is your favorite colors?',
#     ['Blue','Red','Green','Yellow'],
#     ['Yellow','Red']
# )
# st.write('You selected', options)

# st.checkbox

# st.header('st.checkbox')
# st.write('What would you like to order?')
# icecream = st.checkbox('Icecream')
# coffee = st.checkbox('Coffee')
# cola = st.checkbox("Cola")

# if icecream:
#     st.write("Great! here's some more :icecream:")
 
# if coffee:
#     st.write("Okay, here's some more :coffee:")
    
# if cola:
#     st.write("Here you go")

import streamlit as st

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["db_username"])
st.write("DB password:", st.secrets["db_password"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)
