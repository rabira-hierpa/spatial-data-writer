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
from os import listdir
from os.path import isfile, join
import glob
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
    updateTime = datetime.now()
    updateDate = updateTime.strftime("%A %d/%m/%Y @ %I:%M%p")
    fields.append(updateDate)
    with open(r'Data-Encoding-Status-CSV.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    print("Status updated for ",fields[0])

def write_to_custom_file(fileName,fields):
    updateTime = datetime.now()
    updateDate = updateTime.strftime("%A %d/%m/%Y @ %I:%M%p")
    fields.append(updateDate)
    with open(r"${fileName}", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    print("Status updated for ",fields[0])

def getFileInf(filePath):
    try:
        file_name = input("Enter file path: ")
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
        fileType = input("File type(CHA): ")
        if (fileType == ''): fileType = 'Controlled Hunted Area'
        
        typeOfData = input("Type of File(Vector)")
        if typeOfData == '':
            typeOfData='Vector'
        owner = 'Ethiopian Wildlife Conservation Agency'
        typeOfSurvey = 'From local database'

        # get geographical information
        geographicalCoverage = input("Geographical Coverage: (regional) ")
        if geographicalCoverage == '': geographicalCoverage = 'regional'
        
        # convert the timestamp in seconds to a datetime date format (Month-Date-Year)
        file_updatedOn = datetime.fromtimestamp(time_stamp).strftime("%m/%d/%Y") 
        print("File Last Modified On: " , file_updatedOn)
    
        # get spacial refernce number
        sref = input("Spacial Reference(32637): ")
        if (sref == ''): sref = 32637
        spacialReference = 'EPSG:' + str(sref)

        # get comments for the layer
        comments = input("Comments: ")

        updateRate = 'N/A'
        dataLicence = 'N/A'
        metaDataLink = 'N/A'
        linkToOCG = 'N/A'
        spatialDataTheme = ''    
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


def wirte_duplicate_file(filePath,comment):
    try:
        data_file = pathlib.Path(filePath)
        assert data_file.exists(), f'No such file: {data_file}'

        # get last modification date of the file
        time_stamp = data_file.stat().st_mtime
        
        layerPath = filePath.split('Rabra/')[1]
        print(layerPath)
        # get layer name
        # fileName_delimiter = input("File name delimiter: ")
        pathLayer = layerPath.split('/')
        final_layer_name = pathLayer[len(pathLayer) - 1]
        print(final_layer_name)

        # get layer discription 
        description = comment
        fileType = input("File type(CHA): ")
        if (fileType == ''): fileType = 'Controlled Hunted Area'
        
        typeOfData = input("Type of File(Vector)")
        if typeOfData == '':
            typeOfData='Vector'
        owner = 'Ethiopian Wildlife Conservation Agency'
        typeOfSurvey = 'From local database'

        # get geographical information
        geographicalCoverage = input("Geographical Coverage: (regional) ")
        if geographicalCoverage == '': geographicalCoverage = 'regional'
        
        # convert the timestamp in seconds to a datetime date format (Month-Date-Year)
        file_updatedOn = datetime.fromtimestamp(time_stamp).strftime("%m/%d/%Y") 
        print("File Last Modified On: " , file_updatedOn)
    
        # get spacial refernce number
        sref = input("Spacial Reference(32637): ")
        if (sref == ''): sref = 32637
        spacialReference = 'EPSG:' + str(sref)

        # get comments for the layer
        comments = comment

        updateRate = 'N/A'
        dataLicence = 'N/A'
        metaDataLink = 'N/A'
        linkToOCG = 'N/A'
        spatialDataTheme = ''    
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

# ==> Start here


def main():
    """
    starting point of the script
    """
    mypath='/home/eensat-client21/Desktop/Rabra/ECWA/EWCA_Protected_Areas/National Park_abiy/Awash/Awash_ArcMap/shapes/*.shp'
    # onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    # for files in onlyfiles:
    #     print(files)
    shapeFiles = glob.glob(mypath)
    for file in shapeFiles:
        wirte_duplicate_file(file,"DUPLICATE FILE found in Awash_ArchMap/Awash_ArchMap/shapes")

if __name__=="__main__":
    main()
