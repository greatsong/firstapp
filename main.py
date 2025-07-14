import streamlit as st

# 앱 제목
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="💼")
st.title("💼 MBTI 기반 직업 추천 웹앱")

# MBTI 데이터
mbti_jobs = {
    "INTJ": {
        "추천 직업": ["데이터 과학자", "전략 컨설턴트", "AI 연구원"],
        "설명": "분석적이고 미래지향적인 INTJ는 복잡한 문제 해결과 전략 수립에 탁월합니다."
    },
    "INFP": {
        "추천 직업": ["작가", "심리상담가", "사회운동가"],
        "설명": "이상주의적이고 감성적인 INFP는 의미 있는 일을 추구하고 타인을 돕는 데서 동기를 얻습니다."
    },
    "ENFP": {
        "추천 직업": ["광고 기획자", "브랜드 디자이너", "창업가"],
        "설명": "창의적이고 활발한 ENFP는 아이디어를 확산하고 사람들과 소통하는 일을 잘 해냅니다."
    },
    "ISTJ": {
        "추천 직업": ["회계사", "공무원", "품질관리 전문가"],
        "설명": "신중하고 체계적인 ISTJ는 규칙과 정확성을 중시하는 분야에 강점을 가집니다."
    },
    # 필요 시 다른 유형도 추가 가능
}

# MBTI 선택
mbti_list = list(mbti_jobs.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택해주세요:", mbti_list)

if selected_mbti:
    st.balloons()
    st.subheader(f"🎯 {selected_mbti}에게 어울리는 직업 추천")
    jobs = mbti_jobs[selected_mbti]["추천 직업"]
    explanation = mbti_jobs[selected_mbti]["설명"]

    for idx, job in enumerate(jobs, start=1):
        st.markdown(f"**{idx}. {job}**")

    st.info(f"🧠 {explanation}")
