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
from scipy import stats
from scipy.stats import zscore
import numpy as np


# In[2]:


# This list should be updated every year; these are the years the code will examine!
years_list_all = (1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 
                  2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 
                  2014, 2015, 2016, 2017, 2018, 2019, 2020)

month_list_all = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')


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
    dataframe.hist(column='sm_5cm', bins=50)
    dataframe.hist(column='sm_10cm', bins=50)
    dataframe.hist(column='sm_20cm', bins=50)
    dataframe.hist(column='sm_50cm', bins=50)
    dataframe.hist(column='sm_100cm', bins=50)


# In[7]:


def yearly_nan_analysis(dataframe):
    
    column_names = ['sm_5cm', 'sm_10cm', 'sm_20cm', 'sm_50cm', 'sm_100cm']
    
    for column in column_names:
        
        if not dataframe[column].isna().sum() < 90:
            dataframe[column] = dataframe[column].where(dataframe[column].isna(), np.nan)

    
# In[8]:


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
    
    empty_dataframe = pd.DataFrame()

    years_list = years_list_all
    
    column_names = ['sm_5cm', 'sm_10cm', 'sm_20cm', 'sm_50cm', 'sm_100cm']

    for year in years_list:

        sm_year = soil_moisture_dataframe[soil_moisture_dataframe["year"] == year]

        # Ensure that there is enough data for each year before mean is calculated
        if sm_year['day'].size > 275:
            
            # Missing/NaN data cleaning
            yearly_nan_analysis(sm_year)
            
            sm_year_mean = sm_year.groupby(
                                    ["year"])[["sm_5cm", "sm_10cm", 
                                               "sm_20cm", "sm_50cm", 
                                               "sm_100cm"]].mean()

            empty_dataframe = empty_dataframe.append(sm_year_mean)

        else:
            data = {'sm_5cm':[np.nan], 'sm_10cm':[np.nan], 'sm_20cm':[np.nan], 'sm_50cm':[np.nan], 'sm_100cm':[np.nan]}
            filler_nan_df = pd.DataFrame(data, index=[year])
            empty_dataframe = empty_dataframe.append(filler_nan_df)
            print(year,': This year did not contain enough data and was set as NaN')
            
    return empty_dataframe


# In[9]:


# Loop through each column to detect and replace columns with NaN values if NaN values exceed 50% of monthly data
def monthly_nan_analysis(dataframe):
    
    column_names = ['sm_5cm', 'sm_10cm', 'sm_20cm', 'sm_50cm', 'sm_100cm']
    
    for column in column_names:
        
        if not dataframe[column].isna().sum() < 16:
            dataframe[column] = dataframe[column].where(dataframe[column].isna(), np.nan)


# In[10]:


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
    
    empty_year_month_dataframe = pd.DataFrame()
    
    years_list = years_list_all
    
    sm_month = soil_moisture_dataframe[soil_moisture_dataframe["month"] == month_name]
    
    # Ensure there is enough data for mean calculation
    for year in years_list:
        
        sm_year_month = sm_month[sm_month["year"] == year]
        
        if sm_year_month['day'].size > 15:
            
            # Missing/NaN data cleaning
            monthly_nan_analysis(sm_year_month)
            
            sm_year_month_mean = sm_year_month.groupby(
                ["year"])[["sm_5cm", "sm_10cm", "sm_20cm", "sm_50cm", "sm_100cm"]].mean()
            
            empty_year_month_dataframe = empty_year_month_dataframe.append(sm_year_month_mean)
            
        else:
            data = {'sm_5cm':[np.nan], 'sm_10cm':[np.nan], 'sm_20cm':[np.nan], 'sm_50cm':[np.nan], 'sm_100cm':[np.nan]}
            filler_nan_df = pd.DataFrame(data, index=[year])
            empty_year_month_dataframe = empty_year_month_dataframe.append(filler_nan_df)
            print(month_name, year, ': Did not contain enough data and was set as NaN')

    return empty_year_month_dataframe


# In[11]:


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
    
    station_sm_monthly_mean = pd.DataFrame()
    
    month_list = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    
    # Select year of analysis
    station_sm_year = soil_moisture_dataframe[soil_moisture_dataframe["year"] == year]

    # Loop through each month of the year to examine NaN or missing values
    for month in month_list:
        
        station_sm_year_month = station_sm_year[station_sm_year["month"] == month]
        
        if station_sm_year_month['day'].size > 15:
            
            monthly_nan_analysis(station_sm_year_month)
    
            station_sm_monthly_avg = station_sm_year_month.groupby(
                ["month"])[["sm_5cm", "sm_10cm", "sm_20cm", "sm_50cm", "sm_100cm"]].mean()
        
            station_sm_monthly_mean = station_sm_monthly_mean.append(station_sm_monthly_avg)
            
        else:
            data = {'sm_5cm':[np.nan], 'sm_10cm':[np.nan], 'sm_20cm':[np.nan], 'sm_50cm':[np.nan], 'sm_100cm':[np.nan]}
            filler_nan_df = pd.DataFrame(data, index=[month])
            station_sm_monthly_mean = station_sm_monthly_mean.append(filler_nan_df)
            print(month, year, ': Did not contain enough data and was set as NaN')
    
    return station_sm_monthly_mean


# In[12]:


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


# In[13]:


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


# In[14]:


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


# In[15]:


def decad_nan_analysis(dataframe):
    
    column_names = ['sm_5cm', 'sm_10cm', 'sm_20cm', 'sm_50cm', 'sm_100cm']
    
    for column in column_names:
        
        if not dataframe[column].isna().sum() < 6:
            dataframe[column] = dataframe[column].where(dataframe[column].isna(), np.nan)


# In[15]:


def decad_mean(dataframe, year):
    
    month_list = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    dec_list = ['decad0', 'decad1', 'decad2']
    
    empty_year_dec_mean_df = pd.DataFrame()
    
    station_sm_year_dec = dataframe[dataframe['year'] == year]
    
    for month in month_list:
        
        station_sm_month_dec = station_sm_year_dec[station_sm_year_dec['month'] == month]
    
        for decad in dec_list:
            
            station_sm_year_month_dec = station_sm_month_dec[station_sm_month_dec['decad'] == decad]
            
            # Ensure each decad of each month has enough data to provide an accurate mean
            if station_sm_year_month_dec['decad'].size > 5:
            
                # NaN analysis
                decad_nan_analysis(station_sm_year_month_dec)

                # Calculate mean
                filler_decad_mean_df = station_sm_year_month_dec.groupby(["month"])[["sm_5cm", "sm_10cm", 
                                                                                "sm_20cm", "sm_50cm", 
                                                                                "sm_100cm"]].mean()

                # Clean columns
                filler_decad_mean_df = filler_decad_mean_df.reset_index()
                filler_decad_mean_df.insert(0, "year", [year], True)
                filler_decad_mean_df.insert(2, "decad", [decad], True)

                empty_year_dec_mean_df = empty_year_dec_mean_df.append(filler_decad_mean_df)
                
            # If a decad of a month does not contain enough data, append a row with only NaN values   
            else:
                data = {'year': [year], 'month':[month], 'decad':[decad], 'sm_5cm':[np.nan], 
                        'sm_10cm':[np.nan], 'sm_20cm':[np.nan], 'sm_50cm':[np.nan], 'sm_100cm':[np.nan]}
                
                filler_nan_df = pd.DataFrame(data)
                
                empty_year_dec_mean_df = empty_year_dec_mean_df.append(filler_nan_df)
                
                #print(year, month, decad, ': Did not contain enough data and was set as NaN')
    
    # Column/Index management
    #empty_year_dec_mean_df = empty_year_dec_mean_df.set_index('year')
    
    return empty_year_dec_mean_df


# In[16]:


def decad_zscore(dataframe, year):

    # Lists needed for loops
    dec_list = ['decad0', 'decad1', 'decad2']
    years_list_all = (1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 
                      2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 
                      2014, 2015, 2016, 2017, 2018, 2019, 2020)
    month_list_all = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    # Create empty dataframes for temporary use in the function
    empty_df1 = pd.DataFrame()
    final_year_zscore_df = pd.DataFrame()

    for month in month_list_all:

        station_sm_month = dataframe[dataframe["month"] == month]

        for decad in dec_list:

            station_sm_month_dec = station_sm_month[station_sm_month['decad'] == decad]

            for item in years_list_all:
                station_sm_month_dec_year = station_sm_month_dec[station_sm_month_dec["year"] == item]

                if station_sm_month_dec_year['year'].size > 5:
                    
                    # NaN analysis
                    decad_nan_analysis(station_sm_month_dec_year)

                    filler_decad_mean_df = station_sm_month_dec_year.groupby(["month"])[["sm_5cm", "sm_10cm", 
                                                                                            "sm_20cm", "sm_50cm", 
                                                                                            "sm_100cm"]].mean()
                    # Clean columns
                    filler_decad_mean_df = filler_decad_mean_df.reset_index()
                    filler_decad_mean_df.insert(0, "year", [item], True)
                    filler_decad_mean_df.insert(2, "decad", [decad], True)

                    empty_df1 = empty_df1.append(filler_decad_mean_df)
                    
                # If the year does not contain enough data to make calculations, set that year as NaN
                else:
                    data = {'year': [item], 'month':[month], 'decad':[decad], 'sm_5cm':[np.nan], 
                                    'sm_10cm':[np.nan], 'sm_20cm':[np.nan], 'sm_50cm':[np.nan], 'sm_100cm':[np.nan]}

                    filler_nan_df = pd.DataFrame(data)

                    empty_df1 = empty_df1.append(filler_nan_df)

            # Z-Score analysis
            empty_df1 = empty_df1.groupby(["year"])[["sm_5cm", "sm_10cm", "sm_20cm", "sm_50cm", "sm_100cm"]].mean()
            empty_df1_zscore = empty_df1.apply(zscore, nan_policy='omit')

            # Create new dataframe of calculated z-scores for desired year
            zscore_month_dec_year = empty_df1_zscore[empty_df1_zscore.index.values == year]
            zscore_month_dec_year.insert(0, "month", [month], True)
            zscore_month_dec_year.insert(1, "decad", [decad], True)

            final_year_zscore_df = final_year_zscore_df.append(zscore_month_dec_year)

    return final_year_zscore_df


# In[16]:


def pentad_nan_analysis(dataframe):
    
    column_names = ['sm_5cm', 'sm_10cm', 'sm_20cm', 'sm_50cm', 'sm_100cm']
    
    for column in column_names:
        
        if not dataframe[column].isna().sum() < 3:
            dataframe[column] = dataframe[column].where(dataframe[column].isna(), np.nan)


# In[16]:


def pentad_mean(dataframe, year):
    
    month_list = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    pent_list = ['pentad0', 'pentad1', 'pentad2', 'pentad3', 'pentad4', 'pentad5']
    
    empty_year_pent_mean_df = pd.DataFrame()
    
    station_sm_year_pent = dataframe[dataframe['year'] == year]
    
    for month in month_list:
        
        station_sm_month_pent = station_sm_year_pent[station_sm_year_pent['month'] == month]
    
        for pentad in pent_list:
            
            station_sm_year_month_pent = station_sm_month_pent[station_sm_month_pent['pentad'] == pentad]
            
            # Ensure each pentad of each month has enough data to provide an accurate mean
            if station_sm_year_month_pent['pentad'].size > 2:
            
                # NaN analysis
                pentad_nan_analysis(station_sm_year_month_pent)

                # Calculate mean
                filler_pentad_mean_df = station_sm_year_month_pent.groupby(["month"])[["sm_5cm", "sm_10cm", 
                                                                                "sm_20cm", "sm_50cm", 
                                                                                "sm_100cm"]].mean()

                # Clean columns
                filler_pentad_mean_df = filler_pentad_mean_df.reset_index()
                filler_pentad_mean_df.insert(0, "year", [year], True)
                filler_pentad_mean_df.insert(2, "pentad", [pentad], True)

                empty_year_pent_mean_df = empty_year_pent_mean_df.append(filler_pentad_mean_df)
                
            # If a pentad of a month does not contain enough data, append a row with only NaN values   
            else:
                data = {'year': [year], 'month':[month], 'pentad':[pentad], 'sm_5cm':[np.nan], 
                        'sm_10cm':[np.nan], 'sm_20cm':[np.nan], 'sm_50cm':[np.nan], 'sm_100cm':[np.nan]}
                
                filler_nan_pent_df = pd.DataFrame(data)
                
                empty_year_pent_mean_df = empty_year_pent_mean_df.append(filler_nan_pent_df)
                
                #print(year, month, pentad, ': Did not contain enough data and was set as NaN')
    
    # Column/Index management
    #empty_year_pent_mean_df = empty_year_pent_mean_df.set_index('year')
    
    
    return empty_year_pent_mean_df


# In[17]:


def pentad_zscore(dataframe, year):

    # Lists needed for loops
    pent_list = ['pentad0', 'pentad1', 'pentad2', 'pentad3', 'pentad4', 'pentad5']
    years_list_all = (1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 
                      2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 
                      2014, 2015, 2016, 2017, 2018, 2019, 2020)
    month_list_all = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    # Create empty dataframes for temporary use in the function
    empty_df2 = pd.DataFrame()
    final_pent_year_zscore_df = pd.DataFrame()

    for month in month_list_all:

        station_sm_month = dataframe[dataframe["month"] == month]

        for pentad in pent_list:

            station_sm_month_pent = station_sm_month[station_sm_month['pentad'] == pentad]

            for item in years_list_all:
                station_sm_month_pent_year = station_sm_month_pent[station_sm_month_pent["year"] == item]

                if station_sm_month_pent_year['year'].size > 2:
                    
                    # NaN analysis
                    pentad_nan_analysis(station_sm_month_pent_year)

                    filler_pentad_mean_df = station_sm_month_pent_year.groupby(["month"])[["sm_5cm", "sm_10cm", 
                                                                                            "sm_20cm", "sm_50cm", 
                                                                                            "sm_100cm"]].mean()
                    # Clean columns
                    filler_pentad_mean_df = filler_pentad_mean_df.reset_index()
                    filler_pentad_mean_df.insert(0, "year", [item], True)
                    filler_pentad_mean_df.insert(2, "pentad", [pentad], True)

                    empty_df2 = empty_df2.append(filler_pentad_mean_df)
                    
                # If the year does not contain enough data to make calculations, set that year as NaN
                else:
                    data = {'year': [item], 'month':[month], 'pentad':[pentad], 'sm_5cm':[np.nan], 
                                    'sm_10cm':[np.nan], 'sm_20cm':[np.nan], 'sm_50cm':[np.nan], 'sm_100cm':[np.nan]}

                    filler_nan_df = pd.DataFrame(data)

                    empty_df2 = empty_df2.append(filler_nan_df)

            # Z-Score analysis
            empty_df2 = empty_df2.groupby(["year"])[["sm_5cm", "sm_10cm", "sm_20cm", "sm_50cm", "sm_100cm"]].mean()
            empty_df2_zscore = empty_df2.apply(zscore, nan_policy='omit')

            # Create new dataframe of calculated z-scores for desired year
            zscore_month_pent_year = empty_df2_zscore[empty_df2_zscore.index.values == year]
            zscore_month_pent_year.insert(0, "month", [month], True)
            zscore_month_pent_year.insert(1, "pentad", [pentad], True)

            final_pent_year_zscore_df = final_pent_year_zscore_df.append(zscore_month_pent_year)

    return final_pent_year_zscore_df


# In[17]:


def zscore_plot(dataframe, timescale, title):
    # Define plot space
    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5, figsize=(40, 30), constrained_layout=True)

    ax1 = plt.subplot2grid((2, 3), (0, 0), colspan=1)
    ax2 = plt.subplot2grid((2, 3), (0, 1), colspan=1)
    ax3 = plt.subplot2grid((2, 3), (0, 2), rowspan=1)
    ax4 = plt.subplot2grid((2, 3), (1, 0))
    ax5 = plt.subplot2grid((2, 3), (1, 1))

    # Define figure title
    fig.suptitle(title, fontsize=40)

    # 5cm depth subplot
    ax1.bar(dataframe.index.values,
             dataframe['sm_5cm'],
             color=(dataframe['sm_5cm'] > 0).map({True: 'b',
                                                        False: 'r'}))

    ax1.set_title('Depth: 5cm', fontsize = 40)
    ax1.set_ylabel('Z-Score Soil Moisture', fontsize = 20.0)
    ax1.set_xlabel(timescale, fontsize = 20)

    # 10cm depth subplot
    ax2.bar(dataframe.index.values,
             dataframe['sm_10cm'],
             color=(dataframe['sm_10cm'] > 0).map({True: 'b',
                                                        False: 'r'}))

    ax2.set_title('Depth: 10cm', fontsize = 40)
    ax2.set_ylabel('Z-Score Soil Moisture', fontsize = 20.0)
    ax2.set_xlabel(timescale, fontsize = 20)

    # 20cm depth subplot
    ax3.bar(dataframe.index.values,
             dataframe['sm_20cm'],
             color=(dataframe['sm_20cm'] > 0).map({True: 'b',
                                                        False: 'r'}))

    ax3.set_title('Depth: 20cm', fontsize = 40)
    ax3.set_ylabel('Z-Score Soil Moisture', fontsize = 20.0)
    ax3.set_xlabel(timescale, fontsize = 20)

    # 50cm depth subplot
    ax4.bar(dataframe.index.values,
             dataframe['sm_50cm'],
             color=(dataframe['sm_50cm'] > 0).map({True: 'b',
                                                        False: 'r'}))

    ax4.set_title('Depth: 50cm', fontsize = 40)
    ax4.set_ylabel('Z-Score Soil Moisture', fontsize = 20.0)
    ax4.set_xlabel(timescale, fontsize = 20)

    # 100cm depth subplot
    ax5.bar(dataframe.index.values,
             dataframe['sm_100cm'],
             color=(dataframe['sm_100cm'] > 0).map({True: 'b',
                                                        False: 'r'}))

    ax5.set_title('Depth: 100cm', fontsize = 40)
    ax5.set_ylabel('Z-Score Soil Moisture', fontsize = 20.0)
    ax5.set_xlabel(timescale, fontsize = 20)

    plt.show()
    
    
# In[18]:


def monthly_mean_zscore(dataframe, year):
    
    month_list = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

    years_list_all = (1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 
                      2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 
                      2014, 2015, 2016, 2017, 2018, 2019, 2020)

    monthly_mean_zscore_df = pd.DataFrame()
    station_nan_cleaned_mean_df = pd.DataFrame()

    for month in month_list:

        station_sm_month = dataframe[dataframe["month"] == month]

        for x in years_list_all:

            station_sm_month_year = station_sm_month[station_sm_month["year"] == x]

            if station_sm_month_year['day'].size > 15:

                monthly_nan_analysis(station_sm_month_year)

                station_sm_month_year_mean = station_sm_month_year.groupby(
                                ["month"])[["sm_5cm", "sm_10cm", "sm_20cm", "sm_50cm", "sm_100cm"]].mean()

                station_sm_month_year_mean.insert(0, "year", [x], True)

                station_nan_cleaned_mean_df = station_nan_cleaned_mean_df.append(station_sm_month_year_mean)

            else:
                data = {'year': [x], 'sm_5cm':[np.nan], 'sm_10cm':[np.nan], 'sm_20cm':[np.nan], 'sm_50cm':[np.nan], 'sm_100cm':[np.nan]}
                filler_nan_df = pd.DataFrame(data, index=[month])
                station_nan_cleaned_mean_df = station_nan_cleaned_mean_df.append(filler_nan_df)
                #print(month, x, ': Did not contain enough data and was set as NaN')
    
    for y in month_list:
                
        station_cleaned_month_mean = station_nan_cleaned_mean_df[station_nan_cleaned_mean_df.index.values == y]

        station_sm_month_mean = station_cleaned_month_mean.groupby(
                    ["year"])[["sm_5cm", "sm_10cm", "sm_20cm", "sm_50cm", "sm_100cm"]].mean()

        station_month_zscore = station_sm_month_mean.apply(zscore, nan_policy='omit')

        station_month_zscore_year = station_month_zscore[station_month_zscore.index.values == year]
        
        station_month_zscore_year.insert(0, "month", [y], True)
        
        monthly_mean_zscore_df = monthly_mean_zscore_df.append(station_month_zscore_year)
        
    monthly_mean_zscore_df = monthly_mean_zscore_df.reset_index()

    monthly_mean_zscore_df = monthly_mean_zscore_df.set_index('month')
                
    return monthly_mean_zscore_df