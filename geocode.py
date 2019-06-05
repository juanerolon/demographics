#Juan E Rolon
#@juanerolon
#https://github.com/juanerolon/demographics



import sys
import pandas as pd
import requests
import IPython

#Using Google Cloud infrastructure
#Set to true to actually get geocoding using my API key from google cloud

keypath = '/Users/juanerolon/cr_storage/'


f = open(keypath + r'geo_tmp_key', 'r')
demo_key = f.readline()
f.close()


#Below we test using the geocoding api from Google maps services
if True:
    url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'sensor': 'false', 'address': '1020+Towhee Dr,+Shreveport,+LA', 'key':demo_key}
    r = requests.get(url, params=params)
    print(r.text)


#processing results from api call above
if False:
    df = pd.read_json('geocode_test.json')
    print(df.results[0]['geometry']['location'])
    print(df.results[0]['geometry']['location']['lat'])
    print (df.results[0]['geometry']['location']['lng'])


#dissentangle json to select fields appropiate for geotagging descriptors
if True:
    df = pd.read_json('geocode_test.json')


    print("\n *json dataframe columns: \n")
    print(df.columns)

    print ("\n *status: \n")
    print(df.status[0])

    print("\n results \n")
    pdd = df.results[0]

    for ky in pdd.keys():
        print("key = {}, value = {}".format(ky,pdd[ky]))

    print("\n *address components: \n")
    for el in pdd["address_components"]:
        print(el)

    print("\n *geometry: \n")
    geo = pdd["geometry"]
    for kel in geo.keys():
        print("key = {}, value = {}".format(kel, geo[kel]))









