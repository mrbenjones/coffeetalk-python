from station.models import *
from station import db
from station.calls import *

import sys
import json

caller_URI = "https://coffeetalk.sneakercamp.net/#/call/draw/{}"

def define_name(example):

    uri = "<a href=\"{}\">{}</a>".format(caller_URI.format(example['code']),
                                   caller_URI.format(example['code']))
    result = "Link for {} : {} ".format(example['name'],uri)
    return result

if (__name__ == "__main__"): 
    for item in callers_and_codes(): 
        print(define_name(item))
        print("\n\n\n\n")
