import phonenumbers
import opencage
from test import number
import folium

from phonenumbers import geocoder
phonenumber = phonenumbers.parse(number)
location = geocoder.description_for_number(phonenumber,"en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode


key = 'cc2a022650d34f49b25ae19baa343047'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat,lng)

myMap = folium.Map(location=[lat, lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)

myMap.save("mylocation.html")