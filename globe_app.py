import base64

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="3D Globe Viewer", layout="wide")
st.title("Equirectangular Map \u2192 3D Globe")

uploaded = st.file_uploader(
    "Upload an equirectangular projection image",
    type=["png", "jpg", "jpeg"],
)

auto_rotate = st.checkbox("Auto-rotate", value=True)

if uploaded:
    # Data-URI approach: works with no extra file server, fine up to a few MB.
    # For very large textures, save to a static dir and pass a URL instead.
    b64 = base64.b64encode(uploaded.getvalue()).decode()
    data_uri = f"data:{uploaded.type};base64,{b64}"

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
else:
    st.info("Upload an equirectangular image to render it on a 3D globe.")
