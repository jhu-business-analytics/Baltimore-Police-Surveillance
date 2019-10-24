from geopy.geocoders import Nominatim
import csv
import re
import math

f = open("crimes_per_camera.csv", "a")
regex = re.compile('[^\w ]')

import csv
from collections import defaultdict

columns = defaultdict(list) # each value in each column is appended to a list

with open('counter_crimes.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v) # append the value into the appropriate list
                                 # based on column name k

print(float(columns["Latitude"][0]))
print(float(columns["Longitude"][0]))
print(float(columns["LAT"][0]))
print(float(columns["LONG"][0]))
crime_seen =  [False for x in range(1000)]
#raise SystemExit
for i in range(592): #number of cameras
	count = 0
	for j in range(1000): #number of crimes
		lat_100m = 0.01 #2000 * 0.001
		long_100m = 0.081 * (40075 * math.cos(float(columns["Latitude"][i]) * (180/math.pi))) / 360
		
		if  (float(columns["LAT"][j]) > float(columns["Latitude"][i]) - lat_100m) and \
			(float(columns["LAT"][j]) < float(columns["Latitude"][i]) + lat_100m) and \
			(float(columns["LONG"][j]) > float(columns["Longitude"][i]) - long_100m) and \
			(float(columns["LONG"][j]) < float(columns["Longitude"][i]) + long_100m):
				count += 1
				crime_seen[j] = True;
	#print(count)


seen = 0
for y in range(1000):
	if crime_seen[y] == True:
		seen += 1

print("Cameras saw ")
print(seen)
print(" / 1000 crimes")

f.close()