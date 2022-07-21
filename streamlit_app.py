import streamlit as st

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
if mood:
    st.balloons()
    st.image('resource/pp.jpg')
    st.success(mood)

