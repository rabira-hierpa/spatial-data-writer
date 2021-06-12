# Import necessary modules first
import pandas as pd
import geopandas as gpd
from pyproj import crs
from shapely.geometry import Polygon, Point, MultiPoint
import re
import csv   

# Create an empty geopandas GeoDataFrame

def read_shape_file(file_path):
    try:
        return gpd.read_file(file_path)
    except:
        return "Bad file path"
# Returns the distance between the two points

def write_csv_file(fields,name):
    file_name= str(name) + '_all_towns.csv'
    with open(f"{file_name}", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    print(file_name, ' Towns Saved!!!--------------------')

def get_distance_points(era_point, gii_point):
    points_df = gpd.GeoDataFrame({'geometry':[era_point,gii_point]},crs='EPSG:3857')
    points_df2 = points_df.shift()
    distance = points_df.distance(points_df2).min()
    print("DISTANCE =",distance)
    # if (distance < 10):

def get_distance_for_all_points(era_towns,gii_towns):
    all_era_towns,all_gii_towns = [],[]
    for era_town in era_towns.iterrows():
        all_era_towns.append(era_town[1][3])
        # print(era_town[1][2]) # ERA town name
    write_csv_file(all_era_towns,'era');
    for gii_town in gii_towns.iterrows():
        all_gii_towns.append(gii_town[1][22]);
    write_csv_file(all_gii_towns,'gii')

        # print(gii_town[1][22]) # GII town name
        # gii_point = gii_town[1][22] # GII Town point
    # for towns in range(1,1359):
    #         # if (gii_town[1][3] == 'Mezezo'):

    for era_town,gii_town in zip(era_towns.iterrows(),gii_towns.iterrows()):
        matched_towns = []
        search_gii_town = re.search(gii_town[1][3],str(all_era_towns),re.IGNORECASE)
        if(search_gii_town):
            matched_towns.append(search_gii_town)
            print(search_gii_town)
        # if (era_town[1][2] == 'Morka' or gii_town[1][3] == 'Morka'):
        #     print("ERA ", era_town[1][2], "\nGII " , gii_town[1][3])
        #     get_distance_points(era_town[1][15][0],gii_town[1][22])


def main():
    print("Starting script...")
    # newdata = gpd.GeoDataFrame() # empty geodat frame
    gii_towns_path = "/home/eensat-client21/Desktop/Rabra/geopada-quickstart/Ethio_Towns-geojson.geojson"
    era_towns_path = "/home/eensat-client21/Desktop/Rabra/geopada-quickstart/Et_Towns-geojson.geojson"
    gii_towns = read_shape_file(gii_towns_path)
    era_towns = read_shape_file(era_towns_path)
    
    # convert to a meter projection
    gii_towns.to_crs(epsg=3857, inplace=True)
    era_towns.to_crs(epsg=3857, inplace=True)

    get_distance_for_all_points(era_towns,gii_towns)
    # GiiMulti = gpd.GeoSeries(gii_towns.unary_union)
    # GiiMulti.crs = GiiMulti.crs
    # GiiMulti.reset_index(drop=True)

    # gii_towns.geometry.apply(lambda x: era_towns.distance(x).min())
    # print(GiiMulti)

    # for era_town in era_towns.iterrows():
    #     era_point_town = era_town[1][15][0]
    #     for gii_town in gii_towns.iterrows():
    #         gii_point_town = gii_town[1][22]
    #         points_df = gpd.GeoDataFrame({'geometry': [era_point_town, gii_point_town]}, crs='EPSG:3857')
    #         points_df2 = points_df.shift()
    #         print(points_df.distance(points_df2))
    

if __name__ == '__main__':
    main()
