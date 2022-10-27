import streamlit as st
import pandas as pd

def menu():
    st.title('ToDo App with Streamlit')
    menu = ['Create', 'Read', 'Update', 'Delete', 'About']
    choice = st.sidebar.selectbox('Menu',menu)
    
    if choice == 'Create' :
        st.subheader('Add Items')
        
        # Layout
        col1, col2 = st.beta_columns(2)
        with col1 :
            task = st.text_area('Task To Do')
        with col2 :
            task_status = st.selectbox('Status',['ToDo','Doing','Done'])
            task_due_date = st.date_input('Due Date')
        
        if st.button('Add Task'):
            st.success(f'Successfilly Added Data: {task}')
        
    elif choice == 'Read' :
        st.subheader('View Items')
    elif choice == 'Update' :
        st.subheader('Edit/Update Items')
    else :
        st.subheader('About')
menu()
