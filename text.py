import streamlit as st
import pandas as pd

# 예시 데이터 직접 생성
data = {
    "언론사": ["A일보", "B신문", "C방송", "D뉴스"],
    "카테고리": ["정치", "경제", "정치", "사회"],
    "제목": ["정부 발표 논란", "증시 폭락", "대통령 연설", "지하철 파업"],
    "날짜": ["2025-08-20", "2025-08-21", "2025-08-21", "2025-08-22"]
}
df = pd.DataFrame(data)

st.title("📰 언론사 비교 대시보드")

# 사이드바
media = st.sidebar.multiselect("언론사 선택", df["언론사"].unique(), default=df["언론사"].unique())
category = st.sidebar.selectbox("카테고리 선택", df["카테고리"].unique())

# 필터링
filtered = df[(df["언론사"].isin(media)) & (df["카테고리"] == category)]

# 기사 수 비교
st.subheader("📊 언론사별 기사 수")
count_data = filtered["언론사"].value_counts()
st.bar_chart(count_data)

# 기사 미리보기
st.subheader("📰 기사 미리보기")
st.write(filtered[["언론사", "제목", "날짜"]])


