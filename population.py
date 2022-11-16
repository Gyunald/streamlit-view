import pandas as pd
import streamlit as st

month = 10

file_path = 'https://raw.githubusercontent.com/Gyunald/streamlit-view/main/population/2022_10.csv'
p_file_path = 'https://raw.githubusercontent.com/Gyunald/streamlit-view/main/population/2022_09.csv'
rename_columns = {'등록인구':'인구','등록인구.3' : '내국인', '등록인구.6': '외국인'}
rename_index = {'합계':'파주시'}
drops = ['시점','등록인구.1','등록인구.2','등록인구.4','등록인구.5','등록인구.7','등록인구.8']

def draw_color(x,color): 
    color = f"background-color : {color}"
    return [color]

def color_negative_red(val):
    color = '#FFA07A' if val < 0 else '#4682B4'
    # return 'background-color: %s' % color
    return 'color: %s' % color

a = pd.read_csv(file_path,encoding='cp949',index_col=1)
aa = pd.read_csv(p_file_path,encoding='cp949',index_col=1)

a = a.drop(['읍면동별(1)'],axis=0)
a = a.drop(drops,axis=1)
a.rename(columns=rename_columns,index=rename_index, inplace=True)

aa = aa.drop('읍면동별(1)',axis=0)
aa = aa.drop(drops,axis=1)
aa.rename(columns=rename_columns,index=rename_index, inplace=True)


for i in a.columns:
    a[i] = a[i].astype(int)
    aa[i] = aa[i].astype(int)

aaa = aa.sub(a)

with st.expander(f"파주시 인구 - {month}월"):
    st.table(a.style.format('{:,}'))
    
c3,c4 = st.columns([1,1])
with c3:
    st.dataframe(a[0:1].style.apply(draw_color, color='#FFA07A', subset=pd.IndexSlice[['파주시'],'인구'],axis=1).format('{:,}'))
    a2 = a[11:15].copy() # 지우면 경고뜸 
    a2.loc['합계'] = a2[['세대수','인구','내국인','외국인']].sum()
    st.dataframe(a2.style.apply(draw_color, color='#17becf', subset=pd.IndexSlice[['합계'],'인구'],axis=1).format('{:,}'))
    st.subheader(f"운정구 비율 : {(sum(a.iloc[11:15,1]) / a.iloc[0,1]) * 100:.2f} %")
with c4:
    aaa.rename({'파주시':'전월대비'},inplace=True)
    st.dataframe(aaa.style.applymap(color_negative_red).format('{:+,}'))
