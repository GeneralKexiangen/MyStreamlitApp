import streamlit as st

st.set_page_config('HKK...')

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title('WOW!HKK')
st.balloons()
st.image('resource/pp.jpg')

