
def build_map_form_data(
    seed, width, height, zoom, center_lat, center_long, grid,
    projection, colourmap, shading, contours,
    adjust_color_by_latitude, water,
    altitude_scaling, wrinkly_maps, biome_maps,
):
    """Convert Streamlit widget values into the POST form data expected
    by https://topps.diku.dk/torbenm/maps.msp
    """

    projection_map = {
        "Mollweide": "M",
        "Mercator": "m",
        "Peters": "p",
        "Square": "q",
        "Stereographic": "s",
        "Orthographic": "o",
        "Gnomonic": "g",
        "Area Preserving Azimuthal": "a",
        "Conical": "c",
        "Icosahedral": "i",
        "Sinusoidal": "S",
        "Equirectangular": "m",  # site has no separate option; go with Mercator and convert it in a moment
    }

    colourmap_map = {
        "Olsson": "Olsson.col",
        "Olsson Light": "OlssonLight.col",
        "Olsson2": "Olsson2.col",
        "OlssonW": "OlssonW.col",
        "Mogensen": "default.col",
        "Mogensen black": "defaultB.col",
        "Bathymetric": "Bathymetric.col",
        "Burrows": "burrows.col",
        "Burrows black": "burrowsB.col",
        "Mars": "mars.col",
        "White": "white.col",
        "Yellow": "yellow.col",
        "Greyscale": "greyscale.col",
        "Black body radiation": "Blackbody.col",
        "Lefebvre": "Lefebvre.col",
        "Lefebvre2": "Lefebvre2.col",
        "uniform blue/green": "2col.col",
    }

    shading_map = {
        "None": "",
        "Bumpmap": " -B",
        "Bumpmap on land only": " -b",
        "Daylight": " -d -a 50",
    }

    contours_map = {
        "None": "",
        "Coastlines only": " -E ",
        "2 (land)": " -E2 ",
        "5 (land)": " -E5 ",
        "10 (land)": " -E10 ",
        "1 (coast)": " -E-1 ",
        "2 (coast)": " -E-2 ",
        "3 (coast)": " -E-3 ",
    }

    polar_map = {
        "No": "",
        "Yes": " -c ",
        "Yes, strongly": " -c -c ",
        "Yes, very strongly": " -c -c -c ",
    }


    form_data = {
        "seed": str(seed),
        "projection": projection_map[projection],
        "width": str(width),
        "height": str(height),
        "shading": shading_map[shading],
        "zoom": str(zoom),
        "lati": str(center_lat),
        "longi": str(center_long),
        "grid": str(grid),
        "colourmap": colourmap_map[colourmap],
        "outline": contours_map[contours],
        "polar": polar_map[adjust_color_by_latitude],
        "water": str(water),
        "what": "Make map",
    }

    # Checkboxes: only present (with their value) when checked
    if altitude_scaling:
        form_data["nonLinear"] = " -n "
    if wrinkly_maps:
        form_data["wrinkly"] = " -S "
    if biome_maps:
        form_data["biome"] = " -z "

    return form_data







def build_globe_params(
    seed, width, height, zoom, center_lat, center_long, grid,
    projection, colourmap, shading, contours,
    adjust_color_by_latitude, water,
    altitude_scaling, wrinkly_maps, biome_maps,
):
    """Convert Streamlit widget values into the POST form data expected
    by https://topps.diku.dk/torbenm/maps.msp
    """

    projection_map = {
        "Mollweide": "M",
        "Mercator": "m",
        "Peters": "p",
        "Square": "q",
        "Stereographic": "s",
        "Orthographic": "o",
        "Gnomonic": "g",
        "Area Preserving Azimuthal": "a",
        "Conical": "c",
        "Icosahedral": "i",
        "Sinusoidal": "S",
        "Equirectangular": "m",  # site has no separate option; go with Mercator and convert it in a moment
    }

    colourmap_map = {
        "Olsson": "Olsson.col",
        "Olsson Light": "OlssonLight.col",
        "Olsson2": "Olsson2.col",
        "OlssonW": "OlssonW.col",
        "Mogensen": "default.col",
        "Mogensen black": "defaultB.col",
        "Bathymetric": "Bathymetric.col",
        "Burrows": "burrows.col",
        "Burrows black": "burrowsB.col",
        "Mars": "mars.col",
        "White": "white.col",
        "Yellow": "yellow.col",
        "Greyscale": "greyscale.col",
        "Black body radiation": "Blackbody.col",
        "Lefebvre": "Lefebvre.col",
        "Lefebvre2": "Lefebvre2.col",
        "uniform blue/green": "2col.col",
    }

    shading_map = {
        "None": "",
        "Bumpmap": " -B",
        "Bumpmap on land only": " -b",
        "Daylight": " -d -a 50",
    }

    contours_map = {
        "None": "",
        "Coastlines only": " -E ",
        "2 (land)": " -E2 ",
        "5 (land)": " -E5 ",
        "10 (land)": " -E10 ",
        "1 (coast)": " -E-1 ",
        "2 (coast)": " -E-2 ",
        "3 (coast)": " -E-3 ",
    }

    polar_map = {
        "No": "",
        "Yes": " -c ",
        "Yes, strongly": " -c -c ",
        "Yes, very strongly": " -c -c -c ",
    }


    form_data = {
        "seed": str(seed),
        "projection": "m",  # Use Mercator for globe generation
        "width": "2000",  # Fixed max width for globe generation
        "height": "2000",  # Fixed max height for globe generation
        "shading": shading_map[shading],
        "zoom": '1',
        "lati": "",
        "longi": "",
        "grid": str(grid),
        "colourmap": colourmap_map[colourmap],
        "outline": contours_map[contours],
        "polar": polar_map[adjust_color_by_latitude],
        "water": str(water),
        "what": "Make map",
    }



    # Checkboxes: only present (with their value) when checked
    if altitude_scaling:
        form_data["nonLinear"] = " -n "
    if wrinkly_maps:
        form_data["wrinkly"] = " -S "
    if biome_maps:
        form_data["biome"] = " -z "

    return form_data