# from math import radians, cos, sin, asin, sqrt
# def dist(lat1, long1, lat2, long2):
#     """
# Replicating the same formula as mentioned in Wiki
#     """
#     # convert decimal degrees to radians 
#     lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
#     # haversine formula 
#     dlon = long2 - long1 
#     dlat = lat2 - lat1 
#     a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
#     c = 2 * asin(sqrt(a)) 
#     # Radius of earth in kilometers is 6371
#     km = 6371* c
#     return km

# import datetime
# print(datetime.datetime.now())
# print("DEWAS: ", dist(22.753284, 75.893700, 22.962267, 76.050797)) #dewas
# print(datetime.datetime.now())
# print("UJJAIN: ", dist(22.753284, 75.893700, 23.179300, 75.784912)) #ujjain
# print(datetime.datetime.now())


# # Import the required library
# from geopy.geocodepip install geopyrs import Nominatim

# # Initialize Nominatim API
# geolocator = Nominatim(user_agent="MyApp")

# location = geolocator.geocode("Hyderabad")

# print("The latitude of the location is: ", location.latitude)
# print("The longitude of the location is: ", location.longitude)



# import requests
# import urllib.parse

# address = 'bhawar, Indore, 452001'
# url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

# response = requests.get(url).json()
# print(response[0]["lat"])
# print(response[0]["lon"])