# Baltimore Police Surveillance
## Proposed Surveillance Planes
The Baltimore Police Department has proposed the use of controversial surveillance planes. These planes would track movement of cars, people, and so on from crimes scenes in order to determine camera feeds that would catch details of suspects. Will these planes be effective? Our analysis found that out of 1,000 crimes, only a relatively small proportion of crimes occur within 100, 500, and 1000 meters of a camera.

This README includes the following major sections:
- Challenge/problem section
- Solution section
- Suggestion section
- Additional Information

# Why is this a Challenge/Problem?
The proposed surveillance planes would cost $2.2 million each year. Although it would be privately funded, the money may be well spent elsewhere. However, if these surveillance planes can be effective, crime would potentially be reduced and crimes could be solves more efficiently and at a higher rate. This is also an issue of balancing drawbacks of reduced privacy for citizens with a potentially lower crime rate and higher crime closure rate. The issue of whether or not surveillance planes should be used affects not only the Baltimore Police Department but all Baltimore City inhabitants as well.

Useful Articles:
- [Baltimore Sun - City Support for Surveillance Planes](https://www.baltimoresun.com/news/crime/bs-md-ci-cr-poll-on-planes-20191014-mmot33qvm5f7pdwznim3qrx4oq-story.html)
- [Baltimore Sun - Persistent Problems with Surveillance](https://www.baltimoresun.com/opinion/editorial/bs-ed-bpd-surveillance-20170214-story.html)
- [The Guardian - FBI Surveillance Planes over US Cities](https://www.theguardian.com/us-news/2015/jun/02/fbi-surveillance-government-planes-cities)
- [Bloomberg - Secret Testing of Surveillance Planes in Baltimore](https://www.bloomberg.com/features/2016-baltimore-secret-surveillance/)
- [CBS Local, Baltimore - Push for Surveillance Planes](https://baltimore.cbslocal.com/2019/08/13/remember-the-surveillance-plane-that-flew-over-baltimore-it-could-fly-again/)
- [Baltimore Police Department - CitiWatch Camera Partnership](https://www.baltimorepolice.org/community/citiwatch-community-partnership-overview)
- [Baltimore Sun - CitiWatch Cameras](https://www.baltimoresun.com/news/crime/bs-md-ci-citiwatch-cameras-20190424-story.html)

Data Sources:
[Baltimore City Open Data](https://data.baltimorecity.gov/)
- [CitiWatch Camera Dataset](https://data.baltimorecity.gov/Public-Safety/CCTV-Cameras/y3f4-umna)
- [Violent Crime Dataset, 2014](https://data.baltimorecity.gov/Crime/Violent-Crime-2014-YTD-Heat-Map/59fg-ary5)

# Our Solution
We created various pivot tables based on the - [Violent Crime Dataset](https://data.baltimorecity.gov/Crime/Violent-Crime-2014-YTD-Heat-Map/59fg-ary5).

## Pivot Table Analysis
We created numerous pivot tables to better visualize the dataset. We found that the majority of crimes occur at night, and in the Northeast and Southeast districts.

### Crimes per Month
![crimes per month](https://github.com/reecewgriffith/Baltimore-Police-Surveillance/blob/master/crimes_per_month.png)

### Crimes per District
![crimes per_district bar](https://github.com/reecewgriffith/Baltimore-Police-Surveillance/blob/master/crime_distr_district_bar.png)

![crimes per_district pie](https://github.com/reecewgriffith/Baltimore-Police-Surveillance/blob/master/crime_distr_district_pie.png)

### Crimes by Day and Night
![crimes day and night month](https://github.com/reecewgriffith/Baltimore-Police-Surveillance/blob/master/crimes_day_night_month.png)

![crimes day and night district](https://github.com/reecewgriffith/Baltimore-Police-Surveillance/blob/master/crimes_day_night_district.png)

## Cluster Analysis
We performed clustering analysis on three different anchor sets: crime type, district, and neighborhood. This provides a simpler way to study the various crime types, disctricts, and neighborhoods of Baltimore. Each anchor serves as a representative of the other crime types, districts, or neighborhoods it represents. This will make it easier for the Baltimore Police department to manage patrols and other such activities.

### Crime Type:

| Anchor | Description | Average Latitude |	Average Longitude |	% of Crimes in Daytime |	% of Crimes in Nighttime |	% of Crimes in Fall |	% of Crimes in Winter |	% of Crimes in Spring |	% of Crimes in Summer |
| ------ | ----------- | ---------------- | ----------------- | ------------------------------- | ----------------------------------- | ---------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| 5	| ROBBERY - COMMERCIAL	| 1.324890724	| -1.328155383	| 2.128211772	| -2.128211772	| -0.537335705	| -0.358477321 |	-0.169978668 |	0.534428439 |
| 2	| HOMICIDE	| -1.914982968	| 1.913482349	| -0.848833783	| 0.848833783	| -0.765568719 |	0.023037538	| -2.209080383	| 1.765513852 |
| 7	| ROBBERY - STREET	| 0.122902836	| -0.104250452	| 0.260553951	| -0.260553951	| 0.693194007	| -0.508324696 | 	0.375331936	| -0.224329586 |

| Description | Cluster |
| ----------- | ------ |
| AGG. ASSAULT |	3 |
| HOMICIDE |	2 |
| RAPE |	3 |
| ROBBERY - CARJACKING |	3 |
| ROBBERY - COMMERCIAL |	1 |
| ROBBERY - RESIDENCE	| 3 |
| ROBBERY - STREET |	3 |
| SHOOTING	| 3 |

### District:

| Anchor | Description | Average Latitude |	Average Longitude |	% of Crimes in Daytime |	% of Crimes in Nighttime |	% of Crimes in Fall |	% of Crimes in Winter |	% of Crimes in Spring |	% of Crimes in Summer |
| ------ | ----------- | ---------------- | ----------------- | ------------------------------- | ----------------------------------- | ---------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| 7 |	SOUTHERN	| 0.035277751	| -0.054845041	| -0.538965665	| 0.538965665	| -0.590171125 |	0.080835878	| 0.436440822 | 	| 0.020732752 |
| 1	| CENTRAL	| -0.140874451 |	0.12746857	| 0.289375281	| -0.289375281 | 	1.327527375	| -0.313203762	| 0.602305331 |	-1.326427772 |
| 9	| WESTERN |	1.241590087	| -1.264783063	| 1.19475154	| -1.19475154	| -1.22292041	| 1.297408411	| -0.82343211	| 0.43494838 |

| District | Cluster |
| -------- | ------ |
| CENTRAL	| 2	|
| EASTERN	| 3	|
| NORTHEAST	| 1	|
| NORTHERN	| 1	|
| NORTHWEST	| 1	|
| SOUTHEAST	| 1	|
| SOUTHERN	| 1	|
| SOUTHWEST	| 2	|
| WESTERN	| 3	|

### Neighborhood:

| Anchor	|	Neighborhood | AGG. ASSAULT |	HOMICIDE	| RAPE |	ROBBERY - CARJACKING |	ROBBERY - COMMERCIAL |	ROBBERY - RESIDENCE	| ROBBERY - STREET |	SHOOTING |
| ------- | ------------ | ------------ | ---------- | ---- | --------------------- | --------------------- | -------------------- | ---------------- | -------- |
| 65	| DRUID HEIGHTS |	0.235718926 |	0.235718926	| -0.00821465	| -0.303204054	| -0.097762223 |	-0.260428539 |	-0.216698689 |	-0.045683609 | -0.045683609 |
| 125 |	KESWICK |	-2.145351679	| -0.537913652	| -0.34162476	| -0.303204054 | 	6.524482051	| -0.790032836 |	-1.477117408 |	-0.596442991 | -0.596442991 |
| 44	| CHARLES VILLAGE	| -1.001885145 |	-0.319530882 |	0.225072304	| -0.037280279 |	0.098073995	| -0.339948704 |	1.108938547 |	-0.440973375 | -0.440973375 |
| 13 |	BEECHFIELD |	0.394715202	| -0.537913652	| 0.134961464	| -0.303204054 |	-0.571033082	| 1.482653471	| -0.351861701	| 0.190828678 | 0.190828678 |
| 61 |	DICKEYVILLE	| -2.145351679	| -0.537913652	| -0.34162476	| 13.76683692	| -0.571033082	| -0.790032836 | -1.477117408	| -0.596442991 | -0.596442991 |


There are over 250 neighborhoods, so the individual clusters for each neighborhood coulf not be shown here. This information can easily be found in our clusters datasheet.

## Camera Data Analysis
![unique crimes seen](https://github.com/reecewgriffith/Baltimore-Police-Surveillance/blob/master/unique_crimes_seen.png)

![non unique crimes seen](https://github.com/reecewgriffith/Baltimore-Police-Surveillance/blob/master/nonunique_crimes_seen.png)

The first figure shows that only 120/1000 unique crimes occur within 100 meters of a camera. However, it is reasonable to think that persons of interest leaving the location of a crime coul pass within this 100 meter radius eventually. The number of crimes seen is likely higher than we are reporting.

The second figure shows that, while only 120 unique crimes occur within 100 meters of a camera, there can be multiple crimes that occur within the radius of the same camera. For example, at a 100 meter radius, only 120 unique crimes occur, but 891 non-unique crimes occur within that same radius.

# Future Suggestions
After analyzing numerous sources of data and creating untilizes multiple methods of visualization and analysis, it is our recommendation that the Baltimore Police Department move forward with the proposed surveillance plane solution. While only a small percentage of unique crimes occur within a reasonable radius of a camera, many non-unique crimes occur within that same radius. These crimes that occur within this radius can easily be linked to their corresponding CitiWatch camera using the tracking data from these surveillance planes.

# Additional Information

## Tools Used
- [Geopy](https://geopy.readthedocs.io/en/stable/), a python library used for translating adresses to lat/long coordinates
- [addr_to_coord.py](https://github.com/reecewgriffith/Baltimore-City-Data-Project/blob/master/addr_to_coord.py), script using geopy to convert addresses of crimes to coordinates
- [count_crimes_per_camera.py](https://github.com/reecewgriffith/Baltimore-City-Data-Project/blob/master/count_crimes_per_camera.py), script to count the number of crimes within various radii of each camera, also counts the proportion of unique crimes seen out of the total number of crimes

