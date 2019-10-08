from shapely.geometry import Point, Polygon, MultiPolygon, LineString
import requests
import pandas as pd
import geojson
from geojson import Feature, Point, FeatureCollection
from datetime import datetime


data = pd.read_csv("data/201908-citibike-tripdata.csv")

starttimes = data['starttime']
data['starttime'] = [datetime.strptime(time, "%Y-%m-%d %H:%M:%S.%f") for time in starttimes]
mydate = datetime.strptime('2019-08-31', '%Y-%m-%d')
data = data[data.starttime.dt.date  == pd.to_datetime('2019-08-31').date()]

od = data.drop(['tripduration', 'starttime', 'stoptime',  'usertype', 'birth year', 'gender'], axis  =1 )
pairs = od.groupby(['start station id', 'start station latitude', 'start station longitude' ,
                'end station id', 'end station latitude', 'end station longitude']).size().reset_index(name='count')

features = []

number_of_elements = pairs.shape[0]

item = 0

for index, pair in pairs.iterrows():

    source_coordinates = str(pair['start station longitude']) + ',' + str(pair['start station latitude']) + ';'
    #print(type(source_coordinates))

    dest_coordinates = str(pair['end station longitude']) + ',' + str(pair['end station latitude'])

    item += 1

    url =  'http://router.project-osrm.org/route/v1/driving/'+source_coordinates+dest_coordinates

    payload = {"steps":"true","geometries":"geojson"}

    try:
        response = requests.get(url,params=payload)
        data = response.json()
        if data:
            if 'routes' in data:
                d = data['routes'][0]['geometry']
                if d:
                    d.update( {'count' : pair['count']} )
                    features.append(d)


    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)

    print(index)
    #if item == 100,000:
    #    break


new_features = []

for feature in features:
  line = LineString(feature['coordinates'])
  cnt = feature['count']

  feature = Feature(
    geometry=line,
    properties=cnt
  )

  new_features.append(feature)

  feature_collection = FeatureCollection(new_features)

with open('paths.geojson', 'w') as f:
  f.write(geojson.dumps(feature_collection))
