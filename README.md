# usgs-nccasc-soil-moisture
Automated tool (Jupyter Notebook) to examine soil moisture datasets for Soil Climate Analysis Network (SCAN) soil moisture monitoring stations across the US.

## Research Collaborators:
* **Imtiaz Rangwala, Ph.D.** Research Scientist, CIRES/Western Water Assessment, University of Colorado-Boulder; Climate Scientist Lead, North Central Climate Adaptation Science Center.  https://cires.colorado.edu/researcher/imtiaz-rangwala

* **Gabriel Senay, Ph.D., P.E.** Research Physical Scientist, U.S. Geological Survey Earth Resources Observation & Science Center/ North Central Climate Adaptation Science Center and Faculty Affiliate with Ecosystem Science and Sustainability.  https://www.usgs.gov/staff-profiles/gabriel-senay

* **Jenny Palomino, Ph.D.** Curriculum Developer & Instructor, University of Colorado-Boulder, Earth Lab. https://www.colorado.edu/earthlab/people/jenny-palomino

* **Leah Wasser, Ph.D.** Earth Analytics Education Initiative Director, University of Colorado-Boulder, Earth Lab. https://www.colorado.edu/earthlab/people/leah-wasser

## Purpose of this Code?
This repository contains a project in collaboration with researchers from the U.S. Geological Survey and the North Central Climate Adaptation Science Center regarding access to soil moisture datasets from various Soil Climate Analysis Network (SCAN; https://www.wcc.nrcs.usda.gov/scan/) stations across the US.  These stations are included in the broader national network of soil moisture monitoring stations: the National Soil Moisture Network (NSMN; http://nationalsoilmoisture.com/).

The notebook contained in this repository allows the user to download soil moisture datasets from an input URL an examine them on different timescales (Annual, Monthly, Daily, Weekly).  Outputs include CSV files for Annual/Monthly/Daily/Weekly mean values and Z-Score analysis values for each in addition to plots for all of the above.

## Goals and Motivation
In-Situ soil moisture data has not been widely incorporated into research and models because of the relative newness of its historical collection.  By creating an easy access tool to examine the data of different timescales, we hope to accomplish two things:

1) Publicly publish this tool so that access to in-situ soil moisture data on different timescales is readily available for environmental condition models (drought, flood, water management, etc.) and is available for use in research going forward.

2) Standardize soil moisture data summarized on any timescale for use in comparison to standardized drought index values at each SCAN station location.  This can help attest to either the validity or weakness of current drought models that use remote-sensed soil moisture values as an input.

## Running this Workflow

### Overview of Workflow:
#### Input: 
* URL(s) to .csv files that contain soil moisture data from SCAN (http://nationalsoilmoisture.com/test/VWC_QAQC/scan/).
* Name of station associated with each url (Ex. Station 2006 = Bushland #2006)

#### Output:
**Dataframes showing:**
* All raw soil moisture data collected at that site over the period of record.
* Annual mean soil moisture across period of record.
* Month of Year mean soil moisture for complete historical record.
* Monthly mean soil moisture for any year on record.
* Monthly mean soil moisture across all years over period of record.
* Daily mean soil moisture for any year on record.
* Z-Score standardized dataframes for each of the above

**Plots showing:**
* Annual mean soil moisture across period of record
* Monthly mean soil moisture for any year on record.
* Daily mean soil moisture for any year on record.
* Weekly mean soil moisture
* Z-Score standardized plots for each of the above

### Steps on How to Run This Workflow

**A GitHub Account is required to run this workflow correctly**

**Packages needed to run this notebook:**
* os
* matplotlib
* pandas
* earthpy
* numpy
* scipy
* seaborn
* warnings

**Follow the below instructions to use Earth Lab's custom environment that contains all needed packages:**

1. Follow instructions provided by the Earth Lab at the University of Colorado, Boulder to download and install Bash, Git, and Minicoda to your computer (https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-git-bash-conda/).  Instructions vary based on operating system!

2. Create an earth-analytics directory on your computer.  This can be done by running the line **mkdir earth-analytics** in your terminal

3. Follow instructions provided by the Earth Lab at the University of Colorado, Boulder to install and activate an environment titled "earth-analytics-python" for use in running this notebook (https://www.earthdatascience.org/workshops/setup-earth-analytics-python/setup-python-conda-earth-analytics-environment/).  This ensures that all needed imports and packages are available for use on your computer.

4. Fork this repository to your personal GitHub account.  Clone this forked repository (click the green clone option on your forked repository) to obtain a link for use in step 10 below.

8. Open a new instance of your operating system's terminal and navigate to the "earth-analytics" directory (run line **cd earth-analytics**).

5. Ensure that the environment is activated before proceeding.  This is done by running the line **conda activate earth-analytics-python** in the terminal.

6. Update Scipy package to latest version.  This is done by running the line **pip install --user --upgrade scipy**

7. Run the line **jupyter notebook** to open the jupyter notebook program.

8. Navigate to the "earth-analytics" folder.

9. Click **New** in the toolbar and select **terminal**

10. In this new terminal, run the line **cd earth-analytics** to enter into your earth-analytics directory, and then run the line **git clone** followed by the url generated from forking and cloning this repository.  This will place the full repository into your "earth-analytics" folder for use.  Now you are ready to begin running the notebook!

## Files Included in this Repository:
.gitignore = file detailing python files that we do not want git to track, notably automatically generated files such as .ipynb_checkpoints.

LICENSE = BSD-3 Clause license detailing legal use of this code.

README.md = ReadMe file detailing the purpose and use of this repository.

usgs-nccasc-soil-moisture = .ipynb Jupyter Notebook file containing code to download, import, and process SCAN soil moisture datasets.
