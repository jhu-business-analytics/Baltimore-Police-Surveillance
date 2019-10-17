from geopy.geocoders import Nominatim
import csv
import re

f = open("coords.csv", "a")
regex = re.compile('[^\w ]')

with open('addresses.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	count = 0
	for row in readCSV:
		
		if count == 0:
			row = "900 S CATON AV"
		else:
			row = str(row)
			row = regex.sub('', row)
		count += 1

		address = row +  " Baltimore, MD"
		geolocator = Nominatim(user_agent="specify_your_app_name_here",timeout=1000)
		location = geolocator.geocode(address)

		if location is not None:
			#print(row)
			#print((location.latitude, location.longitude))
			
			f.write(str((location.latitude, location.longitude)) + "\n")
f.close()