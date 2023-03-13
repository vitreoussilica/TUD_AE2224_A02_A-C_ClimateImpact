from os import listdir
from os.path import isfile, join

## The function below generates all filenames in the given directory.
## Use it by calling the function with the path to the full_data folder as input.
## The file structure of the full_data folder must then be as follows:
## Full_data contains two folders: DT00 and DT12.
## These folders contain ALL raw files from the dataset and are NOT subdivided in different folders for the different solutions.
def all_filenames(path_to_full_data: str, model: str):
    filepaths = []

    for f in listdir(path_to_full_data + '/DT00'):
        if isfile(join(path_to_full_data + '/DT00', f)) and f[(f.find('_0000_'))+6::] == model:
            filepaths.append(path_to_full_data + '/DT00/' + f)

    for f in listdir(path_to_full_data + '/DT12'):
        if isfile(join(path_to_full_data + '/DT12', f)) and f[(f.find('_0000_'))+6::] == model:
            filepaths.append(path_to_full_data + '/DT12/' + f)

    return filepaths

def all_filenames_DT00(path_to_full_data: str, model: str):
    filepaths = []

    for f in listdir(path_to_full_data + '/DT00'):
        if isfile(join(path_to_full_data + '/DT00', f)) and f[(f.find('_0000_'))+6::] == model:
            filepaths.append(path_to_full_data + '/DT00/' + f)

    return filepaths

def all_filenames_DT12(path_to_full_data: str, model: str):
    filepaths = []

    for f in listdir(path_to_full_data + '/DT12'):
        if isfile(join(path_to_full_data + '/DT12', f)) and f[(f.find('_0000_'))+6::] == model:
            filepaths.append(path_to_full_data + '/DT12/' + f)

    return filepaths


## ------------------------------------------------------------
## Retrieve all airtraf_ac file names
def all_filenames_airtraf_ac(path_to_full_data: str):
    return all_filenames(path_to_full_data, 'airtraf_ac.nc')

## Retrieve all airtraf_ac file names for DT00
def all_filenames_airtraf_ac_DT00(path_to_full_data: str):  
    return all_filenames_DT00(path_to_full_data, 'airtraf_ac.nc')

## Retrieve all airtraf_ac file names for DT12
def all_filenames_airtraf_ac_DT12(path_to_full_data: str):
    return all_filenames_DT12(path_to_full_data, 'airtraf_ac.nc')
## ------------------------------------------------------------


## ------------------------------------------------------------
## Retrieve all aitraf_gp file names
def all_filenames_airtraf_gp(path_to_full_data: str):
    return all_filenames(path_to_full_data, 'airtraf_gp.nc')

## Retrieve all aitraf_gp file names for DT00
def all_filenames_airtraf_gp_DT00(path_to_full_data: str):
    return all_filenames_DT00(path_to_full_data, 'airtraf_gp.nc')

## Retrieve all aitraf_gp file names for DT12
def all_filenames_airtraf_gp_DT12(path_to_full_data: str):
    return all_filenames_DT12(path_to_full_data, 'airtraf_gp.nc')
## ------------------------------------------------------------