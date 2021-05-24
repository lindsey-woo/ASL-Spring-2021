#import headers
import csv
import gmplot
import math
from gmplot import *

lon_list = []
lat_list = []

# with open('position_jackal.csv', newline = '') as csvfile: #read the csv file
with open('out4.csv', 'r') as csvfile: #read the csv file

    reader = csv.DictReader(csvfile) #dataframe which csv is written into
    #iterate over each 'row' in the dataframe
    #each row is a python dictionary which contains:
    #dict_keys([' Ellipsoid Alt (m)', ' Solution Type', ' Lon (deg)', 'GPS Time (sec)', ' Lat (deg)'])

    lon_list = [] #lists to store latitude and longitude
    lat_list = []

    lon_sum = 0. #initialize sums to calculate average
    lat_sum = 0.

    for row in reader: #iterate over the rows
        lon = row['Longitude'] #extract longitude and latitude and assign them to variables
        lat = row['Latitude']

        lon_sum += float(lon) #increase sum to calculate average
        lat_sum += float(lat)

        lon_list.append(float(lon)) #append to longitude list
        lat_list.append(float(lat)) #append to latitude list

mean_lon = lon_sum / len(lon_list) #average longitude
mean_lat = lat_sum / len(lat_list) #average latitude

print("mean longitude: ", mean_lon, "mean latitude: ", mean_lat)

lon_list_atlas = []
lat_list_atlas = []

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
gmap = gmplot.GoogleMapPlotter(mean_lat, mean_lon, 18, map_type='satellite') #satellite view

#gmap.apikey = 'AIzaSyDeRNMnZ__VnQDiATiuz4kPjF_c9r1kWe8'
gmap.scatter(lat_list, lon_list, size=0.5, marker = False, color = 'red') #plot first 2000 points red
gmap.scatter(lat_list, lon_list, size=0.5, marker = False, color = 'red') #plot last 2000 points blue
#gmap.scatter(lat_list_atlas[:4000], lon_list_atlas[:4000], size=1, marker = False, color = 'blue') #plot first 2000 points red
#gmap.scatter(lat_list_atlas[4000:-1], lon_list_atlas[4000:-1], size=1, marker = False, color = 'blue') #plot last 2000 points blue

#location where you want to save your file.
gmap.draw("/home/asl-laptop/workspace/gps_data/map04.html")
