from pathlib import Path

import streamlit as st

BASE_DIR = Path(__file__).resolve().parent
html_path = BASE_DIR / "index.html"

st.set_page_config(page_title="Laban Ekitela", page_icon="🚀", layout="wide")

if not html_path.exists():
    st.error("Missing required file: index.html")
    st.stop()

try:
    html = html_path.read_text(encoding="utf-8")
except OSError as exc:
    st.error(f"Unable to read index.html: {exc}")
    st.stop()

st.components.v1.html(html, height=5000, scrolling=True)
