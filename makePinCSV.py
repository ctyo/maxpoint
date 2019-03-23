import sys
import random

num = int(sys.argv[1])
ne = {
    "lat" : 43,
    "lon" : 130
}
sw = {
    "lat" : 32,
    "lon" : 150
}
print("latitude,longitude,name")
for i in range(num):
    lat = random.uniform(ne["lat"], sw["lat"])
    lon = random.uniform(ne["lon"], sw["lon"])
    print(str(lat) + "," + str(lon)+',test')