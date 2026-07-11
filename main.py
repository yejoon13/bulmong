import streamlit as st
import random
from datetime import datetime

st.set_page_config(
    page_title="Campfire Relax",
    page_icon="🔥",
    layout="wide"
)


# ---------------------------
# 테마
# ---------------------------

themes = {
    "🌲 숲속 캠핑": {
        "sky": "#9CCBFF",
        "ground": "#4E7A45",
        "mountain": "#355834"
    },

    "🏞️ 호숫가 캠핑": {
        "sky": "#A7D8FF",
        "ground": "#4B8FA8",
        "mountain": "#486581"
    },

    "❄️ 겨울 캠핑": {
        "sky": "#D9EAF7",
        "ground": "#FFFFFF",
        "mountain": "#78909C"
    },

    "🏖️ 해변 캠핑": {
        "sky": "#FFD59A",
        "ground": "#D8B26E",
        "mountain": "#8D6E63"
    }
}


choice = st.sidebar.selectbox(
    "🏕️ 캠핑 장소",
    list(themes.keys())
)


theme = themes[choice]


# ---------------------------
# CSS
# ---------------------------

st.markdown(
f"""

<style>

.stApp {{

background:
linear-gradient(
180deg,
{theme["sky"]} 0%,
{theme["sky"]} 55%,
{theme["ground"]} 100%
);

}}


h1,h2,h3,p,div {{

color:#111111;
text-align:center;

}}


.title {{

font-size:55px;
font-weight:900;

}}


.scene {{

height:180px;
position:relative;

}}


.mountain {{

position:absolute;
bottom:0;
left:0;
width:100%;
height:100px;

background:{theme["mountain"]};

clip-path:
polygon(
0 80%,
20% 30%,
40% 75%,
60% 25%,
80% 70%,
100% 35%,
100% 100%,
0 100%
);

}}


/* 별 */

.star {{

font-size:35px;
animation:twinkle 2s infinite;

}}


@keyframes twinkle {{

50%{{opacity:.3;}}

}}



/* 불꽃 */

.fireplace {{

margin-top:20px;

}}


.flame {{

position:relative;

margin:auto;

width:150px;
height:220px;

background:
linear-gradient(
orange,
red
);

border-radius:
50% 50% 40% 40%;

animation:
fireMove .35s infinite alternate;

box-shadow:
0 0 40px orange,
0 0 80px red;

}}



.flame:before {{

content:"";

position:absolute;

bottom:25px;
left:35px;

width:80px;
height:130px;

background:
linear-gradient(
yellow,
orange
);

border-radius:
50%;

animation:
innerFire .25s infinite alternate;

}}



@keyframes fireMove {{

from{{transform:rotate(-5deg) scale(1);}}

to{{transform:rotate(5deg) scale(1.05);}}

}}



@keyframes innerFire {{

from{{transform:translateX(-5px);}}

to{{transform:translateX(8px);}}

}}



.wood {{

font-size:70px;

}}



.quote {{

background:
rgba(255,255,255,.65);

padding:20px;

border-radius:20px;

font-size:25px;

margin:20px;

}}


</style>

""",
unsafe_allow_html=True
)



# ---------------------------
# 화면
# ---------------------------

st.markdown(
"<div class='title'>🏕️ Campfire Relax</div>",
unsafe_allow_html=True
)


st.markdown(
f"""
<h3>
{choice}<br>
잠시 멈추고 불꽃을 바라보세요.
</h3>
""",
unsafe_allow_html=True
)



# 하늘 별

st.markdown(
"""
<div class="star">
⭐ ✨ ⭐ ✨ ⭐ ✨ ⭐
</div>
""",
unsafe_allow_html=True
)



# 산 배경

st.markdown(
"""
<div class="scene">

<div class="mountain"></div>

</div>
""",
unsafe_allow_html=True
)



# 불꽃

st.markdown(
"""
<div class="fireplace">

<div class="flame"></div>

<div class="wood">
🪵🪵🪵
</div>

</div>
""",
unsafe_allow_html=True
)



# 위로 문구

quotes=[

"오늘 하루도 정말 수고했습니다.",

"불꽃처럼 천천히 마음을 녹여보세요.",

"잠시 아무 생각 없이 쉬어도 괜찮습니다.",

"작은 휴식이 내일의 힘이 됩니다.",

"지금 이 순간만 바라보세요."

]


st.markdown(
f"""
<div class="quote">

💬 {random.choice(quotes)}

</div>
""",
unsafe_allow_html=True
)



# 버튼

c1,c2,c3=st.columns(3)


with c1:

    if st.button("☕ 따뜻한 커피"):
        st.success(
            "따뜻한 커피 한잔과 함께 쉬어가세요."
        )


with c2:

    if st.button("🌿 심호흡"):
        st.success(
            "천천히 숨을 들이마시고 내쉬어 보세요."
        )


with c3:

    if st.button("❤️ 응원"):
        st.balloons()
        st.success(
            "오늘도 충분히 잘하고 있습니다."
        )



st.divider()


st.markdown("### 🕒 현재 시간")


st.metric(
    "Time",
    datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )
)


st.caption(
"🔥 Campfire Relax - 마음이 쉬어가는 공간"
)
