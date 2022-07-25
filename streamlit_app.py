import streamlit as st
from PIL import Image

st.set_page_config('HKK...')

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.title('WOW!HKK')
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
mood = st.sidebar.text_input('Write down your mood at right now please.')
img_file_buffer = st.sidebar.camera_input("Take a picture")
if mood and img_file_buffer:
    st.balloons()
    img = Image.open(img_file_buffer)
    st.image(img)
    # st.image('resource/pp.jpg')
    st.success(mood)

