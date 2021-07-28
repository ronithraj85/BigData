#!/usr/bin/env python

from operator import itemgetter
import sys

final_year = None
max_temp = 0

for line in sys.stdin:
    line = line.strip()
    year, temperature = line.split(',')
    if final_year == year:
        max_temp = max(int(max_temp), int(temperature))
    else:
        if final_year:
            print(final_year, max_temp)
        final_year = year
        max_temp = temperature
        
if final_year:
    print(final_year, max_temp)

