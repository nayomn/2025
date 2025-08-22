import streamlit as st
import pandas as pd

st.title("🕵️ 가짜뉴스 판별 체험 앱 (링크 버전 - 간단형)")

if "news_data" not in st.session_state:
    st.session_state["news_data"] = []

url = st.text_input("뉴스 링크 입력")
title = st.text_input("기사 제목 입력")

if st.button("추가하기") and url and title:
    # 규칙 기반 판별 (간단 예시)
    fake_keywords = ["충격", "긴급", "단독", "파격", "소름"]
    trust_keywords = ["정부", "공식", "발표", "자료", "통계"]

    fake_count = sum(word in title for word in fake_keywords)
    trust_count = sum(word in title for word in trust_keywords)

    score = 50 + fake_count*10 - trust_count*5
    score = max(0, min(100, score))

    new_entry = {"제목": title, "링크": url, "가짜뉴스 가능성(%)": score}
    st.session_state["news_data"].append(new_entry)
    st.success("✅ 추가 완료!")

df = pd.DataFrame(st.session_state["news_data"])
st.write(df)





