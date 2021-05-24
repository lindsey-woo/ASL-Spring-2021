#import headers
import csv
import gmplot
import math
from gmplot import *

lon_list = []
lat_list = []

# with open('position.csv', newline = '') as csvfile: #read the csv file
with open('position.csv', 'r') as csvfile: #read the csv file

    reader = csv.DictReader(csvfile) #dataframe which csv is written into
    #iterate over each 'row' in the dataframe
    #each row is a python dictionary which contains:
    #dict_keys([' Ellipsoid Alt (m)', ' Solution Type', ' Lon (deg)', 'GPS Time (sec)', ' Lat (deg)'])

    lon_list = [] #lists to store latitude and longitude
    lat_list = []

    lon_sum = 0. #initialize sums to calculate average
    lat_sum = 0.

    for row in reader: #iterate over the rows
        lon = row[' Lon (deg)'] #extract longitude and latitude and assign them to variables
        lat = row[' Lat (deg)']

        lon_sum += float(lon) #increase sum to calculate average
        lat_sum += float(lat)

        lon_list.append(float(lon)) #append to longitude list
        lat_list.append(float(lat)) #append to latitude list

mean_lon = lon_sum / len(lon_list) #average longitude
mean_lat = lat_sum / len(lat_list) #average latitude

print("mean longitude: ", mean_lon, "mean latitude: ", mean_lat)

#first two arugments are the geographical coordinates .i.e. Latitude and Longitude
#and the zoom resolution
gmap = gmplot.GoogleMapPlotter(mean_lat, mean_lon, 18, map_type='satellite') #satellite view

#gmap.apikey = 'AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8'
gmap.scatter(lat_list, lon_list, size=0.5, marker = False, color = 'red') #plot first 2000 points red

#location where you want to save your file.
gmap.draw("/home/asl-laptop/workspace/gps_data/map05.html")
