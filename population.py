# import streamlit as st

# col1, col2 = st.columns([1,1])
# col3, col4 = st.columns([1,1])

# with col1:
#     drill_pi = st.number_input("Drill Pi",1.0)
#     st.write(round(25.4 * drill_pi,2))

# with col2:
#     hole = st.number_input("Holes Angle",1)
#     st.write(round(360 / hole,3), 'x', hole)
#     st.write(round(360 / hole,3) / 2)

# with col3:
#     with st.form("my_form",clear_on_submit=False):
#         tap = st.text_input("Inch Tap",placeholder='ex) 1-8, 7/8-9')
#         deep = st.text_input("Deep",placeholder='ex) 1.5-2.5')
#         rpm = st.text_input("RPM",value=100)
#         conversion = st.form_submit_button("CONVERSION")
        
#         if conversion:
#             if tap and rpm != "" and '-' in tap:
#                 if '/' not in tap:
#                     integer = int(tap[:tap.index('-')])
#                     tap_thread = int(tap[tap.index('-')+1:])
#                     tap_pi = integer * 25.4
#                     drill = (integer * 25.4) - (25.4 / tap_thread)
#                     pitch = 25.4 / tap_thread
#                     feed = round(int(rpm)*pitch,2)
#                     z1 = float(deep[:deep.index('-')]) * 25.4
#                     z2 = float(deep[deep.index('-')+1:]) * 25.4

#                     st.write('D',round(drill,3))
#                     st.write('P',round(pitch,3))
#                     st.write('S',int(rpm),'F',feed)
#                     st.write('Z',round(-z1,2),round(-z2,2))

#                 else:
#                     numerator = int(tap[:tap.index('/')])
#                     denominator = int(tap[tap.index('/')+1 : tap.index('-')])
#                     tap_thread = int(tap[tap.index('-')+1:])
#                     tap_pi = (numerator / denominator) * 25.4
#                     drill = (numerator / denominator) * 25.4 - (25.4 / tap_thread)
#                     pitch = 25.4 / tap_thread
#                     feed = round(int(rpm)*pitch,3)
#                     z1 = float(deep[:deep.index('-')]) * 25.4
#                     z2 = float(deep[deep.index('-')+1:]) * 25.4

#                     st.write('D',round(drill,2))
#                     st.write('P',round(pitch,3))
#                     st.write('S',int(rpm),'F',feed)
#                     st.write('Z',round(-z1,2),round(-z2,2))

#             else:
#                 st.warning('나사산을 입력하세요. ex) 1-8')

# with col4:
#     with st.form("time",clear_on_submit=False):
#         holes = st.number_input('Holes',1)
#         f = st.number_input('Feed',value=100, step=10)
#         z = st.number_input('Z',value=10.0, step=0.1)
#         q = st.number_input('Q',value=0.5, step=0.1)
#         r = st.number_input('R',value=0.1,step=0.1)
#         t = r * (z//q)
#         move_time = 1
#         time = (((z / (f / 60))) * (holes * move_time)) 
#         time2 = (((z + t) / (f / 60))  * (holes * (move_time))) 

#         conversion1 = st.form_submit_button("G81")
#         conversion2 = st.form_submit_button("G73")

#         if conversion1:
#             st.write(int(time/60) // 60,'h',int(time/60) % 60,'m',int(time % 60),'s')
        
#         if conversion2:
#             st.write(int(time2 / 60) // 60,'h',int(time2/60) % 60,'m',int(time2 % 60),'s')

import pandas as pd
import streamlit as st

month = 10

file_path = st.secrets.populations.path
p_file_path = st.secrets.populations.p_path
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
    st.dataframe(aaa.style.applymap(color_negative_red).format('{:+,}'))
