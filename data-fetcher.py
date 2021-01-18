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


# Fields 
# updateRate = ''
# dataLicence = ''
# metaDataLink = ''
# linkToOCG = ''
# spatialDataTheme = ''
# spatialAccuracy = ''

def print_final_info(fields,layerPath):
    for field in fields:
        print(field)
    print(layerPath," is now wirtten!")

def write_status_to_file(fields):
    with open(r'Data-Encoding-Status-CSV.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    print("Status updated for ",fields[0])

# ==> Start here
file_name = input("Enter file path: ")


try:
    data_file = pathlib.Path(file_name)
    assert data_file.exists(), f'No such file: {data_file}'

    # get last modification date of the file
    time_stamp = data_file.stat().st_mtime
    
    layerPath = file_name.split('Rabra/')[1]
    print(layerPath)
    # get layer name
    # fileName_delimiter = input("File name delimiter: ")
    pathLayer = layerPath.split('/')
    final_layer_name = pathLayer[len(pathLayer) - 1]
    print(final_layer_name)

    # get layer discription 
    description = input("File description:")
    fileType = input("File type: ")
    
    typeOfData = 'Vector'
    owner = 'Ethiopian Wildlife Conservation Agency'
    typeOfSurvey = 'From local database'

    # get geographical information
    geographicalCoverage = input("Geographical Coverage: ")
    # convert the timestamp in seconds to a datetime date format (Month-Date-Year)
    file_updatedOn = datetime.fromtimestamp(time_stamp).strftime("%m/%d/%Y") 
    print("File Last Modified On: " , file_updatedOn)
   
    # get spacial refernce number
    spacialReference = input("Spacial Reference(numbers only): ")
    spacialReference = 'EPSG:' + spacialReference
    comments = input("Comments: ")
    updateRate = 'N/A'
    dataLicence = 'N/A'
    metaDataLink = 'N/A'
    linkToOCG = 'N/A'
    spatialDataTheme = 'N/A'    
    spatialAccuracy = 'N/A'
    category = 'BASIC'
    fileName_identifier = final_layer_name
    

    # Write to csv file
    fields=[fileName_identifier,description,typeOfData,owner,typeOfSurvey,geographicalCoverage,file_updatedOn,updateRate,dataLicence,metaDataLink,linkToOCG,spacialReference,spatialAccuracy,comments,fileName_identifier,category,spatialDataTheme]
    with open(r'shape_rows.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    status_fields = [fileName_identifier,layerPath,fileType,owner,"Done"]

    # Print Info messages
    print_final_info(fields,layerPath)
    write_status_to_file(status_fields)

except:
    print("Unable to locate file! Please try again.")
    quit()

