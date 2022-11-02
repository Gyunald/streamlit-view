import streamlit as st
import streamlit_authenticator as stauth
import yaml

hashed_passwords = stauth.Hasher(['123','456']).generate()

with open('C:\Users\kdkim\Desktop\python\streamlit_1\pages\config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('IMI Login', 'main')

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    st.write('Some content')
elif authentication_status == None:
    st.warning('Please enter your username and password')
elif authentication_status == False:
    st.error('Username/password is incorrect')

try:
    if authenticator.register_user('Register user', preauthorization=False):
        st.success('User registered successfully')
except Exception as e:
    st.error(e)

with open('C:\Users\kdkim\Desktop\python\streamlit_1\pages\config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)