import os
from matplotlib import pyplot as plt
import mplleaflet
from  PIL import Image
from scipy.io import loadmat



def display_coordinates(array): #scatter plot to show pricing range and population by location
    lons = array[:, 1:2]
    lats = array[:, 0:1]
    score = array[:, 2:3]

    cmap = plt.cm.get_cmap("jet")
    plt.scatter(x=lons, y=lats, c=score, cmap=cmap)

    mapfile = 'map.html' # save file
    mplleaflet.show(path=mapfile)

def get_coordinates(loacetion):
    coordinates = loadmat('GPS_Long_Lat_Compass.mat')
    if loacetion == 'Pittsburgh':
        coordinates = coordinates['GPS_Compass'][:3077,:2]
    elif loacetion == 'Orlando':
        coordinates = coordinates['GPS_Compass'][3077:4401, :2]
    elif loacetion == 'Manhatten':
        coordinates = coordinates['GPS_Compass'][4401:, :2]
    return coordinates



def display_image(path,images):
    for image in images:
        im = Image.open(os.path.join(path, image))
        im.show()



















