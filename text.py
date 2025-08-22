import streamlit as st
import pandas as pd
from newspaper import Article   # pip install newspaper3k

st.title("📰 언론사 비교 대시보드 (뉴스 링크 입력 버전)")

# 데이터 저장용
if "news_data" not in st.session_state:
    st.session_state["news_data"] = []

# 입력 폼
with st.form("link_form"):
    url = st.text_input("뉴스 기사 링크 입력")
    submitted = st.form_submit_button("추가하기")

    if submitted and url:
        try:
            article = Article(url, language="ko")
            article.download()
            article.parse()

            new_entry = {
                "언론사": article.source_url,   # 신문사 주소 (출처)
                "제목": article.title,
                "본문": article.text[:200] + "..." if len(article.text) > 200 else article.text,
                "링크": url
            }
            st.session_state["news_data"].append(new_entry)
            st.success("✅ 뉴스가 추가되었습니다!")
        except Exception as e:
            st.error(f"뉴스를 불러오지 못했습니다: {e}")

# 데이터 출력
df = pd.DataFrame(st.session_state["news_data"])

if not df.empty:
    st.subheader("📊 언론사별 기사 수")
    count_data = df["언론사"].value_counts()
    st.bar_chart(count_data)

    st.subheader("📰 기사 목록")
    st.write(df)
else:
    st.info("아직 입력된 뉴스가 없습니다. 위에 뉴스 링크를 추가해주세요!")



