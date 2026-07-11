import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Campfire Relax", page_icon="🔥", layout="wide")

themes = {
    "🌲 숲속": {
        "bg": "#0b3d0b",
        "text": "숲속의 조용한 밤"
    },
    "🏞️ 호숫가": {
        "bg": "#0b4f6c",
        "text": "잔잔한 호숫가"
    },
    "❄️ 겨울": {
        "bg": "#3b4c6b",
        "text": "눈 내리는 겨울 캠핑"
    },
    "🏖️ 해변": {
        "bg": "#e89b3d",
        "text": "노을이 지는 해변"
    }
}

theme = st.sidebar.selectbox("배경 선택", list(themes.keys()))

bg = themes[theme]["bg"]

st.markdown(f"""
<style>

.stApp {{
background:{bg};
color:white;
}}

h1,h2,h3,p,div {{
color:white;
text-align:center;
}}

.fire {{
font-size:220px;
animation:flicker 1s infinite alternate;
}}

@keyframes flicker {{
0%{{transform:scale(1);}}
50%{{transform:scale(1.08);}}
100%{{transform:scale(.95);}}
}}

.star {{
font-size:24px;
animation:blink 2s infinite;
}}

@keyframes blink {{
50%{{opacity:0.2;}}
}}

button {{
width:100%;
}}

</style>
""", unsafe_allow_html=True)

st.title("🏕️ Campfire Relax")

st.write(themes[theme]["text"])

st.markdown(
"<div class='star'>✨ ⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐ ✨</div>",
unsafe_allow_html=True
)

st.markdown(
"<div class='fire'>🔥</div>",
unsafe_allow_html=True
)

quotes = [
"오늘도 정말 수고했어요.",
"잠시 쉬어가도 괜찮습니다.",
"불꽃처럼 천천히 마음을 녹여보세요.",
"당신은 충분히 잘하고 있습니다.",
"오늘 하루도 의미 있는 하루였습니다."
]

st.subheader("💬 오늘의 위로")

st.success(random.choice(quotes))

col1,col2,col3=st.columns(3)

with col1:
    if st.button("☕ 커피 한잔"):
        st.info("따뜻한 커피 한잔이 마음을 편안하게 합니다.")

with col2:
    if st.button("🌿 심호흡"):
        st.success("천천히 숨을 들이마시고 내쉬어 보세요.")

with col3:
    if st.button("❤️ 응원받기"):
        st.balloons()
        st.success("당신은 충분히 잘하고 있습니다!")

st.markdown("---")

st.subheader("🕒 현재 시간")

st.metric(
"Now",
datetime.now().strftime("%Y-%m-%d %H:%M:%S")
)

st.markdown("---")

st.caption("🔥 Made with Streamlit")
