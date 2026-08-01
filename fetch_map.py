import requests
from time import sleep
from mercator2equirectangular import mercator_to_equirectangular


# params = {
#     "seed": "1111111",
#     "projection": "M",
#     "width": "500",
#     "colourmap": "Olsson.col",
#     "height": "250",
#     "shading": "",
#     "zoom": "1",
#     "outline": "",
#     "lati": "",
#     "polar": "",
#     "longi": "",
#     "water": "-0.02",
#     "grid": "none",
#     "what": "Make map"
# }



def get_bitmap(params, output_filename): 
    session = requests.Session()

    request_map_regen = session.post("https://topps.diku.dk/torbenm/maps.msp",data=params)
    get_img_response = session.get(f"https://topps.diku.dk/torbenm/Maps/Map-{params["seed"][-3:]}.bmp")


    request_map_regen.raise_for_status()
    sleep(1)
    get_img_response.raise_for_status()


    with open(output_filename, "wb") as f:
        f.write(get_img_response.content)




def get_maps(general_params, globe_params):
    """Get both the map and the globe images from the TorbenM website."""
    # Get the map image
    get_bitmap(general_params, "flatmap.bmp")
    # Get the globe image
    sleep(4)  # Wait for the map to be generated before trying to display it
    get_bitmap(globe_params, "maxmercator.bmp")
    mercator_to_equirectangular("maxmercator.bmp", "equirectangular.bmp")