#!/usr/bin/python

import PyPDF2
import re
import json
import csv

lastnameRE=re.compile("^[A-Z]{3,}")
phoneRE=re.compile("\d{3,}.?\d{4,}")
firstnameRE=re.compile("[A-Z][a-z]")
def extract_names(filename):
    text = ""
    with open(filename,'rb') as  infile:
        reader = PyPDF2.PdfFileReader(infile)
        i=0
        while (i<reader.numPages):
            page = reader.getPage(i)
            text += page.extractText()
            i+=1
    return text

def spit_records(text):
    def is_last_name(field):
        if (field==(field.upper())):
            return True
        else:
            return False
    def is_number(field):
        return bool(phoneRE.search(field))
    def is_first_name(field):
        return bool(firstnameRE.search(field))

    last = ""
    second_last = ""
    sequence = text.split("\n")
    for (a,b,c) in zip(sequence[:-2],sequence[1:-1],sequence[2:]):
        if is_last_name(a) and is_number(c) and is_first_name(b):
            test_email = "{}.{}@state.nm.us".format(b,a).replace(" ","_").replace("(","").replace(")","")
            yield {'name' : "{} {}".format(b,a),
                   'email':test_email}


def records_from_csv(filename):
    with open(filename,newline='') as csvfile:
        resultReader = csv.reader(csvfile,delimiter=",",quotechar="\"")
        for row in resultReader:
            name=row[0]
            nameFields = [n.strip() for n in name.split(",")]
            yield {'name' : "{} {}".format(nameFields[1],nameFields[0]),
                   'email' : row[1].strip()}
            
        
            
if (__name__=="__main__"):
#    names = [n for n in spit_records(extract_names('names.pdf'))]
    names = list(records_from_csv("bureaunames.csv"))
    print(names)
    print(len(names))
    with open("names.json","w+") as outfile:
        json.dump(names,outfile)
