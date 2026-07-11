import streamlit as st
import time

st.set_page_config(
    page_title="🔥 Campfire Relax",
    page_icon="🔥",
    layout="centered"
)

# CSS
st.markdown("""
<style>
.stApp{
    background: linear-gradient(180deg,#09111f,#111827,#1f2937,#000000);
    color:white;
}

h1,h2,h3,p,div{
    color:white;
    text-align:center;
}

.fire{
    font-size:130px;
    animation:flicker 1s infinite alternate;
}

@keyframes flicker{
    0%{transform:scale(1);}
    25%{transform:scale(1.03) rotate(-2deg);}
    50%{transform:scale(0.98);}
    75%{transform:scale(1.05) rotate(2deg);}
    100%{transform:scale(1);}
}

.message{
    font-size:24px;
    padding:15px;
    color:#FFD580;
}

.quote{
    font-size:20px;
    color:#DDDDDD;
    font-style:italic;
    margin-top:20px;
}

.footer{
    color:gray;
    text-align:center;
    margin-top:40px;
}
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown("<h1>🏕️ Campfire Relax</h1>", unsafe_allow_html=True)
st.markdown("<p>잠시 쉬어가세요.</p>", unsafe_allow_html=True)

# 불
st.markdown("<div class='fire'>🔥</div>", unsafe_allow_html=True)

# 타이핑 효과
text = "오늘 하루도 정말 수고하셨습니다."
placeholder = st.empty()

current = ""
for ch in text:
    current += ch
    placeholder.markdown(
        f"<div class='message'>{current}</div>",
        unsafe_allow_html=True
    )
    time.sleep(0.05)

st.markdown("---")

quotes = [
    "불꽃은 조용히 타오르고 있습니다.",
    "조급하지 않아도 괜찮습니다.",
    "천천히 숨을 들이마시고 내쉬어 보세요.",
    "지금 이 순간만큼은 아무 걱정도 내려놓으세요.",
    "오늘의 피로는 이 불꽃과 함께 흘려보내세요.",
    "당신은 충분히 잘하고 있습니다.",
    "잠시 멍하니 바라보는 시간도 소중한 휴식입니다."
]

st.subheader("🌙 오늘의 한마디")

for q in quotes:
    st.markdown(
        f"<div class='quote'>{q}</div>",
        unsafe_allow_html=True
    )
    time.sleep(0.3)

st.markdown("---")

st.subheader("⏳ 아무것도 하지 않는 1분")

progress = st.progress(0)

for i in range(100):
    progress.progress(i + 1)
    time.sleep(0.6)

st.success("1분 동안 충분히 쉬었습니다. 😊")

st.markdown("""
<div class='footer'>
🔥 Campfire Relax<br>
잠시 멈추는 시간도 삶의 일부입니다.
</div>
""", unsafe_allow_html=True)
