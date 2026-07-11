import streamlit as st
import random
import time
from pathlib import Path

st.set_page_config(
    page_title="🔥 Campfire Relax",
    page_icon="🏕️",
    layout="wide"
)

####################################
# 배경 CSS
####################################

st.markdown("""
<style>

.stApp{
background:linear-gradient(#06111f,#101820,#000000);
}

.main-title{
text-align:center;
font-size:55px;
color:#FFD369;
}

.sub{
text-align:center;
font-size:22px;
color:white;
}

.fire{
font-size:150px;
text-align:center;
animation:flicker 1s infinite alternate;
}

@keyframes flicker{
0%{transform:scale(1);}
25%{transform:scale(1.03);}
50%{transform:scale(.96);}
75%{transform:scale(1.05);}
100%{transform:scale(1);}
}

.quote{

font-size:28px;
text-align:center;
color:white;
padding:30px;

}

.small{

text-align:center;
color:gray;

}

</style>

""",unsafe_allow_html=True)

####################################
# 제목
####################################

st.markdown("<div class='main-title'>🏕️ Campfire Relax</div>",unsafe_allow_html=True)

st.markdown("<div class='sub'>오늘 하루도 정말 수고하셨습니다.</div>",unsafe_allow_html=True)

####################################
# 테마 선택
####################################

theme=st.sidebar.selectbox(
"캠핑 장소 선택",

[
"🌲 숲속",
"🏞️ 호숫가",
"❄️ 겨울 캠핑"
]

)

image={
"🌲 숲속":"images/forest.jpg",
"🏞️ 호숫가":"images/lake.jpg",
"❄️ 겨울 캠핑":"images/winter.jpg"
}

if Path(image[theme]).exists():
    st.image(image[theme],use_container_width=True)

####################################
# 불멍
####################################

st.markdown("<div class='fire'>🔥</div>",unsafe_allow_html=True)

####################################
# 자연소리
####################################

sound=st.sidebar.selectbox(

"자연 소리",

[
"🔥 장작",
"🌧️ 빗소리",
"🌊 파도",
"🌲 숲"
]

)

audio={
"🔥 장작":"sounds/fire.mp3",
"🌧️ 빗소리":"sounds/rain.mp3",
"🌊 파도":"sounds/ocean.mp3",
"🌲 숲":"sounds/forest.mp3"
}

if Path(audio[sound]).exists():

    st.audio(audio[sound])

####################################
# 명언
####################################

quotes=[

"천천히 쉬어도 괜찮습니다.",

"불꽃은 서두르지 않아도 계속 타오릅니다.",

"오늘 하루도 충분히 잘했습니다.",

"잠시 멍하니 있는 시간도 소중합니다.",

"지금 이 순간을 즐겨보세요.",

"모든 걱정은 잠시 내려두세요.",

"행복은 이렇게 작은 쉼에서 시작됩니다."

]

st.markdown(
f"<div class='quote'>{random.choice(quotes)}</div>",
unsafe_allow_html=True
)

####################################
# 힐링 타이머
####################################

minute=st.sidebar.selectbox(

"힐링 시간",

[
5,
10,
30
]

)

if st.button("힐링 시작 🌙"):

    progress=st.progress(0)

    seconds=minute*60

    for i in range(seconds):

        progress.progress((i+1)/seconds)

        time.sleep(1)

    st.success("편안한 시간이었습니다 😊")

####################################
# 별똥별
####################################

if random.randint(1,6)==1:

    st.balloons()

####################################

st.markdown("---")

st.markdown(

"<div class='small'>🔥 Campfire Relax | 마음이 쉬어가는 공간</div>",

unsafe_allow_html=True
)
