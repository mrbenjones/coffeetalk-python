#!/usr/bin/python

import csv
import json

from station import db
from station.models import *

def user_list(csv_file):
    with open(csv_file,'rb') as infile:
        reader = csv.DictReader(infile)
        for record in reader:
            yield record

if (__name__=="__main__"):
    print([u for u in user_list('users.csv')])
        
