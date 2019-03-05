#!/usr/bin/python

import csv
import json

from station import db
from station.models import *

def user_list(csv_file):
    with open(csv_file,'r') as infile:
        reader = csv.DictReader(infile)
        for record in reader:
            yield record

def create_user(dict):
    uu = User()
    uu.username = dict['username']
    uu.email = dict['email']
    uu.set_password("1885BeH")
    return uu

def create_caller(dict):
    cc = Caller()
    cc.full_name = dict['name']
    cc.email = dict['email']
    cc.active = True
    cc.apply_code()
    return cc

if (__name__=="__main__"):
    users = [u for u in user_list("preload/users.csv")]
    callers = json.load(open("preload/names.json","r"))
    for uu in [create_user(u) for u in users]:
        print(uu)
        db.session.add(uu)
    for cc in [create_caller(c) for c in callers]:
        print(cc)
        db.session.add(cc)
    db.session.commit()
    
        
