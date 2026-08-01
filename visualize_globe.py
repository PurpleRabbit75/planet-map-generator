import streamlit.components.v1 as components
import base64
import streamlit as st

def display_globe(path_to_bmp):
    uploaded = open(path_to_bmp, "rb").read()
    auto_rotate = st.checkbox("Auto-rotate", value=True)

    b64 = base64.b64encode(uploaded).decode()
    data_uri = f"data:image/bmp;base64,{b64}"

    html_code = f"""
    <div id="globeViz" style="width:100%;height:650px;"></div>
    <script src="https://unpkg.com/globe.gl"></script>
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
    components.html(html_code, height=670)