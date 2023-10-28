import openai
import streamlit as st

# OpenAI APIの設定
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

# 画像を生成するリクエストの送信
def generate_image_with_dalle2(prompt):
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
image_url = generate_image_with_dalle2(user_input)
st.image(image_url, caption='画像キャプション')
