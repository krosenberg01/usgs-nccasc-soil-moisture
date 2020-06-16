#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import os
import earthpy as et
import warnings
import pandas as pd
import earthpy.plot as ep

# Ignore warnings
warnings.simplefilter('ignore')


# In[2]:


def url_to_df(url, station_name, dictionary):
    """Function that takes a url to a csv file and downloads and 
    imports the data contained at the url. Then, it changes the station name 
    in the new dataframe to an input name given (ideally the name of the station),
    removes any unnecessary columns of data, and changes the month names from int 
    to str month name format.

        Parameters
        ----------
        url : url to csv file
            Input url to a csv file.

        station_name : str
            Name of the station for the data being imported and downloaded.

        dictionary : dictionary
            Empty dictionary for the created dataframes to be exported to.

        Returns
        ------
        No physical return; Returns any newly created dataframes to the input 
        empty dictionary specified.
    """
    
    path_to_data = os.path.join(et.data.get_data(url=url))
    
    dataframe = pd.read_csv(path_to_data)
    
    dataframe['Station ID'] = station_name
    
    output_dataframe = dataframe[['Station ID', 'year', 'month', 'day', 'doy',
                                  'sm_5cm', 'sm_10cm', 'sm_20cm', 'sm_50cm', 'sm_100cm']]
    
    output_dataframe['month'].replace({1: "Jan", 2: "Feb", 3: "Mar", 
                                  4: "Apr", 5: "May", 6: "Jun", 
                                  7: "Jul", 8: "Aug", 9: "Sep", 
                                  10: "Oct", 11: "Nov", 12: "Dec"}, 
                                 inplace=True)
    
    cut_labels = ['decad0', 'decad1', 'decad2']
    cut_bins = [0, 10, 20, 31]
    output_dataframe['decad'] = pd.cut(output_dataframe['day'], bins=cut_bins, labels=cut_labels)
    
    cut_labels = ['pentad0', 'pentad1', 'pentad2', 'pentad3', 'pentad4', 'pentad5']
    cut_bins = [0, 5, 10, 15, 20, 25, 31]
    output_dataframe['pentad'] = pd.cut(output_dataframe['day'], bins=cut_bins, labels=cut_labels)
    
    dictionary.update({station_name: output_dataframe})


# In[3]:


# Create target dictionary for storage of site data
soil_moisture_dict = {}


# In[4]:


# Download and import data for each site using function
# Bushland, TX: 2006
url_to_df(
    "http://nationalsoilmoisture.com/test/VWC_QAQC/scan/2006.csv", "bushland", soil_moisture_dict)

# Nunn, Colorado: 2017
url_to_df(
    "http://nationalsoilmoisture.com/test/VWC_QAQC/scan/2017.csv", "nunn", soil_moisture_dict)

# Fort Assiniboine, Montana: 2019
url_to_df(
    "http://nationalsoilmoisture.com/test/VWC_QAQC/scan/2019.csv", "fort_assiniboine", soil_moisture_dict)

# Mandan, North Dakota: 2020
url_to_df(
    "http://nationalsoilmoisture.com/test/VWC_QAQC/scan/2020.csv", "mandan", soil_moisture_dict)

# Lind, Washington: 2021
url_to_df(
    "http://nationalsoilmoisture.com/test/VWC_QAQC/scan/2021.csv", "lind", soil_moisture_dict)

# Beasley Lake, Mississippi: 2032
url_to_df(
    "http://nationalsoilmoisture.com/test/VWC_QAQC/scan/2032.csv", "beasley_lake", soil_moisture_dict)

# Eastview Farm, Tennessee: 2077
url_to_df(
    "http://nationalsoilmoisture.com/test/VWC_QAQC/scan/2077.csv", "eastview_farm", soil_moisture_dict)

# Mammoth Cave, Kentucky: 2079
url_to_df(
    "http://nationalsoilmoisture.com/test/VWC_QAQC/scan/2079.csv", "mammoth_cave", soil_moisture_dict)

# Abrams, Kansas: 2092
url_to_df(
    "http://nationalsoilmoisture.com/test/VWC_QAQC/scan/2092.csv", "abrams", soil_moisture_dict)


# In[7]:


# List of all stations:
station_list = ["bushland", "nunn", "fort_assiniboine", "mandan",
                "lind", "beasley_lake", "eastview_farm", "mammoth_cave", "abrams"]


# In[ ]:




