from station.models import *
from station import db
from station.calls import *

import sys
import json

caller_URI = "https://coffeetalk.sneakercamp.net/#/call/draw/{}"

def define_name(example):

    uri = "<a href=\"{}\">{}</a>".format(caller_URI.format(example['code']),
                                   caller_URI.format(example['code']))
    result = "Link for {} ({}) : {} ".format(example['name'],
                                             example['email'],uri)
    return result

if (__name__ == "__main__"):
    csvFile = open("call_links.csv","w")
    csvFile.write("Name,email,code,link\n")
    print("<html><head><title>Coffeetalk Links</title><body>")
    for item in callers_and_codes():
        csvFile.write("\"{}\",\"{}\",\"{}\",\"{}\"\n".format(
            item['name'],item['email'],
            item['code'],
            caller_URI.format(item['code'])
        ))
        print(define_name(item))
        print("\n\n\n\n")
        print("<br/><br/><br/>")
    print("</body></html>")

