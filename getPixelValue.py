import rasterio

habitatDict = {
    0:"Other", 
    100:"Forest",
    200:"Savanna",
    300:"Shrubland",
    400:"Grassland",
    500:"Wetlands (inland)",
    600:"Rocky Areas",
    800:"Desert",
    900:"Marine - Neritic",
    1000:"Marine - Oceanic",
    1100:"Marine - Deep Ocean Floor",
    1200:"Marine - Intertidal",
    1400:"Artificial - Terrestrial"}


def getCoordinatePixel(map,lon,lat):
    # open map
    dataset = rasterio.open(map)
    # get pixel x+y of the coordinate
    py, px = dataset.index(lon, lat)
    # create 1x1px window of the pixel
    window = rasterio.windows.Window(px - 1//2, py - 1//2, 1, 1)
    # read rgb values of the window
    clip = dataset.read(window=window)
    return(clip[0][0][0])

map_dir = "./IUCN_habitat_2019_lvl1_1km.tif"
classification = getCoordinatePixel(map_dir, 151.20063699830578, -33.910642692510685)
habitat = habitatDict[classification]
print("done")
