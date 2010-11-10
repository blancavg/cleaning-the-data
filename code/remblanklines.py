#!/usr/bin/python

# Removes blank lines

import re

ifile = open("/home/blanca/cenidpd/datanalysis/books/data/foo.txt", "r")
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

