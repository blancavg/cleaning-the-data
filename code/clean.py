#!/usr/bin/python
############################################
### File:	clean.py
### Author:	Blanca A. Vargas-Govea
### Email:	blanca.vg@gmail.com
### Date:	05-Nov-2010
############################################
# Removes non-alphanumeric characters from all attributes

import re

ifile = open("/home/blanca/cenidpd/cleaning-the-data/data/foo.txt", "r")
ofile = open("/home/blanca/cenidpd/cleaning-the-data/data/newfoo.txt", "w")
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
            cadena = ' '.join(row[attcount].split()) # replace multiple spaces with one
            print "cadena = ",cadena
            tmp = re.sub(r'[^a-zA-Z0-9: ]', '', cadena) # remove all non-alphan chars but semicolon and single space
            print "tmp = ",tmp
            #m = re.sub('\W','',row[attcount]) #clean data
            newrow.append(tmp)
            print "dirty: ",row[attcount],"\tclean: ",tmp           
            attcount = attcount + 1
    lcount = 1
    attcount = 0
    s = ",".join(newrow)+'\n'  # to string
    ofile.write(s)
    newrow = []
    
ifile.close()
ofile.close()

