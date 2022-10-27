import streamlit as st
import easyocr
import pandas as pd
import io
from PIL import Image
import time

if 'ocr' not in st.session_state:
    st.session_state.ocr = {}
a = st.empty()
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    st.image(uploaded_file)
    bar = st.progress(0)
    bytes_data = uploaded_file.read()
    image = Image.open(io.BytesIO(bytes_data))

    with st.empty():
        st.write('processing...⏳')
        for i in range(0,60):
            time.sleep(0.01)
            bar.progress(i + 1)
        reader = easyocr.Reader(['en'])
        result = reader.readtext(image)
        for j in range(70,100):
            time.sleep(0.01)
            bar.progress(j + 1)
        st.write('✔️ processing completed!')

    for i in result:
        st.session_state.ocr[i[1]] = float(i[1]) * 25.4

    col1, col2, = st.columns([1,1])

    df = pd.DataFrame({'inch' : st.session_state.ocr.keys(), 'mm' : st.session_state.ocr.values()})

    with col1:
        st.table(df)
        st.session_state.ocr = {}