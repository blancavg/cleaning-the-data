#!/usr/bin/python
############################################
### File:	argcleanrmv.py
### Author:	Blanca A. Vargas-Govea
### Email:	blanca.vg@gmail.com
### Date:	08-Nov-2010
### ./argcleanrmv.py foo.txt
### ./argcleanrmv.py foo.txt -c 0,1
############################################
# Remove non-alphanumeric characters from all attributes
# Remove empty lines

import sys
import re
import argparse

def parse():
    "Parsing command line arguments"
    arglist = []
    parser = argparse.ArgumentParser()
    parser.add_argument('ifilename', action='store', help='File name')
    parser.add_argument('-c', action='append', dest='columns',
                    default=[],
                    help='Add repeated values to a list',
                    )
    results = parser.parse_args()      
    if not results.columns:
        print "The whole file will be cleaned (default)"        
    else:
        columns = results.columns # list of strings to list of integers
        strcol = columns.pop()
        strcol = strcol.split(',')
        cols = map(eval,strcol)
        arglist.append(cols)
        print "Cleaning only the listed columns",cols
    arglist.append(results.ifilename)
    print "Arglist = ",arglist
    return arglist

def cleanav(attval,cleanrow):
    "Clean a string"
    m = re.sub('\W','',attval) #clean data
    cleanrow.append(m)
    #print "dirty: ",attval,"\tclean: ",m  
    #print "cleanrow = ",cleanrow
    return cleanrow

def clean():
    "Clean a dirty file"
    arglist = parse()
    dirtyf = arglist.pop()
    colist = []
    if len(arglist) > 0:
        colist = arglist.pop() 
    #print "colist = ",colist
    try:
        ifile = open("../data/"+dirtyf, "r")
    except IOError:
        sys.exit("Error: can\'t find file or read data")
    else:
        print "OK"
    ofile = open("../data/clean_"+dirtyf, "w")
    lcount = 0
    attcount = 0
    newrow = []
    writetofile = True
    for line in ifile:
        row = line.rstrip() # remove trailing chars
        row = row.split(','); # row is a list: row[0],row[1]    
        if lcount == 0:
            attnumber = len(row) # attribute number in header
        rowlen = len(row)
        print "Attribute number: ",rowlen # attribute number in row
        if rowlen <> attnumber:
            print "Wrong attribute number, skipping example"
            writetofile = False
        if writetofile:
            if not colist:
                for attval in row:
                    newrow = cleanav(attval,newrow)
            else:
                for attval in colist:
                   newrow = cleanav(row[attval],newrow)
            s = ",".join(newrow)+'\n' # to string
            ofile.write(s) 
        writetofile = True                     
        lcount = 1
        attcount = 0
        newrow = []
    ifile.close()
    ofile.close()
    return
    
clean()

