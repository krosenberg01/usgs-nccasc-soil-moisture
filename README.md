# usgs-nccasc-soil-moisture
Tool to examine soil moisture datasets for select Soil Climate Analysis Network soil moisture monitoring stations across the US.

## Purpose of this Code?
This repository contains a project in collaboration with the USGS and NC CASC regarding access to soil moisture datasets from various Soil Climate Analysis Network (SCAN; https://www.wcc.nrcs.usda.gov/scan/) stations across the US.  These stations are included in the broader national network of soil moisture monitoring stations: the National Soil Moisture Network (NSMN; http://nationalsoilmoisture.com/).

The notebook contained in this repository allows the user to download soil moisture datasets from an input URL an examine them on different timescales (Annual, Monthly, Daily).

## Goals and Motivation
In-Situ soil moisture data has not been widely incorporated into research and models because of the relative newness of its historical collection.  By creating an easy access tool to examine the data of different timescales, we hope to accomplish two things:

1) Publicly publish this tool so that access to in-situ soil moisture data on different timescales is readily available for environmental condition models (drought, flood, water management, etc.) and is available for use in research going forward.

2) Standardize soil moisture data summarized on a weekly (pentad/decad) timescale for use in comparison to standardized drought model values at each station location.  This can help attest to either the validity or weakness of current drought models that use remote-sensed soil moisture values as an input.

## Running this Workflow

### Overview of Workflow:
**Input**: 
* URL(s) to .csv files that contain soil moisture data from SCAN (http://nationalsoilmoisture.com/test/VWC_QAQC/scan/).
* Name of station associated with each url (Ex. Station 2006 = Bushland)

**Ouput**: 
Dataframes showing:
* All soil moisture (SM) data collected at that site over the period of record.
* Annual mean SM across period of record.
* Annual mean SM for a specific month across period of record.
* Monthly mean SM for any year on record.
* Monthly mean SM across all years over period of record.
* Daily mean SM for any year on record.
* Daily mean SM for any given day across period of record.

Plots showing:
* Annual mean soil moisture across period of record
* Monthly mean soil moisture for any year on record.
* Daily mean soil moisture for any year on record.

### Steps on How to Run This Workflow

**Packages needed to run this notebook:
    * x
    * y
    * z

1. Follow instructions provided by the Earth Lab at the University of Colorado, Boulder to download and install Bash, Git, and Minicoda to your computer (https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-git-bash-conda/).  Instructions vary based on operating system!

2. Create an earth-analytics directory on your computer.  This can be done by running the line **mkdir earth-analytics** in your terminal

3. Follow instructions provided by the Earth Lab at the University of Colorado, Boulder to install and activate an environment titled "earth-analytics-python" for use in running this notebook (https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-python-conda-earth-analytics-environment/).  This ensures that all needed imports and packages are available for use on your computer.

4. Ensure that the environment is activated before proceeding.  This is done by running the line **conda activate earth-analytics-python** in the terminal.

5. Update Scipy package to latest version.  This is done by running the line **pip install --user --upgrade scipy**

6. Run the line **jupyter notebook** to open the jupyter notebook program.

7. Navigate to the "earth-analytics" folder.

8. Click **New** in the toolbar and select **terminal**

9. In this new terminal, run the line **cd earth-analytics** to enter into your earth-analytics directory, and then run the line **git clone** followed by the url generated from cloning this repository.  This will place the full repository into your "earth-analytics" folder for use.  Now you are ready to begin running the notebook!

## Files Included in this Repository:
.gitignore = file detailing python files that we do not want git to track, notably automatically generated files such as .ipynb_checkpoints.

LICENSE = BSD-3 Clause license detailing legal use of this code.

README.md = ReadMe file detailing the purpose and use of this repository.

usgs-nccasc-soil-moisture = .ipynb Jupyter Notebook file containing code to download, import, and process SCAN soil moisture datasets.
