import streamlit as st
import pandas as pd

st.title("🕵️ 가짜뉴스 판별 체험 앱")

# 데이터 저장용
if "news_data" not in st.session_state:
    st.session_state["news_data"] = []

# 입력 폼
url = st.text_input("뉴스 링크 입력")
title = st.text_input("기사 제목 입력")

if st.button("분석하기"):
    if not url or not title:
        st.warning("뉴스 링크와 제목을 모두 입력해주세요!")
    else:
        # 규칙 기반 판별
        fake_keywords = ["충격", "긴급", "단독", "파격", "제보", "소름"]
        trust_keywords = ["정부", "통계청", "공식", "발표", "자료"]

        fake_count = sum(word in title for word in fake_keywords)
        trust_count = sum(word in title for word in trust_keywords)

        score = 50 + fake_count*10 - trust_count*5
        score = max(0, min(100, score))  # 0~100 범위

        # 데이터 저장
        st.session_state["news_data"].append({
            "제목": title,
            "링크": url,
            "가짜뉴스 가능성(%)": score
        })

        # 결과 출력
        st.subheader("🔎 분석 결과")
        st.write(f"**제목:** {title}")
        st.write(f"**뉴스 링크:** {url}")
        st.write(f"**가짜뉴스 가능성: {score}%**")

        st.markdown("**판별 근거:**")
        if fake_count > 0:
            st.write(f"⚠ 과장된 표현 발견: {fake_count}회")
        if trust_count > 0:
            st.write(f"✅ 신뢰 키워드 발견: {trust_count}회")
        if fake_count == 0 and trust_count == 0:
            st.write("중립적인 표현으로 판단됩니다.")

# 전체 데이터 테이블
if st.session_state["news_data"]:
    st.subheader("📄 입력된 뉴스 데이터")
    df = pd.DataFrame(st.session_state["news_data"])
    st.write(df)






