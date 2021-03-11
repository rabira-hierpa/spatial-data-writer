# Import necessary modules first
import geopandas as gpd
from shapely.geometry import Point

# Create an empty geopandas GeoDataFrame

def read_shape_file(file_path):
    try:
        return gpd.read_file(file_path)
    except:
        return "Bad file path"

# Returns the distance between the two points
def get_distance_points(point1,point2):
    # code goes here
    pass

def main():
    print("Starting script...")
    # newdata = gpd.GeoDataFrame() # empty geodat frame
    gii_towns_path ="/home/eensat-client21/Desktop/Rabra/geopada-quickstart/Ethio_Towns-geojson.geojson"
    era_towns_path = "/home/eensat-client21/Desktop/Rabra/geopada-quickstart/Et_Towns-geojson.geojson"
    gii_towns = read_shape_file(gii_towns_path)
    era_towns = read_shape_file(era_towns_path)

    # print(gii_towns)
    # print(era_towns['NAME'],era_towns['POINT_X'],era_towns['POINT_Y'])
    for towns in era_towns.iterrows():
        print(towns)

if __name__ == '__main__':
    main()
