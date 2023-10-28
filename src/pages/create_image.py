import openai
import streamlit as st

# OpenAI APIの設定
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# 画像を生成するリクエストの送信
response = openai.Image.create(
  prompt="a",
  n=1,
  size='{}x{}'.format(str(256), str(256))
)

# 生成された画像のURLを取得
image_url = response['data'][0]['url']

# 画像を表示する処理
# user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)
st.image(image_url, caption='画像キャプション')
