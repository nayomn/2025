import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 예시 데이터 불러오기
df = pd.read_csv("news_data.csv")

st.title("📰 언론사 비교 대시보드")

# 사이드바 옵션
media = st.sidebar.multiselect("언론사 선택", df["언론사"].unique(), default=df["언론사"].unique()[0])
category = st.sidebar.selectbox("카테고리 선택", df["카테고리"].unique())
date_range = st.sidebar.date_input("기간 선택", [])

# 필터링
filtered = df[(df["언론사"].isin(media)) & (df["카테고리"] == category)]

# 기사 수 비교
st.subheader("📊 언론사별 기사량")
count_data = filtered["언론사"].value_counts()
st.bar_chart(count_data)

# 기사 미리보기
st.subheader("📰 기사 미리보기")
st.write(filtered[["언론사", "제목", "날짜"]].head(10))

