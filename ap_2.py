import random
import streamlit as st
import pandas as pd

# text

st.title("IMI CCI") # 웹 대시보드
st.header("IMI CCI") # 제목같은 큰 글씨
st.subheader("IMI CCI") # 제목보다는 작은 글씨
st.text("IMI CCi") # 작은 글씨

st.success("Success는 녹색") # 녹색 영역표시
st.warning("Warning은 노란색") # 노란색 영역표시
st.info("Info는 파란색") # 파란색 영역표시
st.error("Error는 빨간색") # 빨간 영역표시

# st.help(sum) # 함수 사용법 ex) sum 사용법

# dataframe

df = pd.read_csv("ec.csv",encoding="cp949")
st.dataframe(df)

a = df['승용'].unique() # unique() : 고유값
st.text("승용은" + str(a) + "대 이다")

st.write('head',df.head()) # head() 앞에서 5개
st.write('tail',df.tail()) # tail() 뒤에서 5개


# 버튼 만들기

st.title("Make Button")
if st.button("승용"):
    st.write("Bye")
    st.dataframe(df['승용'].unique())
else :
    st.write("Hi")

st.title("Make Button")
if st.button("승합"):    
    st.dataframe(df['승합'].unique())
else :
    st.write("Hi")

# 라디오(radio) 버튼 만들기
# 클릭했을때, 나타나는 문자열을 리턴해줌

status = st.radio("choice", pd.Series(["a","b","c"]))
st.header(status)

a = st.radio("정렬방식", pd.Series(["오름차순","내림차순"]))
# a = st.sidebar.radio("정렬방식", ("오름차순","내림차순"))
# a = st.radio("정렬방식", ("오름차순","내림차순"))
b = ("오름차순","내림차순")
if a == b[0]:
# if a == "오름차순" :
    st.dataframe(df.sort_values("승용"))
else :
    st.dataframe(df.sort_values("승용",ascending=False))

# 체크박스 (체크하면 True)

if st.checkbox("a"):
    st.write("A")
    st.dataframe(df.head())
else:
    st.text("B")

# 셀렉트박스 (여러개 중에서 1개만 고르기)
st.title('IMI CCI')
option = st.selectbox(
    '당신의 직책을 선택해주세요.',
    pd.Series(['CEO', 'AI Engineer', 'Intern', 'Product Manager']))
# option = st.sidebar.selectbox(
#     '당신의 직책을 선택해주세요.',
#     pd.Series(['CEO', 'AI Engineer', 'Intern', 'Product Manager']))
f'You selected: {option}'