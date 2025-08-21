import streamlit as st

# 페이지 설정
st.set_page_config(page_title="🌟 MBTI 진로 추천 사이트 🌟", layout="centered")

# 타이틀
st.markdown("<h1 style='text-align: center;'>🌈 MBTI 기반 직업 추천 서비스 🌈</h1>", unsafe_allow_html=True)
st.write("✨ 당신의 성격 유형에 맞는 완벽한 직업을 찾아드립니다! ✨")

# MBTI 선택
mbti = st.selectbox(
    "🔮 당신의 MBTI 유형을 선택하세요:",
    ["ISTJ 🛠️", "ISFJ 🤝", "INFJ 🌌", "INTJ 🧠",
     "ISTP ⚡", "ISFP 🎨", "INFP 💭", "INTP 📚",
     "ESTP 🎯", "ESFP 🎉", "ENFP 🌟", "ENTP 🚀",
     "ESTJ 🏛️", "ESFJ 💕", "ENFJ 🌍", "ENTJ 👑"]
)

# 직업 추천 데이터 (이모지 포함)
jobs = {
    "ISTJ": ["📊 회계사", "⚖️ 법무사", "📈 데이터 분석가"],
    "ISFJ": ["👩‍⚕️ 간호사", "👨‍🏫 교사", "🏛️ 사회복지사"],
    "INFJ": ["🎨 예술가", "📚 심리상담가", "✍️ 작가"],
    "INTJ": ["🧠 과학자", "💻 시스템 분석가", "📊 전략 기획자"],
    "ISTP": ["🔧 엔지니어", "🚗 자동차 정비사", "🕵️ 탐정"],
    "ISFP": ["🎨 디자이너", "🎶 음악가", "📸 사진작가"],
    "INFP": ["✍️ 소설가", "🧘 상담사", "🎭 예술가"],
    "INTP": ["🔬 연구원", "💻 프로그래머", "🧩 전략 컨설턴트"],
    "ESTP": ["🎯 영업 사원", "⚡ 기업가", "🎬 이벤트 기획자"],
    "ESFP": ["🎤 배우", "🎉 방송인", "🎶 가수"],
    "ENFP": ["🎬 광고 기획자", "📰 언론인", "🚀 스타트업 창업가"],
    "ENTP": ["💡 발명가", "🎙️ 방송인", "🚀 벤처기업가"],
    "ESTJ": ["🏛️ 공무원", "📊 관리자", "⚖️ 판사"],
    "ESFJ": ["👩‍🏫 교사", "🏥 간호사", "👨‍💼 HR 매니저"],
    "ENFJ": ["🌍 NGO 활동가", "🎤 강연가", "👩‍🏫 교육자"],
    "ENTJ": ["👑 CEO", "⚖️ 변호사", "📂 프로젝트 매니저"]
}

# 선택된 MBTI에서 이모지만 제거 (키 값 매칭)
mbti_key = mbti.split(" ")[0]

# 추천 직업 표시
if mbti:
    st.markdown(f"<h2 style='text-align: center;'>🔎 {mbti_key} 추천 직업</h2>", unsafe_allow_html=True)
    if mbti_key in jobs:
        for job in jobs[mbti_key]:
            st.markdown(f"<h3 style='text-align: center;'>✨ {job} ✨</h3>", unsafe_allow_html=True)
    else:
        st.write("😅 아직 데이터가 준비되지 않았습니다.")

# 푸터
st.markdown("---")
st.markdown("<p style='text-align: center;'>🌟 제작: 당신의 진로 멘토 AI 🌟</p>", unsafe_allow_html=True)
