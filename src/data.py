reimbursement_rates = {
    'Group 1': {'Lodging': 250, 'Transportation': 55, 'Per Diem': 65},
    'Group 2': {'Lodging': 225, 'Transportation': 50, 'Per Diem': 60},
    'Group 3': {'Lodging': 150, 'Transportation': 45, 'Per Diem': 55},
    'Group 4': {'Lodging': 125, 'Transportation': 40, 'Per Diem': 50},
    'Group 5': {'Lodging': 125, 'Transportation': 40, 'Per Diem': 50}
}

state_abbreviations = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming'
}

city_mapping = {
    ("Phoenix", "AZ"): "Phoenix / Scottsdale",
    ("Scottsdale", "AZ"): "Phoenix / Scottsdale",
    ("Grand Canyon", "AZ"): "Grand Canyon / Flagstaff",
    ("Flagstaff", "AZ"): "Grand Canyon / Flagstaff",
    ("Antioch", "CA"): "Antioch / Brentwood / Concord",
    ("Brentwood", "CA"): "Antioch / Brentwood / Concord",
    ("Concord", "CA"): "Antioch / Brentwood / Concord",
    ("Bakersfield", "CA"): "Bakersfield / Ridgecrest",
    ("Ridgecrest", "CA"): "Bakersfield / Ridgecrest",
    ("Barstow", "CA"): "Barstow / Ontario / Victorville",
    ("Ontario", "CA"): "Barstow / Ontario / Victorville",
    ("Victorville", "CA"): "Barstow / Ontario / Victorville",
    ("Eureka", "CA"): "Eureka / Arcata / McKinleyville",
    ("Arcata", "CA"): "Eureka / Arcata / McKinleyville",
    ("McKinleyville", "CA"): "Eureka / Arcata / McKinleyville",
    ("Mill Valley", "CA"): "Mill Valley / San Rafael / Novato",
    ("San Rafael", "CA"): "Mill Valley / San Rafael / Novato",
    ("Novato", "CA"): "Mill Valley / San Rafael / Novato",
    ("Point Arena", "CA"): "Point Arena / Gualala",
    ("Gualala", "CA"): "Point Arena / Gualala",
    ("San Mateo", "CA"): "San Mateo / Foster City / Belmont",
    ("Foster City", "CA"): "San Mateo / Foster City / Belmont",
    ("Belmont", "CA"): "San Mateo / Foster City / Belmont",
    ("Sunnyvale", "CA"): "Sunnyvale / Palo Alto / San Jose",
    ("Palo Alto", "CA"): "Sunnyvale / Palo Alto / San Jose",
    ("San Jose", "CA"): "Sunnyvale / Palo Alto / San Jose",
    ("West Sacramento", "CA"): "West Sacramento / Davis",
    ("Davis", "CA"): "West Sacramento / Davis",
    ("Boulder", "CO"): "Boulder / Broomfield",
    ("Broomfield", "CO"): "Boulder / Broomfield",
    ("Crested Butte", "CO"): "Crested Butte / Gunnison",
    ("Gunnison", "CO"): "Crested Butte / Gunnison",
    ("Denver", "CO"): "Denver / Aurora",
    ("Aurora", "CO"): "Denver / Aurora",
    ("Fort Collins", "CO"): "Fort Collins / Loveland",
    ("Loveland", "CO"): "Fort Collins / Loveland",
    ("Silverthorne", "CO"): "Silverthorne / Breckenridge",
    ("Breckenridge", "CO"): "Silverthorne / Breckenridge",
    ("Bridgeport", "CT"): "Bridgeport / Danbury",
    ("Danbury", "CT"): "Bridgeport / Danbury",
    ("New London", "CT"): "New London / Groton",
    ("Groton", "CT"): "New London / Groton",
    ("Boca Raton", "FL"): "Boca Raton / Delray Beach / Jupiter",
    ("Delray Beach", "FL"): "Boca Raton / Delray Beach / Jupiter",
    ("Jupiter", "FL"): "Boca Raton / Delray Beach / Jupiter",
    ("Fort Walton Beach", "FL"): "Fort Walton Beach / De Funiak Springs",
    ("De Funiak Springs", "FL"): "Fort Walton Beach / De Funiak Springs",
    ("Tampa", "FL"): "Tampa / St. Petersburg",
    ("St. Petersburg", "FL"): "Tampa / St. Petersburg",
    ("Jekyll Island", "GA"): "Jekyll Island / Brunswick",
    ("Brunswick", "GA"): "Jekyll Island / Brunswick",
    ("Sun Valley", "ID"): "Sun Valley / Ketchum",
    ("Ketchum", "ID"): "Sun Valley / Ketchum",
    ("Bolingbrook", "IL"): "Bolingbrook / Romeoville / Lemont",
    ("Romeoville", "IL"): "Bolingbrook / Romeoville / Lemont",
    ("Lemont", "IL"): "Bolingbrook / Romeoville / Lemont",
    ("East St. Louis", "IL"): "East St. Louis / O'Fallon / Fairview Heights",
    ("O'Fallon", "IL"): "East St. Louis / O'Fallon / Fairview Heights",
    ("Fairview Heights", "IL"): "East St. Louis / O'Fallon / Fairview Heights",
    ("Indianapolis", "IN"): "Indianapolis / Carmel",
    ("Carmel", "IN"): "Indianapolis / Carmel",
    ("Lafayette", "IN"): "Lafayette / West Lafayette",
    ("West Lafayette", "IN"): "Lafayette / West Lafayette",
    ("Kansas City", "KS"): "Kansas City / Overland Park",
    ("Overland Park", "KS"): "Kansas City / Overland Park",
    ("Alexandria", "LA"): "Alexandria / Leesville / Natchitoches",
    ("Leesville", "LA"): "Alexandria / Leesville / Natchitoches",
    ("Natchitoches", "LA"): "Alexandria / Leesville / Natchitoches",
    ("Boston", "MA"): "Boston / Cambridge",
    ("Cambridge", "MA"): "Boston / Cambridge",
    ("Burlington", "MA"): "Burlington / Woburn",
    ("Woburn", "MA"): "Burlington / Woburn",
    ("Plymouth", "MA"): "Plymouth / Taunton / New Bedford",
    ("Tauton", "MA"): "Plymouth / Taunton / New Bedford",
    ("New Bedford", "MA"): "Plymouth / Taunton / New Bedford",
    ("Aberdeen", "MD"): "Aberdeen / Bel Air / Belcamp",
    ("Bel Air", "MD"): "Aberdeen / Bel Air / Belcamp",
    ("Belcamp", "MD"): "Aberdeen / Bel Air / Belcamp",
    ("Cambridge", "MD"): "Cambridge / St. Michaels",
    ("St. Michaels", "MD"): "Cambridge / St. Michaels",
    ("Bar Harbor", "ME"): "Bar Harbor / Rockport",
    ("Rockport", "ME"): "Bar Harbor / Rockport",
    ("Kennebunk", "ME"): "Kennebunk / Kittery / Sanford",
    ("Kittery", "ME"): "Kennebunk / Kittery / Sanford",
    ("Sanford", "ME"): "Kennebunk / Kittery / Sanford",
    ("Pontiac", "MI"): "Pontiac / Auburn Hills",
    ("Auburn Hills", "MI"): "Pontiac / Auburn Hills",
    ("Minneapolis", "MN"): "Minneapolis / St. Paul",
    ("St. Paul", "MN"): "Minneapolis / St. Paul",
    ("Big Sky", "MT"): "Big Sky / West Yellowstone / Gardiner",
    ("West Yellowstone", "MT"): "Big Sky / West Yellowstone / Gardiner",
    ("Gardiner", "MT"): "Big Sky / West Yellowstone / Gardiner",
    ("Kalispell", "MT"): "Kalispell / Whitefish",
    ("Whitefish", "MT"): "Kalispell / Whitefish",
    ("Atlantic Beach", "NC"): "Atlantic Beach / Morehead City",
    ("Morehead City", "NC"): "Atlantic Beach / Morehead City",
    ("Lebanon", "NH"): "Lebanon / Lincoln / West Lebanon",
    ("Lincoln", "NH"): "Lebanon / Lincoln / West Lebanon",
    ("West Lebanon", "NH"): "Lebanon / Lincoln / West Lebanon",
    ("Cherry Hill", "NJ"): "Cherry Hill / Moorestown",
    ("Moorestown", "NJ"): "Cherry Hill / Moorestown",
    ("Eatontown", "NJ"): "Eatontown / Freehold",
    ("Freehold", "NJ"): "Eatontown / Freehold",
    ("Edison", "NJ"): "Edison / Piscataway",
    ("Piscataway", "NJ"): "Edison / Piscataway",
    ("Princeton", "NJ"): "Princeton / Trenton",
    ("Trenton", "NJ"): "Princeton / Trenton",
    ("Springfield", "NJ"): "Springfield / Cranford / New Providence",
    ("Cranford", "NJ"): "Springfield / Cranford / New Providence",
    ("New Providence", "NJ"): "Springfield / Cranford / New Providence",
    ("Incline Village", "NV"): "Incline Village / Reno / Sparks",
    ("Reno", "NV"): "Incline Village / Reno / Sparks",
    ("Sparks", "NV"): "Incline Village / Reno / Sparks",
    ("Floral Park", "NY"): "Floral Park / Garden City / Great Neck",
    ("Garden City", "NY"): "Floral Park / Garden City / Great Neck",
    ("Great Neck", "NY"): "Floral Park / Garden City / Great Neck",
    ("Nyack", "NY"): "Nyack / Palisades",
    ("Palisades", "NY"): "Nyack / Palisades",
    ("Riverhead", "NY"): "Riverhead / Ronkonkoma / Melville",
    ("Ronkonkoma", "NY"): "Riverhead / Ronkonkoma / Melville",
    ("Melville", "NY"): "Riverhead / Ronkonkoma / Melville",
    ("Saratoga Springs", "NY"): "Saratoga Springs / Schenectady",
    ("Schenectady", "NY"): "Saratoga Springs / Schenectady",
    ("Syracuse", "NY"): "Syracuse / Oswego",
    ("Oswego", "NY"): "Syracuse / Oswego",
    ("Tarrytown", "NY"): "Tarrytown / White Plains / New Rochelle",
    ("White Plains", "NY"): "Tarrytown / White Plains / New Rochelle",
    ("New Rochelle", "NY"): "Tarrytown / White Plains / New Rochelle",
    ("Dayton", "OH"): "Dayton / Fairborn",
    ("Fairborn", "OH"): "Dayton / Fairborn",
    ("Eugene", "OR"): "Eugene / Florence",
    ("Florence", "OR"): "Eugene / Florence",
    ("Allentown", "PA"): "Allentown / Easton / Bethlehem",
    ("Easton", "PA"): "Allentown / Easton / Bethlehem",
    ("Bethlehem", "PA"): "Allentown / Easton / Bethlehem",
    ("Chester", "PA"): "Chester / Radnor / Essington",
    ("Radnor", "PA"): "Chester / Radnor / Essington",
    ("Essington", "PA"): "Chester / Radnor / Essington",
    ("Malvern", "PA"): "Malvern / Frazer / Berwyn",
    ("Frazer", "PA"): "Malvern / Frazer / Berwyn",
    ("Berwyn", "PA"): "Malvern / Frazer / Berwyn",
    ("East Greenwich", "RI"): "East Greenwich / Warwick",
    ("Warwick", "RI"): "East Greenwich / Warwick",
    ("Jamestown", "RI"): "Jamestown / Middletown / Newport",
    ("Middletown", "RI"): "Jamestown / Middletown / Newport",
    ("Newport", "RI"): "Jamestown / Middletown / Newport",
    ("Providence", "RI"): "Providence / Bristol",
    ("Bristol", "RI"): "Providence / Bristol",
    ("Deadwood", "SD"): "Deadwood / Spearfish",
    ("Spearfish", "SD"): "Deadwood / Spearfish",
    ("Brentwood", "TN"): "Brentwood / Franklin",
    ("Franklin", "TN"): "Brentwood / Franklin",
    ("Arlington", "TX"): "Arlington / Fort Worth / Grapevine",
    ("Fort Worth", "TX"): "Arlington / Fort Worth / Grapevine",
    ("Grapevine", "TX"): "Arlington / Fort Worth / Grapevine",
    ("Midland", "TX"): "Midland / Odessa",
    ("Odessa", "TX"): "Midland / Odessa",
    ("Williamsburg", "VA"): "Williamsburg / York",
    ("York", "VA"): "Williamsburg / York",
    ("Everett", "WA"): "Everett / Lynnwood",
    ("Lynnwood", "WA"): "Everett / Lynnwood",
    ("Olympia", "WA"): "Olympia / Tumwater",
    ("Tumwater", "WA"): "Olympia / Tumwater",
    ("Port Angeles", "WA"): "Port Angeles / Port Townsend",
    ("Port Townsend", "WA"): "Port Angeles / Port Townsend",
    ("Pinedale", "WY"): "Jackson / Pinedale",
    ("Jackson", "WY"): "Jackson / Pinedale",
    ('Birmingham', 'AL'): 'Birmingham', ('Gulf Shores', 'AL'): 'Gulf Shores', ('Huntsville', 'AL'): 'Huntsville', ('Mobile', 'AL'): 'Mobile', ('Hot Springs', 'AR'): 'Hot Springs', ('Kayenta', 'AZ'): 'Kayenta', ('Sedona', 'AZ'): 'Sedona', ('Tucson', 'AZ'): 'Tucson', ('Death Valley', 'CA'): 'Death Valley', ('Fresno', 'CA'): 'Fresno', ('Los Angeles', 'CA'): 'Los Angeles', ('Mammoth Lakes', 'CA'): 'Mammoth Lakes', ('Monterey', 'CA'): 'Monterey', ('Napa', 'CA'): 'Napa', ('Oakhurst', 'CA'): 'Oakhurst', ('Oakland', 'CA'): 'Oakland', ('Palm Springs', 'CA'): 'Palm Springs', ('Sacramento', 'CA'): 'Sacramento', ('San Diego', 'CA'): 'San Diego', ('San Francisco', 'CA'): 'San Francisco', ('San Luis Obispo', 'CA'): 'San Luis Obispo', ('Santa Barbara', 'CA'): 'Santa Barbara', ('Santa Cruz', 'CA'): 'Santa Cruz', ('Santa Monica', 'CA'): 'Santa Monica', ('Santa Rosa', 'CA'): 'Santa Rosa', ('South Lake Tahoe', 'CA'): 'South Lake Tahoe', ('Stockton', 'CA'): 'Stockton', ('Tahoe City', 'CA'): 'Tahoe City', ('Truckee', 'CA'): 'Truckee', ('Visalia', 'CA'): 'Visalia', ('Yosemite National Park', 'CA'): 'Yosemite National Park', ('Aspen', 'CO'): 'Aspen', ('Colorado Springs', 'CO'): 'Colorado Springs', ('Cortez', 'CO'): 'Cortez', ('Douglas', 'CO'): 'Douglas', ('Durango', 'CO'): 'Durango', ('Grand Lake', 'CO'): 'Grand Lake', ('Montrose', 'CO'): 'Montrose', ('Steamboat Springs', 'CO'): 'Steamboat Springs', ('Telluride', 'CO'): 'Telluride', ('Vail', 'CO'): 'Vail', ('Hartford', 'CT'): 'Hartford', ('New Haven', 'CT'): 'New Haven', ('District of Columbia', 'DC'): 'District of Columbia', ('Lewes', 'DE'): 'Lewes', ('Wilmington', 'DE'): 'Wilmington', ('Bradenton', 'FL'): 'Bradenton', ('Cocoa Beach', 'FL'): 'Cocoa Beach', ('Daytona Beach', 'FL'): 'Daytona Beach', ('Fort Lauderdale', 'FL'): 'Fort Lauderdale', ('Fort Myers', 'FL'): 'Fort Myers', ('Gulf Breeze', 'FL'): 'Gulf Breeze', ('Key West', 'FL'): 'Key West', ('Miami', 'FL'): 'Miami', ('Naples', 'FL'): 'Naples', ('Orlando', 'FL'): 'Orlando', ('Panama City', 'FL'): 'Panama City', ('Pensacola', 'FL'): 'Pensacola', ('Punta Gorda', 'FL'): 'Punta Gorda', ('Sarasota', 'FL'): 'Sarasota', ('Sebring', 'FL'): 'Sebring', ('St. Augustine', 'FL'): 'St. Augustine', ('Stuart', 'FL'): 'Stuart', ('Tallahassee', 'FL'): 'Tallahassee', ('Vero Beach', 'FL'): 'Vero Beach', ('Athens', 'GA'): 'Athens', ('Atlanta', 'GA'): 'Atlanta', ('Augusta', 'GA'): 'Augusta', ('Marietta', 'GA'): 'Marietta', ('Savannah', 'GA'): 'Savannah', ('Dallas', 'IA'): 'Dallas', ('Des Moines', 'IA'): 'Des Moines', ('Boise', 'ID'): 'Boise', ("Coeur d'Alene", 'ID'): "Coeur d'Alene", ('Chicago', 'IL'): 'Chicago', ('Oak Brook Terrace', 'IL'): 'Oak Brook Terrace', ('Bloomington', 'IN'): 'Bloomington', ('Ft. Wayne', 'IN'): 'Ft. Wayne', ('Boone', 'KY'): 'Boone', ('Kenton', 'KY'): 'Kenton', ('Lexington', 'KY'): 'Lexington', ('Louisville', 'KY'): 'Louisville', ('New Orleans', 'LA'): 'New Orleans', ('Andover', 'MA'): 'Andover', ('Falmouth', 'MA'): 'Falmouth', ('Hyannis', 'MA'): 'Hyannis', ("Martha's Vineyard", 'MA'): "Martha's Vineyard", ('Nantucket', 'MA'): 'Nantucket', ('Northampton', 'MA'): 'Northampton', ('Pittsfield', 'MA'): 'Pittsfield', ('Quincy', 'MA'): 'Quincy', ('Springfield', 'MA'): 'Springfield', ('Worcester', 'MA'): 'Worcester', ('Annapolis', 'MD'): 'Annapolis', ('Baltimore City', 'MD'): 'Baltimore City', ('Centreville', 'MD'): 'Centreville', ('Columbia', 'MD'): 'Columbia', ('Ocean City', 'MD'): 'Ocean City', ('Portland', 'ME'): 'Portland', ('Ann Arbor', 'MI'): 'Ann Arbor', ('Detroit', 'MI'): 'Detroit', ('Grand Rapids', 'MI'): 'Grand Rapids', ('Holland', 'MI'): 'Holland', ('Mackinac Island', 'MI'): 'Mackinac Island', ('Midland', 'MI'): 'Midland', ('Muskegon', 'MI'): 'Muskegon', ('Petoskey', 'MI'): 'Petoskey', ('South Haven', 'MI'): 'South Haven', ('Traverse City', 'MI'): 'Traverse City', ('Duluth', 'MN'): 'Duluth', ('Rochester', 'MN'): 'Rochester', ('Kansas City', 'MO'): 'Kansas City', ('St. Louis', 'MO'): 'St. Louis', ('Oxford', 'MS'): 'Oxford', ('Southaven', 'MS'): 'Southaven', ('Starkville', 'MS'): 'Starkville', ('Helena', 'MT'): 'Helena', ('Missoula', 'MT'): 'Missoula', ('Asheville', 'NC'): 'Asheville', ('Chapel Hill', 'NC'): 'Chapel Hill', ('Charlotte', 'NC'): 'Charlotte', ('Durham', 'NC'): 'Durham', ('Fayetteville', 'NC'): 'Fayetteville', ('Greensboro', 'NC'): 'Greensboro', ('Kill Devil Hills', 'NC'): 'Kill Devil Hills', ('Raleigh', 'NC'): 'Raleigh', ('Omaha', 'NE'): 'Omaha', ('Concord', 'NH'): 'Concord', ('Conway', 'NH'): 'Conway', ('Laconia', 'NH'): 'Laconia', ('Manchester', 'NH'): 'Manchester', ('Portsmouth', 'NH'): 'Portsmouth', ('Flemington', 'NJ'): 'Flemington', ('Newark', 'NJ'): 'Newark', ('Parsippany', 'NJ'): 'Parsippany', ('Somerset', 'NJ'): 'Somerset', ('Toms River', 'NJ'): 'Toms River', ('Albuquerque', 'NM'): 'Albuquerque', ('Carlsbad', 'NM'): 'Carlsbad', ('Santa Fe', 'NM'): 'Santa Fe', ('Taos', 'NM'): 'Taos', ('Las Vegas', 'NV'): 'Las Vegas', ('Albany', 'NY'): 'Albany', ('Binghamton', 'NY'): 'Binghamton', ('Buffalo', 'NY'): 'Buffalo', ('Glens Falls', 'NY'): 'Glens Falls', ('Ithaca', 'NY'): 'Ithaca', ('Kingston', 'NY'): 'Kingston', ('Lake Placid', 'NY'): 'Lake Placid', ('New York City', 'NY'): 'New York City', ('Niagara Falls', 'NY'): 'Niagara Falls', ('Poughkeepsie', 'NY'): 'Poughkeepsie', ('Troy', 'NY'): 'Troy', ('West Point', 'NY'): 'West Point', ('Canton', 'OH'): 'Canton', ('Cincinnati', 'OH'): 'Cincinnati', ('Cleveland', 'OH'): 'Cleveland', ('Columbus', 'OH'): 'Columbus', ('Hamilton', 'OH'): 'Hamilton', ('Mentor', 'OH'): 'Mentor', ('Sandusky', 'OH'): 'Sandusky', ('Oklahoma City', 'OK'): 'Oklahoma City', ('Beaverton', 'OR'): 'Beaverton', ('Bend', 'OR'): 'Bend', ('Clackamas', 'OR'): 'Clackamas', ('Lincoln City', 'OR'): 'Lincoln City', ('Seaside', 'OR'): 'Seaside', ('Bucks', 'PA'): 'Bucks', ('Gettysburg', 'PA'): 'Gettysburg', ('Harrisburg', 'PA'): 'Harrisburg', ('Hershey', 'PA'): 'Hershey', ('Lancaster', 'PA'): 'Lancaster', ('Montgomery', 'PA'): 'Montgomery', ('Philadelphia', 'PA'): 'Philadelphia', ('Pittsburgh', 'PA'): 'Pittsburgh', ('Reading', 'PA'): 'Reading', ('State College', 'PA'): 'State College', ('Charleston', 'SC'): 'Charleston', ('Hilton Head', 'SC'): 'Hilton Head', ('Myrtle Beach', 'SC'): 'Myrtle Beach', ('Rapid City', 'SD'): 'Rapid City', ('Chattanooga', 'TN'): 'Chattanooga', ('Knoxville', 'TN'): 'Knoxville', ('Memphis', 'TN'): 'Memphis', ('Nashville', 'TN'): 'Nashville', ('Austin', 'TX'): 'Austin', ('Big Spring', 'TX'): 'Big Spring', ('Galveston', 'TX'): 'Galveston', ('Houston', 'TX'): 'Houston', ('Pecos', 'TX'): 'Pecos', ('Plano', 'TX'): 'Plano', ('San Antonio', 'TX'): 'San Antonio', ('South Padre Island', 'TX'): 'South Padre Island', ('Waco', 'TX'): 'Waco', ('Moab', 'UT'): 'Moab', ('Park City', 'UT'): 'Park City', ('Provo', 'UT'): 'Provo', ('Salt Lake City', 'UT'): 'Salt Lake City', ('Blacksburg', 'VA'): 'Blacksburg', ('Charlottesville', 'VA'): 'Charlottesville', ('Loudoun', 'VA'): 'Loudoun', ('Lynchburg', 'VA'): 'Lynchburg', ('Richmond', 'VA'): 'Richmond', ('Roanoke', 'VA'): 'Roanoke', ('Virginia Beach', 'VA'): 'Virginia Beach', ('Wallops Island', 'VA'): 'Wallops Island', ('Burlington', 'VT'): 'Burlington', ('Montpelier', 'VT'): 'Montpelier', ('Stowe', 'VT'): 'Stowe', ('White River Junction', 'VT'): 'White River Junction', ('Ocean Shores', 'WA'): 'Ocean Shores', ('Seattle', 'WA'): 'Seattle', ('Spokane', 'WA'): 'Spokane', ('Tacoma', 'WA'): 'Tacoma', ('Vancouver', 'WA'): 'Vancouver', ('Madison', 'WI'): 'Madison', ('Milwaukee', 'WI'): 'Milwaukee', ('Sturgeon Bay', 'WI'): 'Sturgeon Bay', ('Wisconsin Dells', 'WI'): 'Wisconsin Dells', ('Charles Town', 'WV'): 'Charles Town', ('Cody', 'WY'): 'Cody'
}
