# Import necessary modules first
import geopandas as gpd
from pyproj import crs
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

    # for era_town in era_towns.iterrows():
    #     era_point_town = era_town[1][15][0]
    #     for gii_town in gii_towns.iterrows():
    #         gii_point_town = gii_town[1][22]
    #         points_df = gpd.GeoDataFrame({'geometry': [era_point_town, gii_point_town]}, crs='EPSG:4326')
    #         points_df2 = points_df.shift() 
    #         print(points_df.distance(points_df2))
    point1,point2 = None,None
    for era_town in era_towns.iterrows():
        if (era_town[1][2] == 'Mezezo'):
            era_point = era_town[1][15][0]
            print(era_town[1][2])
    for gii_town in gii_towns.iterrows():
        if (gii_town[1][3] == 'Mezezo'):
            gii_point = gii_town[1][22]

    points_df = gpd.GeoDataFrame({'geometry':[era_point,gii_point]},crs='EPSG:4326')
    points_df2 = points_df.shift()
    print(points_df.distance(points_df2))

if __name__ == '__main__':
    main()
