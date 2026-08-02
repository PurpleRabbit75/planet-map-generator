import base64
import streamlit as st
from pathlib import Path

def display_globe(path_to_bmp):
    uploaded = open(path_to_bmp, "rb").read()
    auto_rotate = st.checkbox("Auto-rotate", value=True)

    b64 = base64.b64encode(uploaded).decode()
    data_uri = f"data:image/bmp;base64,{b64}"

    js_path = Path(__file__).with_name("globe.gl.min.js")
    globe_js = js_path.read_text(encoding="utf-8")

    html_code = f"""
    <div id="globeViz" style="width:100%;height:650px;"></div>
    <script>{globe_js}</script>
    <script>
        const globe = Globe()
        (document.getElementById('globeViz'))
        .globeImageUrl('{data_uri}')
        .backgroundColor('rgba(0,0,0,0)')
        .width(document.getElementById('globeViz').clientWidth)
        .height(650);

        globe.controls().autoRotate = {str(auto_rotate).lower()};
        globe.controls().autoRotateSpeed = 0.6;
    </script>
    """
    st.iframe(html_code, height=670)