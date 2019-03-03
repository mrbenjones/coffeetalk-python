#!/usr/bin/python

import PyPDF2
import re

lastnameRE=re.compile("^[A-Z]{3,}")
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

def extract_records(text):
    def valid(record):
        return (bool(lastnameRE.search(record.get('last_name',""))))
    fields = 7 
    keys = ["last_name",
            "first_name",
            "number",
            "office",
            "title",
            "location"]
    record = {}
    for line in text.split("\n"):
        
        if fields < 6:
            record[keys[fields]] = line.strip()
            fields += 1
        if fields==6:
            if (valid(record)):
                yield record
            fields = 0
            record = {}
        if line.strip().startswith("LOCATION"):
            fields = 0
            record = {}


            
            
            
            
            
if (__name__=="__main__"):
    names = [k for k in extract_records(extract_names('names.pdf'))]
    print(len(names))
