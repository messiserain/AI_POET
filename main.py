#from dotenv import load_dotenv
#load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

import streamlit as st

st.title("인공지능 가수")
subject = st.text_input("가사의 주제를 입력해주세요.")
st.write("가사의 주제 : " + subject)

if st.button("가사 작성"):
    with st.spinner("가사 작성중 ..."):
        result = chat_model.invoke(subject + "에 대한 가사를 써줘")
        st.write(result.content)