#!/usr/bin/env python3
"""
Author: Kamil Dabek
Program will extract the S3 request IDs from a log file of an S3 request
Input: filepath to an S3 log file
Output: S3 request IDs from log file into a separate text file

Additional note: to extract S3 request ID via CLI. Run command with --debug flag e.g. aws s3 ls --debug 2> s3_log.txt
"""

import os
import argparse
import re

parser = argparse.ArgumentParser(description='Will extract the S3 Request ID pairs from an S3 request debug file and export the IDs to a new file.')
parser.add_argument('-i', '--inputfile', type=str, metavar='', required=True, help='file where the S3 debug logs are located')
parser.add_argument('-o', '--outputfile', type=str, metavar='', default="request_ids1.txt", help='file where you want the extracted S3 IDs to be written')
args = parser.parse_args()

INPUTFILE = args.inputfile
OUTPUTFILE = args.outputfile
# request ID tags have ': ' at the end to skip the useless characters before the RID
REQUEST_ID_SHORT = "x-amz-request-id': '"
REQUEST_ID_LONG = "x-amz-id-2': '"

def parse_s3_log():
    print(f'Getting request IDs from: {os.path.abspath(INPUTFILE)} and outputting to {os.path.abspath(OUTPUTFILE)}')
    with open(INPUTFILE, 'r') as s3_logs:

    # iterate through lines in input file and write request IDs to external file
        with open(OUTPUTFILE, 'a') as f:
            f.write(f"S3 Request IDs from file in {os.path.abspath(INPUTFILE)}\n----------------------\n")
            for line in s3_logs:
                if bool(re.search(f'{REQUEST_ID_SHORT}', f'{line}')):   # use regex to check if RID contained in line
                    short_id = re.split(f'\\b{REQUEST_ID_SHORT}\\b', line)[1][0:16]     # takes first 16 chars after RID tag
                    f.write(f"short request ID: {short_id}\n")

                if bool(re.search(f'{REQUEST_ID_LONG}', f'{line}\n')):   # use regex to check if RID contained in line
                    long_id = re.split(f'\\b{REQUEST_ID_LONG}\\b', line)[1][0:76]     # takes first 76 chars after RID tag
                    f.write(f"long request ID:  {long_id}\n")
                    f.write("----------------------\n\n")
            f.close()
        s3_logs.close()

parse_s3_log()      # calls log parser function
