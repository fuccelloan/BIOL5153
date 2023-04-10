#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="This script reads in a GFF file")

parser.add_argument("gff_name", help="", type=str)
parser.add_argument("fasta_name", help="", type=str)

args = parser.parse_args()

with open(args.gff_name) as gff:

	for line in gff:
		elements = line.strip("\n").split("\t")
		if elements[0] != '':
			type = elements[2]
			length = int(elements[4]) - (int(elements[3]) - 1)
			print(type, length) 
