import streamlit as st

st.title("El mejor título del universo")

st.header("Las rosas son rojas")
st.write("William Shakespeare")
image = Image.open ('guau.jpg')

st.image(image, caption = 'El amor de tu vida')
