#!/usr/bin/python3

''' A script to merge non-spaital population data to 
    a spatial one
    # Written by Rabra Hierpa(@rabira-hierpa)
'''

import sys
import csv   
import pathlib
import glob

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
    return town_names

def main():
    print("Starting Merge Population ...")
    csv_file_path = '/home/eensat-client21/Desktop/Rabra/GII/eth_towns/ethio-towns-csv.csv'
    _total = 0
    _region = 'TIGRAY'
    _region_tonws = []
    _row_counter = 0
    towns = read_pop_file('./pop/trigray-pop-2020.csv')
    with open(csv_file_path,'r') as file:
        csv_reader = csv.reader(file,delimiter=',')
        for row in csv_reader:
            for town in towns:
                # row[3] is region name
                if row[3].upper() == town.upper() and row[6] == _region:
                    print(row[3:11])
                    _total +=1

    print("Total Matched towns in " + _region + " is: " + str(_total) )
    mismatch = len(csv_reader) - _total
    print("Mismatch: " + str(mismatch))

if __name__ == '__main__':
    main()

