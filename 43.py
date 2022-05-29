#Name: Anik Singha
#Email: anik.singha68@myhunter.cuny.edu
#Date: September 12, 2021
#Folium with pandas

import pandas as pd
import folium

file = input("Enter CSV file name: ")
output = input("Enter outfile file: ")

map = folium.Map(location=[40.768731, -73.964915],zoom_start=10)

df = pd.read_csv(file)

for index in df.iterrows():
    lat = df['LATITUDE'][index]
    lon = df['LONGITUDE'][index]
    name = df["NAME"][index]
    newMarker = folium.Marker([lon, lat], popup=name)
    newMarker.add_to(map)

map.save(output)
