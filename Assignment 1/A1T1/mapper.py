#!/usr/bin/env python3
import sys
from datetime import datetime
import json
import operator

result=[]
final_results = []

for line in sys.stdin:
    record=json.loads(line)
    if(record['Severity']>=2 and record['Sunrise_Sunset']=='Night'and record['Visibility(mi)']<=10 and record['Precipitation(in)']>=0.2 and (record['Weather_Condition'] in ['Thunderstorm','Heavy Rain Showers','Blowing Dust','Heavy Snow','Heavy Rain']) and ("lane blocked" in str(record['Description']).lower() or "shoulder blocked" in str(record['Description']).lower() or "overturned vehicle" in str(record['Description']).lower()) ):
       result.append(record['Start_Time'])
       
       
for i in result:
    i=i.split('.')[0]
    date_object=datetime.strptime(i,"%Y-%m-%d %H:%M:%S")
    final_results.append(date_object.hour)

final_results.sort()

for j in final_results:
    print(j,"1")
