import streamlit as st
import pandas as pd

st.set_page_config(page_title="📰 뉴스 3줄 요약기", layout="wide")
st.title("📰 뉴스 3줄 요약기")
st.markdown("뉴스 기사 내용을 입력하면 핵심 내용을 3줄로 요약해 보여줍니다.")

# 데이터 저장용
if "news_data" not in st.session_state:
    st.session_state["news_data"] = []

# 입력
url = st.text_input("🔗 뉴스 링크 입력 (선택)")
text = st.text_area("📝 기사 본문 입력")

if st.button("3줄 요약"):
    if not text.strip():
        st.warning("기사 본문을 입력해주세요!")
    else:
        # 문장 단위로 나누기
        sentences = [s.strip() for s in text.split(". ") if s.strip()]
        # 상위 3문장 추출
        summary = ". ".join(sentences[:3]) + ("..." if len(sentences) > 3 else "")

        # 데이터 저장
        st.session_state["news_data"].append({
            "뉴스 링크": url if url else "-",
            "3줄 요약": summary
        })

        # 결과 출력
        st.subheader("📝 3줄 요약")
        st.write(summary)

# 전체 데이터 테이블
if st.session_state["news_data"]:
    st.subheader("📄 입력된 뉴스 데이터")
    df = pd.DataFrame(st.session_state["news_data"])
    st.dataframe(df.style.set_properties(**{'background-color':'#f0f8ff','color':'#333','font-weight':'bold'}))
