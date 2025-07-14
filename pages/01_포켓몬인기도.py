import streamlit as st
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(page_title="포켓몬 인기 TOP 10", page_icon="📊")
st.title("📊 전 세계에서 가장 인기 있는 포켓몬 TOP 10")

# 포켓몬 인기 데이터
pokemon_names = [
    "피카츄 ⚡", "리자몽 🔥", "이브이 🌈", "뮤츠 🧬", "루카리오 🐾",
    "개굴닌자 💦", "거북왕 🛡️", "팬텀 👻", "뮤 🌟", "나인테일 🔮"
]
popularity_scores = [98, 92, 90, 88, 85, 83, 81, 79, 77, 75]

# plotly 그래프 생성
fig = go.Figure(data=[
    go.Bar(
        x=pokemon_names,
        y=popularity_scores,
        text=popularity_scores,
        textposition='auto'
    )
])

# 레이아웃 설정
fig.update_layout(
    title="🔥 포켓몬 인기 순위 (인기도 점수 기준)",
    xaxis_title="포켓몬",
    yaxis_title="인기도 (100점 만점)",
    yaxis=dict(range=[0, 100]),
    height=500
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)
