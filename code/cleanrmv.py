#!/usr/bin/python
############################################
### File:	cleanrmv.py
### Author:	Blanca A. Vargas-Govea
### Email:	blanca.vg@gmail.com
### Date:	08-Nov-2010
############################################
# Removes non-alphanumeric characters from all attributes
# Remove empty lines

import re

ifile = open("/home/blanca/cenidpd/datanalysis/books/data/foo.txt", "r")
ofile = open("/home/blanca/cenidpd/datanalysis/books/data/newfoo.txt", "w")
print "Name of the input file: ", ifile.name
lcount = 0
attcount = 0
newrow = []
writetofile = True

for line in ifile:
    row = line.rstrip() # remove trailing chars
    row = row.split(',');  # row is a list: row[0],row[1]    
    if lcount == 0:
        attnumber = len(row)
    rowlen = len(row)
    print "Elementos de la fila: ",rowlen 
    if rowlen <> attnumber:
        print "Wrong attribute number, skipping example"
        writetofile = False
    if writetofile:
        while(attcount < attnumber): # attribute iteration
            m = re.sub('\W','',row[attcount]) #clean data
            newrow.append(m)
            print "dirty: ",row[attcount],"\tclean: ",m  
            attcount = attcount + 1
        print "imprimiendo"
        s = ",".join(newrow)+'\n'  # to string
        ofile.write(s)   
    writetofile = True                     
    lcount = 1
    attcount = 0
    newrow = []
    
ifile.close()
ofile.close()

