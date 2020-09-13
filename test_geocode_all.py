# Look up an address, get the coordinations, and show it on the map with Flask.
debug = True
from geopy.geocoders import Nominatim                                       # OpenStreetMap https://nominatim.org/
from flask import Flask,render_template
import folium

locator = Nominatim(user_agent="Willem Geo-coder")
location = locator.geocode("191 Queen Street, Auckland, New Zealand")

if debug == True : 
    print (location)
    print(f"Latitude = {location.latitude}, Longitude = {location.longitude}")
   
app = Flask(__name__)

@app.route('/')
def map_func():
	return render_template('map.html', lat = location.latitude, long = location.longitude)

if __name__ == '__main__':
    app.run(debug = True)    

