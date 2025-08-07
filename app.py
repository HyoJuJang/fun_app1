import streamlit as st
import time
import random

# 페이지 설정
st.set_page_config(page_title="📡 정치 성향 측정기", page_icon="📡", layout="centered")

# 제목 및 설명
st.markdown("<h1 style='text-align:center;'>📡 당신의 정치 성향을 측정 중입니다...</h1>", unsafe_allow_html=True)
st.write("국가 정보 센터와 연결 중...\n신경 반응을 감지 중입니다...")

# 애니메이션용 빈 요소
bar_placeholder = st.empty()

# 뇌파 바 애니메이션
bar = ""
for _ in range(20):
    bar += random.choice(["📈", "📉"])
    bar_placeholder.markdown(f"<h3 style='text-align:center;'>{bar}</h3>", unsafe_allow_html=True)
    time.sleep(0.1)

# 버튼
if st.button("🟥 STOP - 측정 종료"):
    st.markdown("---")
    result = random.choice([

        """🧱 **보수적 행보형**  
        변화보다 안정이 중요.  
        아직도 폰 진동 끄는 법 모름.  
        **대표 발언**: "이게 그때 내가 알던 그거 맞아?"  
        """,

        """🪩 **진보 과잉형**  
        매일 가치관 업데이트 중.  
        앱 바뀌면 인생도 바뀜.  
        **대표 발언**: "그건 너무 구시대적이지 않아?"  
        """,

        """🛏 **중립 침대형**  
        정치보다 침대 온도에 관심 많음.  
        **대표 발언**: "난 그냥 그랬으면 좋겠어..."  
        """,

        """🧃 **양비론 젤리형**  
        결론: "다 똑같은 거 아냐?"  
        뭐든 중간, 뭐든 흐물  
        **대표 발언**: "거기서 거기지 뭐."  
        """,

        """🧠 **진지 백서형**  
        혼자 맥락 분석하다 지침.  
        **대표 발언**: "이건 맥락을 봐야지."  
        """,

        """🐒 **선동적 침팬지형**  
        화낼 준비 완료.  
        **대표 발언**: "이게 나라냐!!! (근데 왜 그런진 모름)"  
        """
    ])

    # 결과 출력
    st.success(result)

    # 하단 안내 문구
    st.markdown("""
    ---
    📝 이 테스트는 정치적 성향을 진단하지 않습니다.  
    당신이 어떤 방식으로 피곤한지를 알려줄 뿐입니다.
    """)



# import streamlit as st

# st.set_page_config(page_title="이상한 심리 테스트", page_icon="🧠", layout="centered")

# st.markdown("<h1 style='text-align: center;'>🧠 이상한 심리 테스트</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; font-size:18px;'>당신의 하루는 이미 정해져 있습니다.</p>", unsafe_allow_html=True)
# st.markdown("---")

# st.subheader("Q. 아침에 눈 뜨자마자 가장 먼저 하는 행동은?")

# choice = st.radio(
#     "",
#     ["다시 잔다", "물 마신다", "폰 본다", "존재를 의심한다"]
# )

# if st.button("🔮 결과 보기"):
#     if choice == "다시 잔다":
#         st.success("🥱 당신은 전생에 수면제였습니다.\n\n존재만으로 주변을 나른하게 만드는 재능이 있군요. 오늘 하루 아무 일도 하지 마세요.")
#     elif choice == "물 마신다":
#         st.info("🚰 당신은 정수기 요정입니다.\n\n수분이 있어야 비로소 움직이는 수분 생명체입니다. 오늘은 물 2L 이상 마시세요.")
#     elif choice == "폰 본다":
#         st.warning("📱 당신은 스마트폰의 환생입니다.\n\n당신의 손은 충전기이고, 당신의 뇌는 와이파이입니다. 데이터 무제한 요금제 추천.")
#     elif choice == "존재를 의심한다":
#         st.error("🌀 당신은 시뮬레이션 안의 NPC일지도 모릅니다.\n\n이 테스트 자체가 현실이 아닐 가능성도 있습니다. 이제 깨어나야 할 시간입니다.")

#     st.markdown("---")
#     st.button("↩ 다시 하기", on_click=lambda: st.experimental_rerun())