import streamlit as st
from newspaper import Article   # pip install newspaper3k

st.title("🕵️ 가짜뉴스 판별 체험 앱 (링크 입력)")

url = st.text_input("뉴스 기사 링크를 입력하세요")

if st.button("분석하기") and url:
    try:
        # 기사 크롤링
        article = Article(url, language="ko")
        article.download()
        article.parse()

        st.subheader("📄 기사 정보")
        st.write(f"**제목:** {article.title}")
        st.write(f"**언론사:** {article.source_url}")
        st.write(article.text[:300] + "..." if len(article.text) > 300 else article.text)

        # 간단한 규칙 기반 가짜뉴스 분석
        fake_keywords = ["충격", "긴급", "단독", "파격", "제보", "소름"]
        trust_keywords = ["정부", "통계청", "공식", "발표", "자료"]

        fake_count = sum(word in article.text for word in fake_keywords)
        trust_count = sum(word in article.text for word in trust_keywords)

        score = 50 + fake_count*10 - trust_count*5
        score = max(0, min(100, score))  # 0~100 범위 제한

        st.subheader("🔎 분석 결과")
        st.write(f"**가짜뉴스 가능성: {score}%**")

        st.markdown("**판별 근거:**")
        if fake_count > 0:
            st.write(f"⚠ 과장된 표현 발견: {fake_count}회")
        if trust_count > 0:
            st.write(f"✅ 신뢰 키워드 발견: {trust_count}회")
        if fake_count == 0 and trust_count == 0:
            st.write("중립적인 표현으로 판단됩니다.")

    except Exception as e:
        st.error(f"뉴스를 불러올 수 없습니다 😢: {e}")





