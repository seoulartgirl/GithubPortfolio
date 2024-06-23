import streamlit as st
import time

st.subheader('Toast')
st.toast('Your edited image was saved!', icon='😍')

if st.button('Three cheers'):
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hip!')
    time.sleep(.5)
    st.toast('Hooray!', icon='🎉')

def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon = "🥞")

if st.button('Cook breakfast'):
    cook_breakfast()

st.subheader('Progress')
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Rerun")


st.subheader('Spinner')
with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')


st.subheader('Balloons')
st.balloons()


st.subheader('Snow')
st.snow()