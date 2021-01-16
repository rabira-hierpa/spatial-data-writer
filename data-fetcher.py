#!/usr/bin/python3
# Data Fetcher
# A simple script to get shape file info and write to a csv file
# written by rabra
# date Jan 16,2021

import sys
import csv   
import pathlib
from osgeo import ogr
from datetime import datetime

file_name = input("Enter file path:")
try:
    data_file = pathlib.Path(file_name)
    assert data_file.exists(), f'No such file: {data_file}'
    # get last modification date of the file
    time_stamp = data_file.stat().st_mtime
    # convert the timestamp in seconds to a datetime date format (Month-Date-Year)
    layerName = file_name.split('Rabra/')[1]
    print(layerName)
    description = input("File description:")
    typeOfData = 'Vector'
    owner = 'Ethiopian Wildlife Conservation Agency'
    typeOfSurvey = 'From local data'
    geographicalCoverage = input("Geographical Coverage ")
    file_updatedOn = datetime.fromtimestamp(time_stamp).strftime("%m/%d/%Y") 
    print("File Last Modified On" , file_updatedOn)
    updateRate = 'N/A'
    dataLicence = 'N/A'
    metaLink = 'N/A'
    linkToOCG = 'N/A'
    spacialReference = input("Spacial Reference(numbers only)")
    spacialReference = 'EPSG:' + spacialReference
    comments = input("Comments:")
    category = 'BASIC'
    spatialDataTheme = 'N/A'

    fields=[layerName,description,typeOfData,owner,typeOfSurvey,geographicalCoverage,file_updatedOn,updateRate,dataLicence,metaLink,linkToOCG,spacialReference,comments,category,spatialDataTheme]
    with open(r'shape_rows.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    print(layerName, " is now written!")

except:
    print("Unable to locate file! Please try again.")
    quit()
