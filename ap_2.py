import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

# 1 헤더 텍스트를 만듭니다.
st.header('st.write') 

# 2 ** 기울기, :: 이모티콘
st.write('Hello, *World!* :sunglasses:') 

# 3 숫자와 같은 다른 데이터 형식을 표시하는 데에도 사용할 수 있습니다.
st.write(1234)

# 4 DataFrames는 다음과 같이 표시될 수도 있습니다.
df = pd.DataFrame({ 
    'fitst column' : [1,2,3,4],
    'second column' : [10,20,30,40]
})
st.write(df)

# 5 여러 인수를 전달할 수 있습니다.
st.write('Below is a DateFrame:', df, 'Above is a dataframe.')

# 6 변수에 전달하여 플롯도 표시할 수 있습니다.
df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)