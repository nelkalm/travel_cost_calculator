# import pandas as pd

# airfare_df = pd.read_csv(
#     '/Users/nelsonlu/Documents/CdphTravelCostCalculator/data/airfare.csv')

# perdiem_df = pd.read_csv(
#     '/Users/nelsonlu/Documents/CdphTravelCostCalculator/data/perdiem24.csv')

# airfare_dict = airfare_df.to_dict(orient='list')
# perdiem_dict = perdiem_df.to_dict(orient='list')

# print({key: airfare_dict[key][:10] for key in airfare_dict})

# result = perdiem_df[(perdiem_df['State'] == 'AL') & (
#     perdiem_df['Destination'] == 'Birmingham')]
# print(result)

input = """
AL	Birmingham
AL	Gulf Shores
AL	Huntsville
AL	Mobile
AR	Hot Springs
AZ	Kayenta
AZ	Sedona
AZ	Tucson
CA	Death Valley
CA	Fresno
CA	Los Angeles
CA	Mammoth Lakes
CA	Monterey
CA	Napa
CA	Oakhurst
CA	Oakland
CA	Palm Springs
CA	Sacramento
CA	San Diego
CA	San Francisco
CA	San Luis Obispo
CA	Santa Barbara
CA	Santa Cruz
CA	Santa Monica
CA	Santa Rosa
CA	South Lake Tahoe
CA	Stockton
CA	Tahoe City
CA	Truckee
CA	Visalia
CA	Yosemite National Park
CO	Aspen
CO	Colorado Springs
CO	Cortez
CO	Douglas
CO	Durango
CO	Grand Lake
CO	Montrose
CO	Steamboat Springs
CO	Telluride
CO	Vail
CT	Hartford
CT	New Haven
DC	District of Columbia
DE	Lewes
DE	Wilmington
FL	Bradenton
FL	Cocoa Beach
FL	Daytona Beach
FL	Fort Lauderdale
FL	Fort Myers
FL	Gulf Breeze
FL	Key West
FL	Miami
FL	Naples
FL	Orlando
FL	Panama City
FL	Pensacola
FL	Punta Gorda
FL	Sarasota
FL	Sebring
FL	St. Augustine
FL	Stuart
FL	Tallahassee
FL	Vero Beach
GA	Athens
GA	Atlanta
GA	Augusta
GA	Marietta
GA	Savannah
IA	Dallas
IA	Des Moines
ID	Boise
ID	Coeur d'Alene
IL	Chicago
IL	Oak Brook Terrace
IN	Bloomington
IN	Ft. Wayne
KY	Boone
KY	Kenton
KY	Lexington
KY	Louisville
LA	New Orleans
MA	Andover
MA	Falmouth
MA	Hyannis
MA	Martha's Vineyard
MA	Nantucket
MA	Northampton
MA	Pittsfield
MA	Quincy
MA	Springfield
MA	Worcester
MD	Annapolis
MD	Baltimore City
MD	Centreville
MD	Columbia
MD	Ocean City
ME	Portland
MI	Ann Arbor
MI	Detroit
MI	Grand Rapids
MI	Holland
MI	Mackinac Island
MI	Midland
MI	Muskegon
MI	Petoskey
MI	South Haven
MI	Traverse City
MN	Duluth
MN	Rochester
MO	Kansas City
MO	St. Louis
MS	Oxford
MS	Southaven
MS	Starkville
MT	Helena
MT	Missoula
NC	Asheville
NC	Chapel Hill
NC	Charlotte
NC	Durham
NC	Fayetteville
NC	Greensboro
NC	Kill Devil Hills
NC	Raleigh
NE	Omaha
NH	Concord
NH	Conway
NH	Laconia
NH	Manchester
NH	Portsmouth
NJ	Flemington
NJ	Newark
NJ	Parsippany
NJ	Somerset
NJ	Toms River
NM	Albuquerque
NM	Carlsbad
NM	Santa Fe
NM	Taos
NV	Las Vegas
NY	Albany
NY	Binghamton
NY	Buffalo
NY	Glens Falls
NY	Ithaca
NY	Kingston
NY	Lake Placid
NY	New York City
NY	Niagara Falls
NY	Poughkeepsie
NY	Troy
NY	West Point
OH	Canton
OH	Cincinnati
OH	Cleveland
OH	Columbus
OH	Hamilton
OH	Mentor
OH	Sandusky
OK	Oklahoma City
OR	Beaverton
OR	Bend
OR	Clackamas
OR	Lincoln City
OR	Seaside
PA	Bucks
PA	Gettysburg
PA	Harrisburg
PA	Hershey
PA	Lancaster
PA	Montgomery
PA	Philadelphia
PA	Pittsburgh
PA	Reading
PA	State College
SC	Charleston
SC	Hilton Head
SC	Myrtle Beach
SD	Rapid City
TN	Chattanooga
TN	Knoxville
TN	Memphis
TN	Nashville
TX	Austin
TX	Big Spring
TX	Galveston
TX	Houston
TX	Pecos
TX	Plano
TX	San Antonio
TX	South Padre Island
TX	Waco
UT	Moab
UT	Park City
UT	Provo
UT	Salt Lake City
VA	Blacksburg
VA	Charlottesville
VA	Loudoun
VA	Lynchburg
VA	Richmond
VA	Roanoke
VA	Virginia Beach
VA	Wallops Island
VT	Burlington
VT	Montpelier
VT	Stowe
VT	White River Junction
WA	Ocean Shores
WA	Seattle
WA	Spokane
WA	Tacoma
WA	Vancouver
WI	Madison
WI	Milwaukee
WI	Sturgeon Bay
WI	Wisconsin Dells
WV	Charles Town
WY	Cody
"""

# Convert the input string to a dictionary
city_dict = {}
for line in input.strip().split('\n'):
    parts = line.split()  # Split each line into parts
    state = parts[0]  # First part is the state
    # Join the remaining parts to form the city name
    city = ' '.join(parts[1:])
    city_dict[(city, state)] = city  # Create dictionary entry

# Print the dictionary in the specified format
print(city_dict)
# for key, value in city_dict.items():
#     print(f"({key}): \"{value}\",")
