#!/usr/bin/env python
# encoding: utf-8
"""
Python Course Project.

Copyright 2016 Maryam, Mukesh and Pramod. All rights reserved.
"""

import subprocess
import argparse


def create_database(subject_data_file):
    command = ['formatdb',
               '-i',
               'subject_data_file',
               '-p',
               'F',
               '-o',
               'T']
    my_proc_1 = subprocess.Popen(command,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 universal_newlines=True)
    return my_proc_1.stdout


def blastn_model_organism(query_fasta_file, database_files):
    command = ['blastn',
               '-task',
               'blastn',
               '-num_threads',
               '16',
               '-evalue',
               '1e-5',
               '-max_target_seqs',
               '1',
               '-outfmt',
               '6 std qlen slen staxids stitle',
               '-query',
               'query_fasta_file',
               '-db',
               'database_files',
               '-out',
               'model_organism_blast_output']

    my_proc_for_blast = subprocess.run(command,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       universal_newlines=True)
    return my_proc_for_blast.stdout


def get_unique_hit_model_organism(model_organism_blast_output, output_uniquehit_file):
    command = ['cut',
               '-f1,2,11,12,16',
               'model_organism_blast_output']

    my_proc_for_cut = subprocess.run(command,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     universal_newlines=True)

    command = ['sort', '-u', '-k1,1']
    with open('output_uniquehit_file', 'w') as stdout_file:
        # with open('output_uniquehit_file', + '_err', 'w') as stderr_file:
            my_proc_for_uniq = subprocess.run(command,
                                              input=my_proc_for_cut.stdout,
                                              stdout=stdout_file,
                                              stderr=stderr_file,
                                              universal_newlines=True)
            return my_proc_for_uniq


def get_non_hit_model_organism(query_fasta_file, model_organism_blast_output, non_hit_after_model_blast):
    f1 = open('query_fasta_file', 'r')
    f2 = open('model_organism_blast_output', 'r')
    f3 = open('non_hit_after_model_blast', 'w')

    list_ids = []
    for line in f2:
        accessorID = line[0:-1]
        list_ids.append(accessorID.partition('\t')[0])
    flag = 0
    for line in f1:
        if line[0] == '>':
            accessorID = line[1:-1]
            if accessorID in list_ids:
                flag = 0
                print('Skipped ' + accessorID)
            else:
                flag = 1
        else:
            if flag == 1:
                if(line[0] == '>'):
                    flag = 0
        if flag == 1:
            f3.write(line)

    f1.close()
    f2.close()
    f3.close()


def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("input_file_to_creat_database", help="Give the " +
                       "file path of the file you need to make database")
    parse.add_argument("query_file", help="Give the fasta query file" +
                       " you want to blast with database")
    parse.add_argument("uniquehit_model_organism", help="Give the name of " +
                       "uniquehit output file")
    parse.add_argument("no_hit_model_organism", help="Give the name of " +
                       "uniquehit output file")
    file = parse.parse_args()

    infilename = file.input_file_to_creat_database
    output_uniquehit_file = file.uniquehit_model_organism
    no_hit_file = file.no_hit_model_organism
    query_fasta_file = file.query_file
    database_files = create_database(infilename)
    model_organism_blast_output = blastn_model_organism(query_fasta_file, database_files)
    get_unique_hit_model_organism(model_organism_blast_output, output_uniquehit_file)
    get_non_hit_model_organism(query_fasta_file, model_organism_blast_output, no_hit_file)


if __name__ == '__main__':
    main()
