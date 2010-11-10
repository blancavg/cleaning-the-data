#!/usr/bin/python
############################################
### File:	clean.py
### Author:	Blanca A. Vargas-Govea
### Email:	blanca.vg@gmail.com
### Date:	05-Nov-2010
############################################
# Removes non-alphanumeric characters from all attributes

import re

ifile = open("/home/blanca/cenidpd/datanalysis/books/data/foo.txt", "r")
ofile = open("/home/blanca/cenidpd/datanalysis/books/data/newfoo.txt", "w")
print "Name of the input file: ", ifile.name
lcount = 0
attcount = 0
newrow = []

for line in ifile:
    row = line.rstrip() # remove trailing chars
    row = row.split(',');  # row is a list: row[0],row[1]
    if lcount == 0:
        attnumber = len(row)
    if lcount > 0:
        while(attcount < attnumber): 
            m = re.sub('\W','',row[attcount]) #clean data
            newrow.append(m)
            print "dirty: ",row[attcount],"\tclean: ",m           
            attcount = attcount + 1
    lcount = 1
    attcount = 0
    s = ",".join(newrow)+'\n'  # to string
    ofile.write(s)
    newrow = []
    
ifile.close()
ofile.close()

