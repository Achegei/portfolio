import streamlit as st

st.set_page_config(page_title="Laban Ekitela", page_icon="🚀", layout="wide")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=5000, scrolling=True)
