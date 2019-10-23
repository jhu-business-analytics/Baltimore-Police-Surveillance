from geopy.geocoders import Nominatim
import csv
import re

f = open("crime_coords.csv", "a")
regex = re.compile('[^\w ]')

with open('crime_addr.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	count = 0
	for row in readCSV:
		
		if count == 0:
			row = "1200 UNION AV"
		else:
			row = str(row)
			row = regex.sub('', row)
		count += 1

		address = row +  " Baltimore, MD"
		geolocator = Nominatim(user_agent="specify_your_app_name_here",timeout=1)
		location = geolocator.geocode(address)

		if location is not None:
			f.write(str((row, location.latitude, location.longitude)) + "\n")
		else:
			f.write("\n")
f.close()