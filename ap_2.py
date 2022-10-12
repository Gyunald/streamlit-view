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

# df = pd.read_csv("ec.csv",encoding="cp949")
df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40],
  'third cloumn' : ["a","b","c","d"]
})

st.dataframe(df)

a = df['second column'].unique() # unique() : 고유값
st.text("second column은" + str(a) + "대 이다")

st.write('head',df.head()) # head() 앞에서 5개
st.write('tail',df.tail()) # tail() 뒤에서 5개


# 버튼 만들기

st.title("Make Button")
if st.button("click me!"):
    st.subheader('second cloumn.unique')
    st.dataframe(df['second column'].unique())
else :
    st.write("Hi")

st.title("Make Button")
if st.button("click me"):    
    st.subheader('third cloumn.unique')
    st.dataframe(df['third cloumn'].unique())
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
    st.dataframe(df.sort_values("second column"))
else :
    st.dataframe(df.sort_values("second column",ascending=False))

# 체크박스 (체크하면 True)

if st.checkbox("체크할때만 나옴"):
    st.write("Hi")
    st.dataframe(df.head())

# 셀렉트박스 (여러개 중에서 1개만 고르기)
st.title('IMI CCI')
option = st.selectbox(
    '당신의 직책을 선택해주세요.',
    pd.Series(['CEO', 'AI Engineer', 'Intern', 'Product Manager']))
# option = st.sidebar.selectbox(
#     '당신의 직책을 선택해주세요.',
#     pd.Series(['CEO', 'AI Engineer', 'Intern', 'Product Manager']))
f'You selected: {option}'