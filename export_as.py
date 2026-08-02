import streamlit as st

PIL_WRITE_SUPPORTED_EXTENSIONS = {
    # Normal ones
    ".bmp": "image/bmp",
    ".gif": "image/gif",
    ".ico": "image/x-icon",
    ".jpg": "image/jpeg",
    ".png": "image/png",
    ".tiff": "image/tiff",
    ".webp": "image/webp",
    "---": "---",
    # Obscure Ones
    ".apng": "image/png",
    ".bw": "image/sgi",
    ".dds": "image/vnd.ms-dds",
    ".dib": "image/bmp",
    ".icb": "image/x-tga",
    ".im": "image/x-im",
    ".j2c": "image/jp2",
    ".j2k": "image/jp2",
    ".jfif": "image/jpeg",
    ".jp2": "image/jp2",
    ".jpc": "image/jp2",
    ".jpe": "image/jpeg",    
    ".jpeg": "image/jpeg",
    ".jpf": "image/jp2",
    ".jpx": "image/jp2",
    ".mpo": "image/mpo",
    ".pbm": "image/x-portable-anymap",
    ".pcx": "image/x-pcx",
    ".pgm": "image/x-portable-anymap",
    ".pnm": "image/x-portable-anymap",
    ".ppm": "image/x-portable-anymap",
    ".rgb": "image/sgi",
    ".rgba": "image/sgi",
    ".sgi": "image/sgi",
    ".tga": "image/x-tga",
    ".tif": "image/tiff",
    ".vda": "image/x-tga",
    ".vst": "image/x-tga",
}

def make_type_selector():
    output_type = st.selectbox("Export As", list(PIL_WRITE_SUPPORTED_EXTENSIONS), index=4)
    output_MIME="/image/jpeg"
    if output_type is not None and output_type != "---":
        output_MIME = PIL_WRITE_SUPPORTED_EXTENSIONS[output_type]
    if output_type == "---":
        output_type = ".jpg"
        output_MIME="/image/jpeg"
    return output_type, output_MIME