import streamlit as st

st.title("El mejor título del universo")

st.header("Las rosas son rojas")
st.write("William Shakespeare")
image = Image.open ('IMG-20230824-WA0031.png')

st.image(image, caption = 'El amor de tu vida')
