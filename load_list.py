from station.models import *
from station import db
import sys

def user_list_from_file(filename):
    codes = {}
    with open(filename) as fin:
        for line in fin.readlines():
            fields = line.split(",")
            cc = Caller()
            if len(fields)>2:
                cc.full_name = "{} {}".format(fields[1],fields[0])
                cc.email = fields[-1].strip()
                cc.active = 1
                cc.apply_code()
                if cc.code in codes:
                    print("ERROR {} has existing code".format(cc.full_name))
                codes[cc.code] = 1
                db.session.add(cc)
            print(cc)
        db.session.commit()

if (__name__=="__main__"):
    print(sys.argv[1].strip())
    user_list_from_file(sys.argv[1].strip())
