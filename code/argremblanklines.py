#!/usr/bin/python
############################################
### File:	argremblanklines.py
### Author:	Blanca A. Vargas-Govea
### Email:	blanca.vg@gmail.com
### Date:	08-Nov-2010
### Example:./argremblanklines.py -f foo.txt
############################################

# Removes blank lines, file name is read from command line arguments
# If attribute number is different to attribute header number, skip example

import re
import argparse

global ifilename

def parse():
    "Parsing command line arguments"
    global ifilename
    print "esto es una prueba"
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='simple_value',
                    help='Store a simple value')

    parser.add_argument('-c', action='append', dest='collection',
                    default=[],
                    help='Add repeated values to a list',
                    )
    results = parser.parse_args()
    print 'simple_value     =', results.simple_value
    print 'collection       =', results.collection
    ifilename = results.simple_value
    print "Input file: ",ifilename    
    return 

def rmvemptyln():
    "Remove blank lines in a file"    
    global ifilename
    print "el nombre leido es: ",ifilename
    ifile = open("/home/blanca/cenidpd/datanalysis/books/data/"+ifilename, "r")
    ofile = open("/home/blanca/cenidpd/datanalysis/books/data/newfoo.txt", "w")
    print "Name of the input file: ", ifile.name
    lcount = 0
    writetofile = True
    for line in ifile:
        row = line.rstrip()		# remove trailing chars
        row = row.split(',')	# row is a list: row[0],row[1]
        if lcount == 0:
            attnumber = len(row)# length from header
        if lcount > 0:
            rowlen = len(row)
            print "Elementos de la fila: ",rowlen 
            if rowlen <> attnumber:
                print "Wrong attribute number, skipping example"
                writetofile = False
        if writetofile:
            s = ",".join(row)+'\n'# to string
            ofile.write(s)
        lcount = 1
        writetofile = True
        newrow = []
    ifile.close()
    ofile.close()
    return

parse()
rmvemptyln()    



