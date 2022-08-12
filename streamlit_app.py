import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="HKK...",
    page_icon="🐬",
    layout="wide",
)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
# st.title("WOW!HKK 🎉️")
st.markdown("# WOW!HKK 🎉️")

mood = st.sidebar.text_input('Write down your mood at right now please.', 'sunshine')
take = st.sidebar.checkbox('Take a picture to upload')
img_file_buffer = None
if take:
    img_file_buffer = st.sidebar.camera_input("Take a picture")
if mood:
    st.balloons()
    c1, c2 = st.columns(2)
    with c1:
        st.write("Your Picture")
        if img_file_buffer:
            img = Image.open(img_file_buffer).resize((800, 600))
            img.save('resource/img.jpg')
            # st.image(img)
            st.image('resource/img.jpg')
        else:
            st.image('resource/pp.jpg')
    with c2:
        st.write("Your Text")
        st.success(mood)
