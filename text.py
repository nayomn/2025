import streamlit as st
import pandas as pd

st.title("📰 언론사 비교 대시보드 (사용자 입력 버전)")

# 데이터 저장용 (빈 리스트)
if "news_data" not in st.session_state:
    st.session_state["news_data"] = []

# 입력 폼
with st.form("news_form"):
    media = st.text_input("언론사 이름 입력")
    category = st.selectbox("카테고리 선택", ["정치", "경제", "사회", "문화", "스포츠", "기타"])
    title = st.text_input("기사 제목 입력")
    date = st.date_input("날짜 선택")
    submitted = st.form_submit_button("추가하기")

    if submitted:
        new_entry = {"언론사": media, "카테고리": category, "제목": title, "날짜": str(date)}
        st.session_state["news_data"].append(new_entry)
        st.success("✅ 기사가 추가되었습니다!")

# 입력된 데이터프레임
df = pd.DataFrame(st.session_state["news_data"])

if not df.empty:
    st.subheader("📊 언론사별 기사 수")
    count_data = df["언론사"].value_counts()
    st.bar_chart(count_data)

    st.subheader("📰 기사 목록")
    st.write(df)
else:
    st.info("아직 입력된 기사가 없습니다. 위에 내용을 입력해주세요!")


