import openai
import streamlit as st
import extra_streamlit_components as stx

#ログインの確認
value = stx.CookieManager().get(cookie='some_cookie_name')
if value == None:
    st.warning("**ログインしてください**")
    st.stop()

# OpenAI APIの設定
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# 画像を生成するリクエストの送信
def dalle2_image(prompt):
  response = openai.Image.create(
    prompt= prompt,
    n=1,
    size='{}x{}'.format(str(256), str(256))
  )
  # 生成された画像のURLを取得
  image_url = response['data'][0]['url']
  return image_url

# 画像を表示する処理
user_input = st.text_input("どのような画像を生成したいですか")
image_url = dalle2_image(user_input)
st.image(image_url, caption='生成画像')
