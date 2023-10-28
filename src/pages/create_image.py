import openai
import streamlit as st

# OpenAI APIの設定
openai.api_key = 'YOUR_API_KEY'

# 画像を生成するリクエストの送信
response = openai.Completion.create(
  engine= "davinci",
  prompt= user_input,
  max_tokens=100,
  temperature=0.7
)

# 生成された画像のURLを取得
image_url = response.choices[0].text.strip()

# 画像を表示するなどの処理
# 例えば、matplotlibライブラリを使用して画像を表示する場合
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread(image_url)
user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)
st.image(img, caption='画像キャプション')