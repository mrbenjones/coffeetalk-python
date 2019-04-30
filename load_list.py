from station.models import *
from station import db
import sys
import json

def user_list_from_names(names):
    for name in names:
        cc = Caller()
        cc.full_name = name['name']
        cc.email = name['email']
        cc.active = 1
        cc.apply_code()
        db.session.add(cc)
        print(cc)
        db.session.commit()


if (__name__=="__main__"):
    names = json.loads(open(sys.argv[1].strip()).read())
    user_list_from_names(names)
    print(names)
