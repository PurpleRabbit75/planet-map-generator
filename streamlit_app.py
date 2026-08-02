import streamlit as st
from time import sleep
import json
from fetch_map import get_maps
from parse_args import build_map_form_data, build_globe_params
from visualize_globe import display_globe


st.title("Planet Map Generator")
st.write(
    "This website is based on https://topps.diku.dk/torbenm/maps.msp"
)

st.divider()
uploaded_file = st.file_uploader("[Optional] Upload map.json parameters file", type="json", width=400)
if uploaded_file is not None:
    uploaded_params = dict(json.load(uploaded_file))
else:
    with open("default.json", "r") as f:
        uploaded_params = dict(json.load(f))


st.text("Alternatively, edit the defaults in the fields below: ")
st.divider()
# st.text(str(uploaded_file) + "\n\n" + str(type(uploaded_file)) + "\n\n" + str(uploaded_params))


col1, col2 = st.columns(2)

with col1:
    seed = st.number_input("Seed", value=int(uploaded_params["seed"]))
    width = st.number_input("Width (max 2000):", value=int(uploaded_params["width"]))
    height = st.number_input("Height (max 2000):", value=int(uploaded_params["height"]))
    zoom = st.number_input("Zoom (0.1 to 10000):", value=float(uploaded_params["zoom"]))
    center_lat = st.number_input("Center Latitude (-90 to 90):", value=float(uploaded_params["lati"]))
    center_long = st.number_input("Center Longitude (-360 to 360):", value=float(uploaded_params["longi"]))
    grid = st.text_input("Grid (none or 1 to 90)", value=uploaded_params["grid"])

with col2:
    projection = st.selectbox("Projection", options=sorted(["Mollweide", "Mercator", "Peters", "Square", "Stereographic", "Orthographic", "Gnomonic", "Area Preserving Azimuthal", "Conical", "Icosahedral", "Sinusoidal", "Equirectangular"], key=uploaded_params["projection"].__ne__))
    colourmap = st.selectbox("Colourmap", options=sorted(["Olsson", "Olsson Light", "Olsson2", "OlssonW", "Mogensen", "Mogensen black", "Bathymetric", "Burrows", "Burrows black", "Mars", "White", "Yellow", "Greyscale", "Black body radiation", "Lefebvre", "Lefebvre2", "uniform blue/green"], key=uploaded_params["colourmap"].__ne__))
    shading = st.selectbox("Shading", options=sorted(["None", "Bumpmap", "Bumpmap on land only", "Daylight"], key=uploaded_params["shading"].__ne__))
    st.space(size="xxsmall")
    contours = st.radio("Contour lines", options=sorted(["None", "Coastlines only", "2 (land)", "5 (land)", "10 (land)", "1 (coast)", "2 (coast)", "3 (coast)"], key=uploaded_params["outline"].__ne__), horizontal = True)
    st.space(size="xxsmall")
    adjust_color_by_latitude = st.radio("Adjust Color by Latitude", options=sorted(["No", "Yes", "Yes, strongly", "Yes, very strongly"], key=uploaded_params["polar"].__ne__), horizontal = True)
    water = st.number_input("Water line (-0.1 to 0.1):", value=float(uploaded_params["water"]))

col3, col4, col5 = st.columns(3, border=True)

with col3:
    altitude_scaling = st.checkbox("Non-linear altitude scaling", value=uploaded_params["nonLinear"] if "nonLinear" in uploaded_params else False)
with col4:
    wrinkly_maps = st.checkbox('Make more "wrinkly" maps', value=uploaded_params["wrinkly"] if "wrinkly" in uploaded_params else False)
with col5:
    biome_maps = st.checkbox("Make biome maps", value=uploaded_params["biome"] if "biome" in uploaded_params else False)




general_params = build_map_form_data(
        seed, width, height, zoom, center_lat, center_long, grid, projection, 
        colourmap, shading, contours, adjust_color_by_latitude, water,
        altitude_scaling, wrinkly_maps, biome_maps,
    )

globe_params = build_globe_params(
        seed, "2000", "2000", zoom, "0", "0", grid, "m", 
        colourmap, shading, contours, adjust_color_by_latitude, water,
        altitude_scaling, wrinkly_maps, biome_maps,
    )



col6, col7, col8 = st.columns(3)
with col6:
    st.button("Make map", on_click=get_maps, args=([general_params, globe_params]))



try:
    if (projection == "Equirectangular"):
        st.image("equirectangular.bmp")
    else:
        st.image("flatmap.bmp")
except FileNotFoundError:
    st.text("Map is loading...")

try:
    display_globe("equirectangular.bmp")
except FileNotFoundError:
    st.text("Globe is loading...")



st.text("The map you are currently viewing was generated from the following parameters:")
with open("map.json", "r") as f:
    st.json(json.load(f))

with open("params.json", "r") as f:
    data = json.load(f)
    st.download_button("Download Parameters", json.dumps(data), file_name="map.json", mime="application/json")