
import sys

curr_state_count = 0
curr_state = None
curr_city_count = 0
curr_city = None

for line in sys.stdin:
    entries = line.strip().split(",")
    if curr_state != entries[0]:
        if curr_state!=None:
            print(curr_city,curr_city_count)
            print(curr_state,curr_state_count+curr_city_count)
            curr_state_count = 0
            curr_city = None
        curr_state = entries[0]
        print(curr_state)
    if curr_city == None:
        curr_city = entries[1]
        curr_city_count = 0
    if curr_city == entries[1]:
        curr_city_count += curr_city_count +1
    else:
        print(curr_city,curr_city_count)
        curr_state_count += curr_city_count
        curr_city = entries[1] 
        curr_city_count = int(entries[2])
    
print(curr_city,curr_city_count)
print(curr_state,curr_state_count+curr_city_count)
