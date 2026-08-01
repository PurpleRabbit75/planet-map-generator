import streamlit as st
from time import sleep
from fetch_map import get_maps
from parse_args import build_map_form_data, build_globe_params

st.title("Planet Map Generator")
st.write(
    "This website is based on https://topps.diku.dk/torbenm/maps.msp"
)


col1, col2 = st.columns(2)

with col1:
    seed = st.number_input("Seed", value=1111111)
    width = st.number_input("Width (max 2000):", value=500)
    height = st.number_input("Height (max 2000):", value=250)
    zoom = st.number_input("Zoom (0.1 to 10000):", value=1)
    center_lat = st.number_input("Center Latitude (-90 to 90):", value=0.0)
    center_long = st.number_input("Center Longitude (-360 to 360):", value=0.0)
    grid = st.text_input("Grid (non or 1 to 90)", value="none")

with col2:
    projection = st.selectbox("Projection", options=["Mollweide", "Mercator", "Peters", "Square", "Stereographic", "Orthographic", "Gnomonic", "Area Preserving Azimuthal", "Conical", "Icosahedral", "Sinusoidal", "Equirectangular"])
    colourmap = st.selectbox("Colourmap", options=["Olsson", "Olsson Light", "Olsson2", "OlssonW", "Mogensen", "Mogensen black", "Bathymetric", "Burrows", "Burrows black", "Mars", "White", "Yellow", "Greyscale", "Black body radiation", "Lefebvre", "Lefebvre2", "uniform blue/green"])
    shading = st.selectbox("Shading", options=["None", "Bumpmap", "Bumpmap on land only", "Daylight"])
    st.space(size="xxsmall")
    contours = st.radio("Contour lines", options=["None", "Coastlines only", "2 (land)", "5 (land)", "10 (land)", "1 (coast)", "2 (coast)", "3 (coast)"], horizontal = True)
    st.space(size="xxsmall")
    adjust_color_by_latitude = st.radio("Adjust Color by Latitude", options=["No", "Yes", "Yes, strongly", "Yes, very strongly"], horizontal = True)
    water = st.number_input("Water line (-0.1 to 0.1):", value=-0.02)

col3, col4, col5 = st.columns(3, border=True)
with col3:
    altitude_scaling = st.checkbox("Non-linear altitude scaling")
with col4:
    wrinkly_maps = st.checkbox('Make more "wrinkly" maps')
with col5:
    biome_maps = st.checkbox("Make biome maps")




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


# sleep(3)  # Wait for the map to be generated before trying to display it
st.image("flatmap.bmp")
# st.image("maxmercator.bmp")


