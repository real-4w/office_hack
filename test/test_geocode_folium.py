#Test Geo-code inspired by https://towardsdatascience.com/geocode-with-python-161ec1e62b89
# WIP : https://www.w3resource.com/python-exercises/geopy/index.php
#import geopy
debug = True
from geopy.geocoders import Nominatim                                       # OpenStreetMap https://nominatim.org/
import folium
#from geopy.extra.rate_limiter import RateLimiter

locator = Nominatim(user_agent="Willem Geo-coder")
location = locator.geocode("191 Queen Street, Auckland, New Zealand")
#geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

if debug == True : 
    print (location)
    print(f"Latitude = {location.latitude}, Longitude = {location.longitude}")
    
m = folium.Map(location=[location.latitude, location.longitude])
# See Jypiter notebook for displaying folium objects, no render funtions available.
# trying to create a html wrapper as per https://stackoverflow.com/questions/36969991/folium-map-not-displaying
# https://ocefpaf.github.io/python4oceanographers/blog/2014/05/05/folium/

