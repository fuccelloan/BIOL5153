#! /usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description="This script reads in a GFF file")

parser.add_argument("gff_name", help="", type=str)
parser.add_argument("fasta_name", help="", type=str)

args = parser.parse_args()

gff = open(args.gff_name, 'r')
fasta = open(args.fasta_name, 'r')

gff_lines = gff.readlines()


gff.close()
fasta.close()
