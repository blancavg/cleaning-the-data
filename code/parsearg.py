#!/usr/bin/python
############################################
### File:	parsearg.py
### Author:	Blanca A. Vargas-Govea
### Email:	blanca.vg@gmail.com
### Date:	09-Nov-2010
### ./parsearg.py -f foo.txt -c 1,2,3,4
############################################
# Use of argparse

import re
import argparse


def parse():
    "Parsing command line arguments"
    print "esto es una prueba"
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', action='store', dest='ifilename',
                    help='Store a simple value')
    parser.add_argument('-c', action='append', dest='columns',
                    default=[],
                    help='Add repeated values to a list',
                    )
    results = parser.parse_args()
    arglist = list(results.columns)
    arglist.append(results.ifilename)
    return arglist

def readfc():
    "Read the args from list"
    arglist = parse()
    dirtyf = arglist.pop()
    print "dirtyfile = ", dirtyf
    print "columns = ",arglist
    return
    
readfc()

