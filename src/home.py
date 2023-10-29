import streamlit as st
import streamlit_authenticator as stauth
import yaml

with open('/mount/src/config/config.yaml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized'],
)

name, authentication_status, username = authenticator.login('Login', 'main')


if 'authentication_status' not in st.session_state:
    st.session_state['authentication_status'] = None

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'ログインに成功しました')
		# ここにログイン後の処理を書く。
elif st.session_state["authentication_status"] is False:
    st.error('ユーザ名またはパスワードが間違っています')
elif st.session_state["authentication_status"] is None:
    st.warning('ユーザ名やパスワードを入力してください')
