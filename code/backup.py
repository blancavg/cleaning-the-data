#!/usr/bin/python
############################################
### File:	cleandirtyf.py
### Author:	Blanca A. Vargas-Govea
### Email:	blanca.vg@gmail.com
### Input:      raw data file
### Output:     A cleaned data file, a report,
###             and a CSV file
### ./cleandirtyf.py foo.txt
### ./cleandirtyf.py foo.txt -s ";"
### ./cleandirtyf.py foo.txt -c 0,1
### ./cleandirtyf.py BX-Users.csv -s semic
############################################
# Remove non-alphanumeric characters from all attributes
# Remove empty lines

import sys
import re
import argparse
import logging
import logging.config
import time

logging.config.fileConfig("loggingf.config")
# create logger
logger = logging.getLogger("clean")

def parse():
    "Parsing command line arguments"
    arglist = []
    parser = argparse.ArgumentParser()
    parser.add_argument('ifilename', action='store', help='File name')
    parser.add_argument('-c', action='append', dest='columns',
                    default=[],
                    help='Add repeated values to a list',
                    )
    parser.add_argument('-s', action='store', dest='separator',
                    help='Store a separator')
    results = parser.parse_args() 
    if not results.columns:
        print "The whole file will be cleaned (default)"
        logger.info("The whole file will be cleaned (default)")       
    else:
        columns = results.columns # list of strings to list of integers
        strcol = columns.pop()
        strcol = strcol.split(',')
        cols = map(eval,strcol)
        arglist.append(cols)
        logger.info("Cleaning only the listed columns: "+str(cols))    
    print "Separator: ",results.separator    
    if not results.separator or results.separator == "comma":
        print "Using the default separator (,)"
        arglist.append(",")
    elif results.separator == "semic":
        arglist.append(";")
    else:
        sys.exit("Not a valid separator. Possible values: comma | semic")
    arglist.append(results.ifilename)
    print "Arglist",arglist
    return arglist

def cleanav(attval,cleanrow):
    "Clean a string"
    singlesp = ' '.join(attval.split()) # replace multiple single
    # remove all non-alphan chars but semicolon and single spaces
    m = re.sub(r'[^a-zA-Z0-9: ]', '', singlesp) 
    cleanrow.append(m)
    logger.debug("dirty: "+attval+"\tclean: "+m)
    logger.debug("cleanrow = " + str(cleanrow))
    return cleanrow

def out(INFILE,allrows,empty,longer,longerow,shorter,shorterow,dirty):
    REPORT = "../reports/rep_"+INFILE
    CSVREPORT = "../data/rep_"+INFILE
    # create report file (friendly readable)
    try:
        hreport = open(REPORT, "w")
    except IOError:
        logger.error("Error: can\'t create the report file")
        sys.exit("Error: can\'t create the report file")
    else:
        print "OK: Report file created"
        logger.info("OK: Report file created")   

    # create csv file
    try:
        csvreport = open(CSVREPORT, "w")
    except IOError:
        logger.error("Error: can\'t create the csv file")
        sys.exit("Error: can\'t create the csv file")
    else:
        print "OK: csv file created"
        logger.info("OK: csv file created")

    allrows = allrows - 1 # without the header
    usefulrows = allrows - empty - longer - shorter
    removed = empty + longer + shorter
    pcgusefulrows = (usefulrows*100)/allrows
    print "===== Input file (before cleaning) = ",INFILE
    print "Examples = ",allrows 
    print "Empty rows (removed) = ",empty
    print "Longer rows (removed) = ",longer
    print "Shorter rows (removed) = ",shorter
    print "Removed rows = ",removed
    print "Dirty values (cleaned) = ", dirty
    print "===== Output file (after cleaning)"
    print "Useful rows = ",usefulrows + 1  # last eol
    print "Useful file = ",pcgusefulrows,"%"
    ########## write to report file
    hreport.write("===== Input file (before cleaning) = "+INFILE+"\n")
    hreport.write("Examples = "+str(allrows)+"\n")
    hreport.write("Empty rows (removed) = "+str(empty)+"\n")
    hreport.write("Longer rows (removed) = "+str(longer)+"\n")
    hreport.write("Shorter rows (removed) = "+str(shorter)+"\n")
    hreport.write("Removed rows = "+str(removed)+"\n")
    hreport.write("Dirty values (cleaned) = "+str(dirty)+"\n")
    hreport.write("===== Output file (after cleaning)"+"\n")
    hreport.write("Useful rows = "+str(usefulrows+1)+"\n")
    hreport.write("Useful file = "+str(pcgusefulrows)+"%"+"\n")
    ########## write to csv 
    csvreport.write("raw,emptyl,long,short,removed,dirtych,usfl,pcgusfl\n")
    csvreport.write(str(allrows)+","+str(empty)+","+str(longer)+","+str(shorter)+","+str(removed)+","+str(dirty)+","+str(usefulrows+1)+","+str(pcgusefulrows)+"\n")
    ########## write to logger
    logger.debug("Longer rows (removed) = "+str(longer)+" Rows = "+str(longerow)+"\n")
    logger.debug("Shorter rows (removed) = "+str(shorter)+" Rows = "+str(shorterow)+"\n")
    hreport.close()
    csvreport.close()
    return

def clean(arglist):
    "Clean dirty file"
    dirtyf = arglist.pop()
    separator = arglist.pop()
    colist = []
    print "colist = ",colist
    if len(arglist) > 0:
        colist = arglist.pop() 
        print "colist = ",colist
    INFILE = "../data/"+dirtyf
    OUTFILE = "../data/clean_"+dirtyf
    try:
        ifile = open(INFILE, "r")
    except IOError:
        logger.error("Error: can\'t find file or read data")
        sys.exit("Error: can\'t find file or read data")
    else:
        logger.info("OK: opening file")
    try:
        ofile = open(OUTFILE, "w")
    except IOError:
        logger.error("Error: can\'t create the cleaned file")
        sys.exit("Error: can\'t create the cleaned file")
    else:
        print "OK: Cleaned file created"
        logger.info("OK: Cleaned file created") 
    lcount = 0
    attcount = 0
    newrow = []
    writetofile = True
    empty = 0  # empty rows counter
    longer = 0  # longer rows counter
    shorter = 0  # shorter rows counter
    dirty = 0  # dirty attribute values counter
    longerow = []
    shorterow = [] 
    for line in ifile:
        print "..."
        row = line.rstrip() # remove trailing chars
        row = row.split(separator); # row is a list: row[0],row[1]    
        if lcount == 0:
            attnumber = len(row) # attribute number in header
        rowlen = len(row)
        logger.debug("Attribute number: "+str(rowlen))
        if rowlen <> attnumber:
            logger.debug("Wrong attribute number, skipping example")
            writetofile = False
            if rowlen == 1:
                empty = empty + 1
            elif rowlen > attnumber:
                longer = longer + 1
                longerow.append(lcount)
            else:
                shorter = shorter + 1
                shorterow.append(lcount)
        if writetofile:
            if not colist:
                for attval in row:
                    newrow = cleanav(attval,newrow)
                    dirty = dirty + 1
            else:
                for attval in colist:
                    newrow = cleanav(row[attval],newrow)
                    dirty = dirty + 1
            s = ",".join(newrow)+'\n' # to string
            ofile.write(s) 
        writetofile = True                     
        lcount = lcount + 1
        attcount = 0
        newrow = []
    ifile.close()
    ofile.close()
    out(dirtyf,lcount,empty,longer,longerow,shorter,shorterow,dirty)
    return
    
def main():
    start = time.clock()
    arglist = parse()
    clean(arglist)
    elapsed = (time.clock() - start)
    print "Elapsed time: ",elapsed
    logger.info("Elapsed time: "+str(elapsed))
    pass

if __name__ == "__main__":
    main()

