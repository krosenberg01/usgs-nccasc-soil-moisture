#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import os
import matplotlib.pyplot as plt
import earthpy as et
import warnings
import pandas as pd
import earthpy.plot as ep


# In[2]:


# Define function to take in a url and output a dataframe into a target dictionary
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
    
    
    dictionary.update({station_name: output_dataframe})


# In[3]:


def plot_yearly_avg_sm(dataframe, figure_title):
    """Function that takes an input station name and plots the yearly 
    average soil moisture values for each depth (5cm, 10cm, 20cm, 50cm, 100cm).  
    Please note that for this function to run, a dataframe of yearly average soil 
    moisture for each depth must exist under the name "yearly_avg_sm"

        Parameters
        ----------
        station_name : str
            Description...


        Returns
        ------
        No physical return.  Will output a plot of yearly average soil moisture 
        at each depth for the station specified.

    """

    filler_yearly_avg_sm = yearly_avg_sm(dataframe)
    
    # Create figure and plot space
    fig, ax = plt.subplots(figsize=(20, 10))

    # Subplot of daily mean discharge from Aug-Oct 2013 at various Colorado stream sites
    ax.plot(filler_yearly_avg_sm.index.values,
         filler_yearly_avg_sm['sm_5cm'],
         color="blue",
         marker='o',
         label="5cm")
    ax.plot(filler_yearly_avg_sm.index.values,
         filler_yearly_avg_sm['sm_10cm'],
         color="red",
         marker='o', label="10cm")
    ax.plot(filler_yearly_avg_sm.index.values,
         filler_yearly_avg_sm['sm_20cm'],
         color="green",
         marker='o', label="20cm")
    ax.plot(filler_yearly_avg_sm.index.values,
         filler_yearly_avg_sm['sm_50cm'],
         color="purple",
         marker='o', label="50cm")
    ax.plot(filler_yearly_avg_sm.index.values,
         filler_yearly_avg_sm['sm_100cm'],
         color="orange",
         marker='o',
         label="100cm")
    
    ax.legend()
    ax.legend(title='Soil Moisture Depth of Measurement\n')
    fig.suptitle("Yearly Mean Soil Moisture", fontsize=20)
    ax.set_title(figure_title)
    ax.set_xlabel("Year")
    ax.set_ylabel("Soil Moisture %")


# In[4]:


def plot_monthly_avg_sm(dataframe, year, figure_title):
    """Function that takes an input station name and plots the monthly 
    average soil moisture values for each depth (5cm, 10cm, 20cm, 50cm, 100cm) 
    for a specified year. Please note that for this function to run, a dataframe 
    of monthly average soil moisture for each depth must exist under the name "monthly_mean"

        Parameters
        ----------
        station_name : str
            Name of station you want plotted.

        year : int
            Integer value for the year desired.


        Returns
        ------
        No physical return.  Will output a plot of monthly average soil moisture 
        at each depth for the station and year specified.

    """
    
    filler_monthly_avg_sm = monthly_mean(dataframe, year)
    
    # Create figure and plot space
    fig, ax = plt.subplots(figsize=(20, 10))

    # Subplot of daily mean discharge from Aug-Oct 2013 at various Colorado stream sites
    ax.plot(filler_monthly_avg_sm.index.values,
         filler_monthly_avg_sm['sm_5cm'],
         color="blue",
         marker='o',
         label="5cm")
    ax.plot(filler_monthly_avg_sm.index.values,
         filler_monthly_avg_sm['sm_10cm'],
         color="red",
         marker='o', label="10cm")
    ax.plot(filler_monthly_avg_sm.index.values,
         filler_monthly_avg_sm['sm_20cm'],
         color="green",
         marker='o', label="20cm")
    ax.plot(filler_monthly_avg_sm.index.values,
         filler_monthly_avg_sm['sm_50cm'],
         color="purple",
         marker='o', label="50cm")
    ax.plot(filler_monthly_avg_sm.index.values,
         filler_monthly_avg_sm['sm_100cm'],
         color="orange",
         marker='o',
         label="100cm")
    
    ax.legend()
    ax.legend(title='Soil Moisture Depth of Measurement\n')
    fig.suptitle("Monthly Mean Soil Moisture", fontsize=20)
    ax.set_title(figure_title)
    ax.set_xlabel("Month")
    ax.set_ylabel("Soil Moisture %")


# In[5]:


def plot_daily_avg_sm(dataframe, year, figure_title):
    """Function that takes an input station name and plots the daily 
    average soil moisture values for each depth (5cm, 10cm, 20cm, 50cm, 100cm) 
    for a specified year. Please note that for this function to run, a dataframe 
    of daily average soil moisture for each depth must exist under the name "daily_avg"

        Parameters
        ----------
        station_name : str
            Name of station you want plotted.

        year : int
            Integer value for the year desired.


        Returns
        ------
        No physical return.  Will output a plot of daily average soil moisture 
        at each depth for the station and year specified.

    """
    
    filler_daily_avg_sm = daily_avg(dataframe, year)
    
    # Create figure and plot space
    fig, ax = plt.subplots(figsize=(20, 10))

    # Subplot of daily mean discharge from Aug-Oct 2013 at various Colorado stream sites
    ax.plot(filler_daily_avg_sm.index.values,
         filler_daily_avg_sm['sm_5cm'],
         color="blue",
         marker='o',
         label="5cm")
    ax.plot(filler_daily_avg_sm.index.values,
         filler_daily_avg_sm['sm_10cm'],
         color="red",
         marker='o', label="10cm")
    ax.plot(filler_daily_avg_sm.index.values,
         filler_daily_avg_sm['sm_20cm'],
         color="green",
         marker='o', label="20cm")
    ax.plot(filler_daily_avg_sm.index.values,
         filler_daily_avg_sm['sm_50cm'],
         color="purple",
         marker='o', label="50cm")
    ax.plot(filler_daily_avg_sm.index.values,
         filler_daily_avg_sm['sm_100cm'],
         color="orange",
         marker='o',
         label="100cm")
    
    ax.legend()
    ax.legend(title='Soil Moisture Depth of Measurement\n')
    fig.suptitle("Daily Mean Soil Moisture", fontsize=20)
    ax.set_title(figure_title)
    ax.set_xlabel("Julian Day")
    ax.set_ylabel("Soil Moisture %")


# In[6]:


def generate_hist(dataframe):
    dataframe.hist(column='sm_5cm')
    dataframe.hist(column='sm_10cm')
    dataframe.hist(column='sm_20cm')
    dataframe.hist(column='sm_50cm')
    dataframe.hist(column='sm_100cm')


# In[7]:


# Function that takes an input dataframe of soil moisture and outputs a dataframe of yearly average SM
def yearly_avg_sm(soil_moisture_dataframe):
    """Function that takes an input dataframe containing raw soil moisture data, 
    and turns it into an output dataframe that contains data from the input 
    dataframe grouped by year and averaged.  Note that for this function to work 
    properly you need to include every year of data desired in the "years_list"
    contained within the function.

        Parameters
        ----------
        soil_moisture_dataframe : dataframe
            Dataframe containing raw soil moisture data.


        Returns
        ------
        empty_dataframe : dataframe
            Dataframe showing yearly average soil moisture for every year contained in the 
            "years_list."

    """
    
    years_list = (1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 
              2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 
              2014, 2015, 2016, 2017, 2018, 2019, 2020)
    
    empty_dataframe = pd.DataFrame()
    
    for x in years_list:
        sm_year = soil_moisture_dataframe[soil_moisture_dataframe["year"] == x]

        sm_year_mean = sm_year.groupby(
                                ["year"])[["sm_5cm", "sm_10cm", 
                                           "sm_20cm", "sm_50cm", 
                                           "sm_100cm"]].mean()
    
        empty_dataframe = empty_dataframe.append(sm_year_mean)
    
    return empty_dataframe


# In[8]:


# Function that takes an input SM dataframe and returns a dataframe displaying yearly average SM for a specified month
def yearly_mean_month(soil_moisture_dataframe, month_name):
    """Function that takes an input dataframe and specified month name 
    and returns a new dataframe that shows yearly average soil moisture 
    values for a specific month, across all years of data.

        Parameters
        ----------
        soil_moisture_dataframe: dataframe
            Input dataframe containing raw soil moisture data.

        month_name : str
            3-letter string month name (e.g. Jan, Feb, Mar, etc.)


        Returns
        ------
        sm_year_month_mean : dataframe
            Output dataframe showing yearly average soil moisture 
            values for a specific month across all years of data.

    """
    
    sm_year_month = soil_moisture_dataframe[soil_moisture_dataframe["month"] == month_name]

    sm_year_month_mean = sm_year_month.groupby(
        ["year"])[["sm_5cm", "sm_10cm", "sm_20cm", "sm_50cm", "sm_100cm"]].mean()

    return sm_year_month_mean


# In[9]:


# Function to take an input SM dataframe and calculate monthly average SM for each depth across one specific year
def monthly_mean(soil_moisture_dataframe, year):
    """Function that takes an input dataframe of raw soil moisture data and a 
    specified year and returns an output dataframe showing monthly average soil 
    moisture for each depth across that year.

        Parameters
        ----------
        soil_moisture_dataframe : type
            Input dataframe containing raw soil moisture data.

        year : int
            Integer value for the year desired.


        Returns
        ------
        station_sm_monthly_mean : dataframe
            Dataframe showing monthly mean soil moisture for each depth across a 
            specified year.

    """
    
    station_sm_monthly_mean = soil_moisture_dataframe[soil_moisture_dataframe["year"] == year]

    station_sm_monthly_mean = station_sm_monthly_mean.groupby(
        ["month"])[["sm_5cm", "sm_10cm", "sm_20cm", "sm_50cm", "sm_100cm"]].mean()
    
    return station_sm_monthly_mean


# In[10]:


# Function that takes an input dataframe and calculates monthly mean SM across all years of data
def monthly_mean_all_years(soil_moisture_dataframe):
    """Function that takes an input dataframe of raw soil moisture data and 
    outputs a new dataframe that shows monthly mean soil moisture across all 
    years of data.

        Parameters
        ----------
        soil_moisture_dataframe : type
            Input dataframe containing raw soil moisture data.


        Returns
        ------
        monthly_sm_mean : dataframe
            Dataframe that shows monthly mean soil moisture across all 
            years of data.

    """
    
    monthly_sm_mean = soil_moisture_dataframe.groupby(
    ["month"])[["sm_5cm", "sm_10cm", "sm_20cm", "sm_50cm", "sm_100cm"]].mean()

    # Reindex dataframe to put month names in order
    monthly_sm_mean = monthly_sm_mean.reindex(
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep',
     'Oct', 'Nov', 'Dec'])
    
    return monthly_sm_mean


# In[11]:


def daily_avg(soil_moisture_dataframe, year):
    """Function that turns an input dataframe of raw soil moisture data 
    into a new dataframe showing daily average soil moisture across a 
    specified year.

        Parameters
        ----------
        soil_moisture_dataframe : dataframe
            Input dataframe containing raw soil moisture data.

        year : int
            Integer value for the year desired.


        Returns
        ------
        sm_daily_avg_year : dataframe
            Dataframe containing daily average soil moisture across 
            a specified year.
            
    """
    
    sm_daily_avg = soil_moisture_dataframe.set_index('doy')
    sm_daily_avg_year = sm_daily_avg[sm_daily_avg["year"] == year]
    
    return sm_daily_avg_year


# In[12]:


def daily_avg_all_years(soil_moisture_dataframe):
    """Function that takes an input dataframe of raw soil moisture data 
    and turns it into a dataframe showing average soil moisture value for 
    each Julian day of the year, across all years of data.

        Parameters
        ----------
        soil_moisture_dataframe : dataframe
            Input dataframe containing raw soil moisture data.


        Returns
        ------
        sm_year_daily_all_years : dataframe
            Dataframe showing average soil moisture value for 
            each Julian day of the year, across all years of data.

    """
    
    sm_daily_avg_all_years = soil_moisture_dataframe.set_index('doy')

    sm_year_daily_all_years = sm_daily_avg_all_years.groupby(
        ["doy"])[["sm_5cm", "sm_10cm", "sm_20cm", "sm_50cm", "sm_100cm"]].mean()
    
    return sm_year_daily_all_years

