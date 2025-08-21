import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천", layout="centered")

st.title("💡 MBTI 기반 직업 추천 서비스")
st.write("당신의 MBTI 유형을 입력하면 적절한 직업을 추천해드립니다!")

# MBTI 선택
mbti = st.selectbox(
    "당신의 MBTI 유형을 선택하세요:",
    ["ISTJ", "ISFJ", "INFJ", "INTJ",
     "ISTP", "ISFP", "INFP", "INTP",
     "ESTP", "ESFP", "ENFP", "ENTP",
     "ESTJ", "ESFJ", "ENFJ", "ENTJ"]
)

# MBTI 직업 추천 데이터
jobs = {
    "ISTJ": ["회계사", "법무사", "데이터 분석가"],
    "ENFP": ["광고 기획자", "언론인", "스타트업 창업가"],
    "INTP": ["연구원", "프로그래머", "전략 컨설턴트"],
    "ESFJ": ["교사", "간호사", "HR 매니저"],
    "ENTJ": ["CEO", "변호사", "프로젝트 매니저"],
    # ... 나머지 MBTI도 추가 가능
}

if mbti:
    st.subheader(f"🔎 {mbti} 유형 추천 직업")
    if mbti in jobs:
        for job in jobs[mbti]:
            st.write(f"- {job}")
    else:
        st.write("아직 데이터가 준비되지 않았습니다 😅")
