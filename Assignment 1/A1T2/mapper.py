#!/usr/bin/env python3
import sys
import json
import requests

latitudes = float(sys.argv[1])
longitudes = float(sys.argv[2])
queried_distances = float(sys.argv[3])

url = "http://20.185.44.219:5000/"

for line in sys.stdin:
    record = json.loads(line.lower().strip().replace("nan","NaN"))
    value1 = record["start_lat"]
    value2 = record["start_lng"]
    distance = pow(pow((value1-latitudes),2) + pow((value2-longitudes),2) ,0.5)
    d = {"latitude":value1,"longitude":value2}
    if(distance < queried_distances and value0!=None and value1!=None):
        r = requests.post(url=url,json=d)
        payload = r.json()
        print(f"{payload['state']},{payload['city']},1")

