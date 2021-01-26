#!/usr/bin/python3

# Data Fetcher
# A simple script to get shape file info and write to a csv file
# written by rabra
# date Jan 16,2021
# updated on Jan 26,2021

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


written_files = []  

def print_final_info(fields,layerPath):
    for field in fields:
        print(field)
    print(layerPath," is now wirtten!")

# Write file encoding status to 
# Data-Encoding-Status.csv file
def write_status_to_file(fields):
    updateTime = datetime.now()
    updateDate = updateTime.strftime("%A %d/%m/%Y @ %I:%M%p")
    fields.append(updateDate)
    with open(r'Data-Encoding-Status-CSV.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    print("Status updated for ",fields[0])

# Writes file encoding status of
# PDF,JPG and PNG files to PDF-File-Status.csv
def write_to_custom_file(fields):
    updateTime = datetime.now()
    updateDate = updateTime.strftime("%A %d/%m/%Y @ %I:%M%p")
    fields.append(updateDate)
    with open(r"PDF_Files_status.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    print("Status updated for ",fields[0])

# Get relative path of a file and its name
# @returns file name and relative path of file from 'Rabra' directory
def getFileNamePath(filePath):
    data_file = pathlib.Path(filePath)
    assert data_file.exists(), f'No such file: {data_file}'
    # get layer PATH RELATIVE ONLY
    layerPath = filePath.split('Rabra/')[1]
    # get layer name
    pathLayer = layerPath.split('/')
    final_layer_name = pathLayer[len(pathLayer) - 1]
    return (final_layer_name,layerPath)

# Get file information and write to 
# two csv files
def getFileInfo(filePath):
    try:
        absolute_file_path = getFileNamePath(filePath)
        final_layer_name = absolute_file_path[0]
        layerPath = absolute_file_path[1]
        print("File name: ",final_layer_name)
        print("Relative Path: \n",layerPath)
        if final_layer_name in written_files:
            return (print("File already written!!"))

        data_file = pathlib.Path(filePath)
        # get last modification date of the file
        time_stamp = data_file.stat().st_mtime
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
        # wirte to shape rows files
        write_status_to_file(status_fields)
    except:
        print("Unable to locate file! Please try again.")
        quit()

# Write INVALID/NON SPECIFIED info to a file
def getNonSpecifiedFileInfo(filePath):
    status = 'NOT AVAILABLE'
    try:
        absolute_file_path = getFileNamePath(filePath)
        final_layer_name = absolute_file_path[0]
        layerPath = absolute_file_path[1]
        print("File name: ",final_layer_name)
        print("Relative Path: \n",layerPath)

        data_file = pathlib.Path(filePath)
        # get last modification date of the file
        time_stamp = data_file.stat().st_mtime
        # get layer discription 
        description = status
        fileType = status        
        typeOfData = status
        owner = 'Ethiopian Wildlife Conservation Agency'
        typeOfSurvey = 'From local database'

        # get geographical information
        geographicalCoverage = status
        
        # convert the timestamp in seconds to a datetime date format (Month-Date-Year)
        file_updatedOn = datetime.fromtimestamp(time_stamp).strftime("%m/%d/%Y") 
        print("File Last Modified On: " , file_updatedOn)
    
        # get spacial refernce number
        spacialReference = status

        # get comments for the layer
        comments = status
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
        status_fields = [fileName_identifier,layerPath,fileType,owner,"Incomplete!"]

        # Print Info messages
        print_final_info(fields,layerPath)
        write_status_to_file(status_fields)
    except:
        print("Unable to locate file! Please try again.")
        quit()

# Write duplicate status of file
def wirte_duplicate_file(filePath,comment):
    try:
        data_file = pathlib.Path(filePath)
        assert data_file.exists(), f'No such file: {data_file}'

        # get last modification date of the file
        time_stamp = data_file.stat().st_mtime
        
        layerPath = filePath.split('Rabra/')[1]
        print(layerPath)

        # get layer name
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

# recursively write duplicate file status
def write_duplicate_status(paths,error_message):
    shapeFiles = glob.glob(paths)
    for file in shapeFiles:
        wirte_duplicate_file(file,error_message)

def write_non_spatail_file_status(paths,file_ext):
    filePaths = paths + '*.' + file_ext
    pdfFiles = glob.glob(filePaths,recursive=True)
    # status_fields = [fileName_identifier,layerPath,fileType,owner,"Done"]
    fileType = "Parks and Protected Areas"
    owner="Ethiopian Wildlife Conservation Agency"
    
    for file in pdfFiles:
        filePathInfo = getFileNamePath(file)
        fileName_identifier = filePathInfo[0]
        fileName_path = filePathInfo[1]
        print(fileName_identifier)
        print(fileName_path)
        status_fields=[fileName_identifier,fileName_path,fileType,owner,file_ext,"Done"]
        write_to_custom_file(status_fields)

def write_spatial_file_status(paths):
    shpFiles = glob.glob(paths,recursive=True)
    total = len(shpFiles)
    count = 0
    for shapeFile in shpFiles:
        print("Fetching Info for :")
        print(shapeFile)
        getFileInfo(shapeFile)
        count = count + 1
        progress = (count/total) * 100
        result = round(progress,2)
        print("Progress:  " + str(count) + "/" + str(total) + "(" + str(result) + "%)" + " completed" )

def write_non_descirptive_files(paths):
    shpFiles = glob.glob(paths,recursive=True)
    total = len(shpFiles)
    count = 0
    for shapeFile in shpFiles:
        print("Fetching Info for :")
        print(shapeFile)
        getNonSpecifiedFileInfo(shapeFile)
        count = count + 1
        progress = (count/total) * 100
        result = round(progress,2)
        print("Progress:  " + str(count) + "/" + str(total) + "(" + str(result) + "%)" + " completed" )


# ==> Start here

def main():
    """
    starting point of the script
    """

    # opens written file status and get the list of files
    # that are already encoded (shp files only)
    with open("shape_rows.csv",'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            written_files.append(row[0])

    written_files.pop(0)
    
    mypath='/home/eensat-client21/Desktop/Rabra/ECWA/EWCA_Protected_Areas/National Park_abiy/Gambella/**/*.shp'
    
    #nonDescriptiveFiles = '/home/eensat-client21/Desktop/Rabra/ECWA/EWCA_Protected_Areas/National Park_abiy/Gambella/GAMBELLAsurveys/Gambella_2009/Shapes/10km/*.shp'

    # write_non_spatail_file_status(mypath,'jpeg')
    # write_non_descirptive_files(nonDescriptiveFiles)
    write_spatial_file_status(mypath)


if __name__=="__main__":
    main()

    
