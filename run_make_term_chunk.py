#!/usr/bin/env python3
import os
import sys

from inline_terms import *

def main(args):
    infile_outfile_list = args[1]
    infile_list = f'{args[1]}.inputs'
    outfile_list = f'{args[1]}.outputs'
    with open(infile_outfile_list, "r") as files,\
        open(infile_list, "w") as infile_list_file,\
        open(outfile_list, "w") as outfile_list_file:
        for filelist in files:
            *inputs, output = filelist.split(';')
            infile_list_file.write(';'.join(inputs) + '\n')
            outfile_list_file.write(output + '\n')
    abbr_to_full = args[2]
    special_domain = args[3]
    if special_domain.lower() == 'false':
        special_domain = False
    lemma_dict = args[4]
    make_term_chunk_file_list(infile_list,outfile_list,abbr_to_full,special_domain,lemma_dict)

if __name__ == '__main__': sys.exit(main(sys.argv))

