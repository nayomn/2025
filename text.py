import streamlit as st
import pandas as pd
from collections import Counter
import re

st.set_page_config(page_title="📰 뉴스 요약 & 키워드 추출기", layout="wide")
st.title("📰 뉴스 요약 & 핵심 키워드 추출기")
st.markdown("뉴스 링크 또는 기사 내용을 입력하면, 자동으로 요약과 핵심 키워드를 추출해 보여줍니다.")

# 데이터 저장용
if "news_data" not in st.session_state:
    st.session_state["news_data"] = []

# 입력 폼
with st.form("news_form"):
    url = st.text_input("🔗 뉴스 링크 입력 (선택)")
    text = st.text_area("📝 기사 제목/본문 입력")
    submitted = st.form_submit_button("분석하기")

def extract_keywords(text, top_n=10):
    # 간단한 키워드 추출: 공백 분리 후 단어 빈도 계산
    words = re.findall(r'\b\w+\b', text.lower())
    stopwords = ["의", "가", "이", "은", "들", "는", "좀", "잘", "걍", "과", "도", "를", "으로", "자", "에", "와", "한", "하다"]
    words = [w for w in words if w not in stopwords and len(w) > 1]
    counter = Counter(words)
    return counter.most_common(top_n)

if submitted:
    if not text.strip():
        st.warning("기사 내용을 입력해주세요!")
    else:
        # 간단 요약: 첫 3문장
        sentences = text.split(". ")
        summary = ". ".join(sentences[:3]) + ("..." if len(sentences) > 3 else "")

        # 키워드 추출
        keywords = extract_keywords(text)

        # 데이터 저장
        st.session_state["news_data"].append({
            "뉴스 링크": url if url else "-",
            "요약": summary,
            "핵심 키워드": ", ".join([k[0] for k in keywords])
        })

        # 결과 출력
        st.subheader("📝 뉴스 요약")
        st.write(summary)

        st.subheader("🔑 핵심 키워드")
        st.write([f"{k[0]} ({k[1]}회)" for k in keywords])

# 전체 데이터 테이블
if st.session_state["news_data"]:
    st.subheader("📄 입력된 뉴스 데이터")
    df = pd.DataFrame(st.session_state["news_data"])
    st.dataframe(df.style.set_properties(**{'background-color':'#f0f8ff','color':'#333','font-weight':'bold'}))
