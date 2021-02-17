#!/usr/bin/python3

''' 
A script to merge non-spaital population data to 
a spatial one
Written by Rabra Hierpa(@rabira-hierpa)

DESCRIPTION 
========

spatail_data[6] = region
spatail_data[3] = towns

non_spatial_data[6] = region
non_spatial_data[3] = towns

'''

import sys
import csv   
import pathlib
import glob
import re

def read_pop_file(file_path):
    town_name = []
    with open(file_path,'r') as pop:
            pop_reader = csv.reader(pop,delimiter=',')
            for row in pop_reader:
                row[2] = row[2].lstrip()
                town_name.append(row[3].split('-Town')[0])
            town_name.pop(0) # removes 'TOWN' header
            town_name.sort() # sort alphabetically
            town_names=tuple(town_name)
    pop.close()
    return town_names

def match_towns(csv_file,town_name):
    csv_file_path = csv_file
    region = str(sys.argv[1]).upper() # sets region from the cli
    file_handler = open(csv_file_path,'r')
    spatial_towns = csv.reader(file_handler,delimiter=',')
    pop_towns = read_pop_file('./pop/ethio-pop-2020.csv')
    non_spatial_len = len(pop_towns)
    total_match = 0
    # region_towns = []
    spatial_len = 0

    for row in spatial_towns:
        for town in pop_towns:
            # row[3] is town name
            if row[3].upper() == town.upper() and row[6].split(' ')[0].upper() == region:
                #print(row[3:11])
                total_match +=1
        spatial_len +=1
    spatial_region_towns_total = sum([1 for x in csv.DictReader(open(csv_file_path)) if x['REGION'].split(' ')[0].upper() == region])

    match_percentage = round((total_match/spatial_region_towns_total) * 100,2)
    print("Total Towns in Spatial Data: {} ".format(spatial_len-1)) # exclude the top header for the csv file
    print("Total Towns in Non Spatial Data: {}".format(non_spatial_len-1)) # exclude the top header of the csv file
    print("Total Towns in {} : {}".format(region,spatial_region_towns_total))
    print("Total Matched towns in {}: {} ({} %)".format(region,total_match,match_percentage))
    mismatch = spatial_region_towns_total - total_match
    mismatch_percentage = round((mismatch/spatial_region_towns_total) * 100,2)
    print("Mismatch: {} ({} %)".format(mismatch,mismatch_percentage))
    file_handler.close()

def Diff(li1, li2):
        return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

def read_csv_file(file_path):
    try:
        file_handler = open(file_path,'r')
        csvfile = csv.reader(file_handler,delimiter=',')
        return csvfile
    except:
        print("Unable to read file!")

def check_town_names(file1,file2):
    file_handler1 = open(file1,'r')
    file_handler2 = open(file2,'r')
    spatial_towns = csv.reader(file_handler1,delimiter=',')
    non_spatial_towns = csv.reader(file_handler2,delimiter=',')
    
    spatial_unique_Towns,non_spatial_unique_towns = set() , set()

    for towns in spatial_towns:
        spatial_unique_Towns.add(towns[3])

    for towns in non_spatial_towns:
        non_spatial_unique_towns.add(towns[3].split('-Town')[0])

    diff_towns = Diff(spatial_unique_Towns,non_spatial_unique_towns)
    print(len(diff_towns))


    # print("All unique spatial towns: ",spatial_unique_Towns)
    # print("All unique spatial towns: ",non_spatial_unique_towns)

    print("Total unique spatial-towns: ", len(spatial_unique_Towns))
    print("Total unique non-spatial towns: ",len(non_spatial_unique_towns))

def write_csv_file(fields,alphabet,all=False):
    if all:
        file_name = 'ALL_Town_names_comparison.csv'
    else:
        file_name = str(alphabet).upper() + '_Town_names_comparison.csv'

    with open(f"./toponyms_eth_towns/{file_name}", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    print("Status updated for ",fields[0])

def filter_town_by_alphabet(file1,file2,file3,alphabet):
    spatial_town = read_csv_file(file1)
    non_spatial_data = read_csv_file(file2)
    era_towns = read_csv_file(file3)

    spaital_total,non_spatial_total,era_total = 0,0,0
    filtered_spatial_towns,filtered_non_spatial_tonws,era_town_list = [],[],[]

    search_string = f'^{alphabet}\S*'
    # print("\n\nSPATIAL TOWN NAMES\n\n")
    for town1 in spatial_town:
        if re.search(search_string,town1[3],re.IGNORECASE):
            filtered_spatial_towns.append(town1[3])
            spaital_total +=1
    filtered_spatial_towns.sort()
    # [print(town) for town in filtered_spatial_towns]
    
    # print("\n\nNON-SPATIAL TOWN NAMES\n\n")

    for town2 in non_spatial_data:
        town_name = town2[3].split('-Town')[0]
        if re.search(search_string,town_name,re.IGNORECASE):
            filtered_non_spatial_tonws.append(town_name)
            non_spatial_total += 1

    filtered_non_spatial_tonws.sort()

    for town3 in era_towns:
        if re.search(search_string,town3[2],re.IGNORECASE):
            era_town_list.append(town3[2])
            era_total +=1

    era_town_list.sort()
    # [print(town) for town in filtered_non_spatial_tonws]

    # Join two lists as a pair using lists
    # Pair the town names of the spaital with the non-spatial
    # [write_csv_file([i,j],alphabet) for i,j in zip(filtered_spatial_towns, filtered_non_spatial_tonws)]

    for idx,towns in enumerate(era_town_list,start=0):         
        try:
            write_csv_file([filtered_spatial_towns[idx],filtered_non_spatial_tonws[idx],towns],alphabet,True)
        except:
            try:
                write_csv_file(["",filtered_non_spatial_tonws[idx],towns],alphabet,True)
            except:
                write_csv_file(["","",towns],alphabet,True)

    print("Total Spatial towns that starts with " + alphabet + ": ", spaital_total)
    print("Total Non Spatial towns that starts with " + alphabet + ": ", non_spatial_total)



def main():
    print("Starting Merge Population ...")
    spatial_data = '/home/eensat-client21/Desktop/Rabra/GII/eth_towns/ethio-towns-csv.csv'
    non_spatial_data = './pop/ethio-pop-2020.csv'
    era_towns = './Eth_Road_Auth/Admin_shape_files/eth_towns_era.csv'
    # match_towns(file_path,sys.argv[1]) # pass the region argument to the match_towns function
    # check_town_names(spatial_data,non_spatial_data)
    # search_alphabet = sys.argv[1]
    characters = 'abcdefijklmnopqrstuvwxyz'
    for char in characters:
        filter_town_by_alphabet(spatial_data,non_spatial_data,era_towns,char)

if __name__ == '__main__':
    main()

