#!/usr/bin/env python3

import sys
		
for line in sys.stdin:
	line=line.strip().split(',')
	print(int(line[0]),round(float(line[1]),2),sep=',')
	
    

