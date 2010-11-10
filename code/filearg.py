#!/usr/bin/python

# Using arguments
# http://www.doughellmann.com/PyMOTW/argparse/

import argparse

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

# $ python argparse_action.py -s value
# $ python argparse_action.py -c
# $ python argparse_action.py -t
# $ python argparse_action.py -f
# $ python argparse_action.py -a one -a two -a three
# $ python argparse_action.py -B -A
# $ python argparse_action.py --version




