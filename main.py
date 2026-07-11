import streamlit as st
import random
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="Campfire Relax",
    page_icon="🔥",
    layout="wide"
)

# 캠핑 테마
themes = {
    "🌲 숲속 캠핑": {
        "bg": "#C8E6C9",
        "name": "조용한 숲속의 밤"
    },
    "🏞️ 호숫가 캠핑": {
        "bg": "#B3E5FC",
        "name": "잔잔한 호숫가"
    },
    "❄️ 겨울 캠핑": {
        "bg": "#ECEFF1",
        "name": "눈 내리는 겨울 밤"
    },
    "🏖️ 해변 캠핑": {
        "bg": "#FFE0B2",
        "name": "노을이 지는 해변"
    }
}

# 테마 선택
theme = st.sidebar.selectbox(
    "🏕️ 캠핑 장소 선택",
    list(themes.keys())
)

background = themes[theme]["bg"]

# CSS
st.markdown(f"""
<style>

.stApp {{
    background:{background};
}}

h1 {{
    color:#111111;
    font-size:55px;
    font-weight:900;
    text-align:center;
}}

h2,h3,p,div {{
    color:#111111;
    text-align:center;
    font-weight:600;
}}

.subtitle {{
    font-size:25px;
    color:#333333;
}}

.fire {{
    font-size:240px;
    text-align:center;
    animation:flicker 1s infinite alternate;
}}

@keyframes flicker {{
    0% {{
        transform:scale(1);
    }}

    50% {{
        transform:scale(1.08);
    }}

    100% {{
        transform:scale(0.95);
    }}
}}

.stars {{
    font-size:30px;
    animation:blink 2s infinite;
}}

@keyframes blink {{
    50% {{
        opacity:0.3;
    }}
}}

.quote {{
    background:rgba(255,255,255,0.6);
    padding:20px;
    border-radius:15px;
    font-size:25px;
    color:#111111;
}}

.footer {{
    font-size:15px;
    color:#555555;
}}

</style>
""", unsafe_allow_html=True)


# 제목
st.markdown("🔥 Campfire Relax")

st.markdown(
    f"""
    <div class="subtitle">
    {themes[theme]["name"]}<br>
    잠시 쉬어가는 시간을 가져보세요.
    </div>
    """,
    unsafe_allow_html=True
)


# 별
st.markdown(
    """
    <div class="stars">
    ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨
    </div>
    """,
    unsafe_allow_html=True
)


# 불멍
st.markdown(
    """
    <div class="fire">
    🔥
    </div>
    """,
    unsafe_allow_html=True
)


# 문구
messages = [
    "오늘 하루도 정말 수고했습니다.",
    "잠시 아무 생각 없이 쉬어도 괜찮아요.",
    "천천히 타오르는 불꽃처럼 편안하게 쉬어가세요.",
    "작은 휴식이 큰 힘이 됩니다.",
    "지금 이 순간만큼은 걱정을 내려놓아 보세요."
]


st.markdown(
    f"""
    <div class="quote">
    💬 {random.choice(messages)}
    </div>
    """,
    unsafe_allow_html=True
)


st.write("")


# 버튼
col1, col2, col3 = st.columns(3)


with col1:
    if st.button("☕ 커피 한잔"):
        st.info("따뜻한 커피처럼 마음도 천천히 편안해집니다.")


with col2:
    if st.button("🌿 심호흡"):
        st.success("천천히 숨을 들이마시고, 천천히 내쉬어 보세요.")


with col3:
    if st.button("❤️ 응원받기"):
        st.balloons()
        st.success("오늘도 충분히 잘하고 있습니다.")


# 시간
st.divider()

st.markdown("### 🕒 현재 시간")

st.metric(
    "현재",
    datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)


# 마무리
st.divider()

st.markdown(
    """
    <div class="footer">
    🔥 Campfire Relax<br>
    마음이 쉬어가는 작은 공간
    </div>
    """,
    unsafe_allow_html=True
)
