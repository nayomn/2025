import streamlit as st

st.title("🕵️ 가짜뉴스 판별 체험 앱")

# 사용자 입력
text = st.text_area("기사 제목이나 내용을 입력하세요")

# 판별 버튼
if st.button("분석하기"):
    if text.strip() == "":
        st.warning("분석할 기사를 입력하세요!")
    else:
        # 간단한 규칙 기반 분석 (예시)
        fake_keywords = ["충격", "긴급", "단독", "파격", "제보", "소름"]
        trust_keywords = ["정부", "통계청", "공식", "발표", "자료"]

        fake_count = sum(word in text for word in fake_keywords)
        trust_count = sum(word in text for word in trust_keywords)

        score = 50 + fake_count*10 - trust_count*5
        score = max(0, min(100, score))  # 0~100 사이 제한

        st.subheader("🔎 분석 결과")
        st.write(f"**가짜뉴스 가능성: {score}%**")

        st.markdown("**판별 근거:**")
        if fake_count > 0:
            st.write(f"⚠ 과장된 표현 발견: {fake_count}회")
        if trust_count > 0:
            st.write(f"✅ 신뢰 키워드 발견: {trust_count}회")
        if fake_count == 0 and trust_count == 0:
            st.write("중립적인 표현으로 판단됩니다.")




