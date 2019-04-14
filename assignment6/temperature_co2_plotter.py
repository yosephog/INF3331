import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

""" This script plots temperature,CO2 and CO2 by country.
it reads data from a csv files and plots them for different
year, temperature and so on.
"""
def read_temprature(month,year_from,year_to,temp_from,temp_to):
    """ This method read a temperature .csv file and returns
    a data fram that is parsed according to the given paramenters
    Parameters-:
    month: str
      the month to be plotted
    year_from: int
       the year from to be plotted that is the start year
     year_to:
       the year up to be plotted
     temp_from: int
       the minimum amount of temperature to be plotted
     temp_to: int
        the maximum amount of teperature to be plotted

    return-:
      returns a data frame that is parsed that fills the Parameters
      that was given.
    """
    temprature=pd.read_csv('temperature.csv',sep=',')
    #temprature=temprature.set_index('Year')
    temprature=temprature[['Year',month]]
    temprature=temprature[(temprature['Year'] >= year_from)]
    temprature=temprature[(temprature['Year'] <= year_to)]
    temprature=temprature.loc[(temprature[month] >= temp_from)]
    temprature=temprature.loc[(temprature[month] <= temp_to)]
    #print(temprature)

    return temprature

def read_co2(year_from,year_to):
    """ This method read a co2 .csv file and returns
    a data fram that is parsed according to the given paramenters
    Parameters-:
    year_from: int
       the year from to be plotted that is the start year
     year_to:
       the year up to be plotted

    return-:
      returns a data frame that is parsed that fills the Parameters
      that was given.
    """

    co2=pd.read_csv('co2.csv',sep=',')
    #co2=co2.set_index('Year')
    co2=co2[(co2['Year'] >= year_from)]
    co2=co2[(co2['Year'] <= year_to)]
    #print(co2)

    return co2

def plot_temprature(month,year_from,year_to,temp_from,temp_to):
    """ This method plots by using the read_temprature method and save
    the plot in a a folder called static at the present directory.
    Parameters-:
    month: str
      the month to be plotted
    year_from: int
       the year from to be plotted that is the start year
     year_to:
       the year up to be plotted
     temp_from: int
       the minimum amount of temperature to be plotted
     temp_to: int
        the maximum amount of teperature to be plotted


    """
    temp=read_temprature(month,year_from,year_to,temp_from,temp_to)
    temp.plot(x='Year')
    if not os.path.exists('static'):
        os.makedirs('static')
    plt.savefig('static/temperature_plot.jpg')

def plot_co2(year_from,year_to):
    """ This method plots a jpg file and save it
     in a static folder in the present direcotry
    Parameters-:
    year_from: int
       the year from to be plotted that is the start year
     year_to: int
       the year up to be plotted
     x_axis-: str
      the one to be the x axis when plotted

    """
    co2=read_co2(year_from,year_to)
    co2.plot(x='Year')
    if not os.path.exists('static'):
        os.makedirs('static')
    plt.savefig('static/co2_plot.jpg')

def read_co2_country(year,lower_threshold,upper_threshold):
    """ This method read a co2_by_country .csv file and returns
    a data fram that is parsed according to the given paramenters
    Parameters-:
    year: str
       the year to be plotted
    lower_threshold:
     the lower amount of co2 that can be included in the plot
     upper_threshold:
       the higher amount of co2 that can be included in the plot
    return-:
      returns a data frame that is parsed that fills the Parameters
      that was given.
    """
    country=pd.read_csv('CO2_by_country.csv',sep=',')
    data=country[['Country Code','Indicator Name','Indicator Code',year]]
    data=data[(data[year] >= lower_threshold)]
    data=data[(data[year] <= upper_threshold)]
    return data

def plot_co2_by_country(year,lower_threshold,upper_threshold):
    """ This method plots a jpg file and save it
     in a static folder in the present direcotry
     x_axis is choosen to be country code. this is becuase
     it is preferable and display the plot in a meaning ful way.

     type plot is bar
     Parameters-:
     year: str
        the year to be plotted
     lower_threshold:
      the lower amount of co2 that can be included in the plot
      upper_threshold:
        the higher amount of co2 that can be included in the plot

      """
    country=read_co2_country(year,lower_threshold,upper_threshold)
    country.plot(x='Country Code',kind='bar')
    if not os.path.exists('static'):
        os.makedirs('static')
    plt.savefig('static/co2_by_country_plot.jpg')
