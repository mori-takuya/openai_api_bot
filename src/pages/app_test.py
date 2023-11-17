
import streamlit as st
import openai

# Streamlit Community Cloudの「Secrets」からOpenAI API keyを取得
openai.api_key = st.secrets.OpenAIAPI.openai_api_key

system_prompt="""
あなたはITエンジニアのための技術アシスタントです。
IT技術以外のことは絶対に答えないでください。
"""

# st.session_stateを使いメッセージのやりとりを保存
if "messages_test" not in st.session_state:
    st.session_state["messages_test"] = [
        {"role": "system", "content": system_prompt}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages_test = st.session_state["messages_test"]

    user_message_test = {"role": "user", "content": st.session_state["user_input"]}
    messages_test.append(user_message_test)

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_test
    )  

    bot_message_test = response["choices"][0]["message"]
    messages_test.append(bot_message_test)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title("ITアシスタントbot")

user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages_test"]:
    messages_test = st.session_state["messages_test"]

    for message_test in reversed(messages_test[1:]):  # 直近のメッセージを上に
        speaker = "自分"
        if message_test["role"]=="assistant":
            speaker="AI"

        st.write(speaker + ": " + message_test["content"])
        st.write("-----------------------------------------------------------------")
