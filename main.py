from urllib.parse import urlparse

import array as ar
from array import *
import streamlit as st
import speech_recognition as sr
from googlesearch import search

# st.markdown(
#     """
#     <style>
#     .reportview-container {
#         background: url("D://photo-1507525428034-2")
#     }
#    .sidebar .sidebar-content {
#         background: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTh8fHxlbnwwfHx8fA%3D%3D&w=1000&q=80")
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
st.image('https://jssors8.azureedge.net/demos/image-slider/img/faded-monaco-scenery-evening-dark-picjumbo-com-image.jpg', width=None)
# st.title("GG search with speech")
st.markdown("<h1 style='text-align: center; color: #F63366;'>GG search with speech</h1>", unsafe_allow_html=True)

hobbies = st.selectbox("",
                         ["Select a subject",'Music/ Video', 'Film/ Movie', 'News'])

res = st.button("What you wanna search?")
# if res: st.write(max(10, 20))

recognizer = sr.Recognizer()

domain_music_video = ["www.youtube.com"]
                #"zingmp3.vn", "nhacdj.vn", "soundcloud.com", "imuzik.viettel.vn",
        #"keeng.vn", "nhaccuatui.com", "vi.chiasenhac.vn", "www.spotify.com", "nhac.vn"]

domain_film = ["vtvgiaitri.vn ", "tv.zing.vn", "fptplay.vn", "phim.keeng.vn", "danet.vn", "netflix.com",
                "biphimz.tv", "phymmoi.net", "phimbathu.com", "bilutv.com", "xemphimso.com", "hdviet.com",
                "vuviphim.com"]

domain_news = ["news.zing.vn", "vnexpress.net", "www.24h.com.vn", "vietnamnet.vn",
                "tuoitre.vn", "kenh14.vn", "www.dkn.tv", "www.doisongphapluat.com", "dantri.com.vn",
                "thanhnien.vn"]

arr=[]

with sr.Microphone() as source:
        if res:
            st.warning("Adjust noise")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            # st.markdown("_Recording in 5s_")
            st.warning("Start to record in 5s")
            recorded_audio = recognizer.listen(source, timeout=5)
            st.warning("Record successfully")

            try:
                # st.write("Nhận diện đoạn text")
                text = recognizer.recognize_google(
                        recorded_audio,
                        language="vi"
                    )
                st.success("What you have said: " + text)

            except Exception as ex:
                st.write(ex)

            try:
                from googlesearch import search
            except ImportError:
                st.write("No module named 'google' found")

            st.markdown("**Result: **")
            for value in search(text, tld="com", lang="vi", num=5, stop=50, pause=2):
                 #list_url.append(value)
            # for count, value in enumerate(list_url):
                domain = urlparse(value).netloc
                arr.append(value)
                if hobbies == 'Music/ Video' and domain in domain_music_video:
                    st.video(value)
                if hobbies == 'Film/ Movie' and domain in domain_film:
                    st.info(str(value))
                if hobbies == 'News' and domain in domain_news:
                    st.info(str(value))

footer="""<style>

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: grey;
text-align: center;
}
</style>
<div class="footer">
<p>Hoai Linh Luu & Minh Nguyen</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)