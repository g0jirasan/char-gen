#!/usr/bin/python -w

import sys

if len(sys.argv) < 3:
	print "[-] Usage: <output file name> <length of buffer> <character>"
	print "[-] Example: gojira.txt 3000 A"
	sys.exit(0)
  
filename = sys.argv[1]
length = sys.argv[2]
char = sys.argv[3]

length = int(length)

buffer = char*length


textfile = open(filename , 'w')
textfile.write(buffer)
textfile.close()
