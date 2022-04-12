from math import radians, cos, sin, asin, sqrt
import requests
import urllib.parse


def get_location(address):
    '''
    get location by geopy library
    '''
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
    response = requests.get(url).json()

    if response:
        add = address.split(',')
        if len(add):
            response = get_location(add)
        print(response[0]["lat"], response[0]["lon"])
    return response


def find_distance(lat1, long1, lat2, long2):
    '''
    Haversine formula
    '''
    # convert decimal degrees to radians 
    lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])
    # haversine formula 
    dlon = long2 - long1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    # Radius of earth in kilometers is 6371
    km = 6371* c
    return km
