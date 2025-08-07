import streamlit as st

st.set_page_config(page_title="이상한 심리 테스트", page_icon="🧠", layout="centered")

st.markdown("<h1 style='text-align: center;'>🧠 이상한 심리 테스트</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>당신의 하루는 이미 정해져 있습니다.</p>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("Q. 아침에 눈 뜨자마자 가장 먼저 하는 행동은?")

choice = st.radio(
    "",
    ["다시 잔다", "물 마신다", "폰 본다", "존재를 의심한다"]
)

if st.button("🔮 결과 보기"):
    if choice == "다시 잔다":
        st.success("🥱 당신은 전생에 수면제였습니다.\n\n존재만으로 주변을 나른하게 만드는 재능이 있군요. 오늘 하루 아무 일도 하지 마세요.")
    elif choice == "물 마신다":
        st.info("🚰 당신은 정수기 요정입니다.\n\n수분이 있어야 비로소 움직이는 수분 생명체입니다. 오늘은 물 2L 이상 마시세요.")
    elif choice == "폰 본다":
        st.warning("📱 당신은 스마트폰의 환생입니다.\n\n당신의 손은 충전기이고, 당신의 뇌는 와이파이입니다. 데이터 무제한 요금제 추천.")
    elif choice == "존재를 의심한다":
        st.error("🌀 당신은 시뮬레이션 안의 NPC일지도 모릅니다.\n\n이 테스트 자체가 현실이 아닐 가능성도 있습니다. 이제 깨어나야 할 시간입니다.")

    st.markdown("---")
    st.button("↩ 다시 하기", on_click=lambda: st.experimental_rerun())