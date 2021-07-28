#!/usr/bin/env python

import sys

for line in sys.stdin:
    date,id_num,temperature = line.strip().split(",")
    year = date.split("-")[-1]
    print "%s\t%s" % (year,temperature)