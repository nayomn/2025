import streamlit as st
import pandas as pd

st.set_page_config(page_title="🕵️‍♀️ 가짜뉴스 판별 체험 앱", layout="wide")
st.title("🕵️‍♀️ 가짜뉴스 판별 체험 앱")
st.markdown("🔗 링크와 기사 제목을 입력하면 가짜뉴스 가능성을 분석하고, 상세 근거와 신뢰 요소를 보여줍니다.")

# 데이터 저장용
if "news_data" not in st.session_state:
    st.session_state["news_data"] = []

# 입력 폼
with st.form("news_form"):
    url = st.text_input("🖇 뉴스 링크 입력")
    title = st.text_input("📝 기사 제목 입력")
    submitted = st.form_submit_button("분석하기")

if submitted:
    if not url or not title:
        st.warning("⚠ 뉴스 링크와 제목을 모두 입력해주세요!")
    else:
        # 규칙 기반 판별
        fake_keywords = ["충격", "긴급", "단독", "파격", "소름", "경악", "대박", "믿기 힘든"]
        trust_keywords = ["정부", "통계청", "공식", "발표", "자료", "보도", "기관"]

        # 과장 표현, 신뢰 키워드, 출처 불명 체크
        fake_count = sum(word in title for word in fake_keywords)
        trust_count = sum(word in title for word in trust_keywords)
        source_count = 0
        source_phrases = ["익명의 제보자", "누군가에 따르면", "전해진 바에 따르면"]

        # 실제 문장 포함 확인
        fake_sentences = [kw for kw in fake_keywords if kw in title]
        trust_sentences = [kw for kw in trust_keywords if kw in title]
        source_sentences = [kw for kw in source_phrases if kw in title]
        source_count = len(source_sentences)

        # 점수 계산
        score = 50 + fake_count*10 - trust_count*5
        score = max(0, min(100, score))  # 0~100 범위

        # 등급/색상/이모지
        if score >= 70:
            color = "🔴 위험"
            emoji = "🚨"
        elif score >= 40:
            color = "🟡 주의"
            emoji = "⚠️"
        else:
            color = "🟢 신뢰"
            emoji = "✅"

        # 데이터 저장
        st.session_state["news_data"].append({
            "제목": title,
            "링크": url,
            "가짜뉴스 가능성(%)": score,
            "등급": color
        })

        # 결과 출력
        st.subheader(f"{emoji} 분석 결과")
        st.markdown(f"**제목:** {title}")
        st.markdown(f"**뉴스 링크:** [바로가기]({url})")
        st.markdown(f"**가짜뉴스 가능성:** {score}%")
        st.markdown(f"**등급:** {color}")

        # 상세 근거
        with st.expander("🔍 판별 근거 자세히 보기"):
            st.markdown(f"⚠ 과장 표현 발견: {fake_count}회")
            for s in fake_sentences:
                st.write(f"- {s}")

            st.markdown(f"❓ 출처 불명 발견: {source_count}회")
            for s in source_sentences:
                st.write(f"- {s}")

            st.markdown(f"✅ 신뢰 키워드 발견: {trust_count}회")
            for s in trust_sentences:
                st.write(f"- {s}")

            if fake_count == 0 and trust_count == 0 and source_count == 0:
                st.write("💬 중립적인 표현으로 판단됩니다.")

        # 사용자 안내
        st.info("ℹ️ 점수는 규칙 기반 분석 결과이며, 100% 정확하지 않습니다. 참고용으로 활용해주세요.")

# 전체 데이터 테이블
if st.session_state["news_data"]:
    st.subheader("📄 입력된 뉴스 데이터")
    df = pd.DataFrame(st.session_state["news_data"])
    st.dataframe(df.style.set_properties(**{'background-color':'#f0f8ff','color':'#333','font-weight':'bold'}))
