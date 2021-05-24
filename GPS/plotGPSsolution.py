#import headers
import csv
import gmplot
import math
import pandas as pd
from gmplot import *

df = pd.read_csv('position.csv')
type_10 = df[df[' Solution Type'] == 10]
type_9  = df[df[' Solution Type'] == 9]
type_6  = df[df[' Solution Type'] == 6]
type_5  = df[df[' Solution Type'] == 5]
type_4  = df[df[' Solution Type'] == 4]
type_2  = df[df[' Solution Type'] == 2]
type_1  = df[df[' Solution Type'] == 1]
type_0  = df[df[' Solution Type'] == 0]




# with open('position_jackal.csv', newline = '') as csvfile: #read the csv file
with open('position.csv', 'r') as csvfile: #read the csv file

    reader = csv.DictReader(csvfile) #dataframe which csv is written into
    #iterate over each 'row' in the dataframe
    #each row is a python dictionary which contains:
    #dict_keys([' Ellipsoid Alt (m)', ' Solution Type', ' Lon (deg)', 'GPS Time (sec)', ' Lat (deg)'])

    lon_list_atlas = [] #lists to store latitude and longitude
    lat_list_atlas = []

    lon_sum_atlas = 0. #initialize sums to calculate average
    lat_sum_atlas = 0.

    for row in reader: #iterate over the rows
        lon_atlas = row[' Lon (deg)'] #extract longitude and latitude and assign them to variables
        lat_atlas = row[' Lat (deg)']

        lon_sum_atlas += float(lon_atlas) #increase sum to calculate average
        lat_sum_atlas += float(lat_atlas)

        lon_list_atlas.append(float(lon_atlas)) #append to longitude list
        lat_list_atlas.append(float(lat_atlas)) #append to latitude list

mean_lon_atlas = lon_sum_atlas / len(lon_list_atlas) #average longitude
mean_lat_atlas = lat_sum_atlas / len(lat_list_atlas) #average latitude



#first two arugments are the geographical coordinates .i.e. Latitude and Longitude
#and the zoom resolution
gmap = gmplot.GoogleMapPlotter(mean_lat_atlas, mean_lon_atlas, 18, map_type='satellite') #satellite view

#gmap.apikey = 'AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8'
gmap.scatter(type_10[' Lat (deg)'],type_10[' Lon (deg)'], size=1, marker = False, color = 'red') #plot first 2000 points red
gmap.scatter(type_9[' Lat (deg)'],type_9[' Lon (deg)'], size=1, marker = False, color = 'orange') #plot first 2000 points red
gmap.scatter(type_6[' Lat (deg)'],type_6[' Lon (deg)'], size=1, marker = False, color = 'yellow') #plot first 2000 points red
gmap.scatter(type_5[' Lat (deg)'],type_5[' Lon (deg)'], size=1, marker = False, color = 'green') #plot first 2000 points red
gmap.scatter(type_4[' Lat (deg)'],type_4[' Lon (deg)'], size=1, marker = False, color = 'blue') #plot first 2000 points red
gmap.scatter(type_2[' Lat (deg)'],type_2[' Lon (deg)'], size=1, marker = False, color = 'purple') #plot first 2000 points red
gmap.scatter(type_1[' Lat (deg)'],type_1[' Lon (deg)'], size=1, marker = False, color = 'white') #plot first 2000 points red
gmap.scatter(type_0[' Lat (deg)'],type_0[' Lon (deg)'], size=1, marker = False, color = 'brown') #plot first 2000 points red


#location where you want to save your file.
gmap.draw("/home/asl-laptop/workspace/gps_data/map04.html")
