import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="PickShare", layout="wide", initial_sidebar_state="collapsed")

# Hide Streamlit chrome so the app fills the screen cleanly
st.markdown("""
<style>
  #MainMenu, header, footer { display: none !important; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  section[data-testid="stAppViewContainer"] { background: #EFE8DA; }
</style>
""", unsafe_allow_html=True)

html = Path("index.html").read_text(encoding="utf-8")
components.html(html, height=900, scrolling=False)
