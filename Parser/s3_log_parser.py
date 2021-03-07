"""
Author: Kamil Dabek
Program will extract the S3 request IDs from a log file of an S3 request
Input: filepath to an S3 log file
Output: S3 request IDs from log file
Additional note: to extract S3 request ID via CLI. Run command with --debug flag e.g. aws s3 ls --debug 2> s3_log.txt
"""
import sys

FILEPATH = '/path/to/file/s3_log_example.txt'
REQUEST_ID_SHORT = "x-amz-request-id"
REQUEST_ID_LONG = "x-amz-id-2"

def parse_s3_log(filepath):
    print(f'Log at: {filepath}')
    log_lines = []
    with open(filepath) as s3_logs:
        log_lines = s3_logs.readlines()

    # request ID pairs will be written to external file request_ids.txt
    with open('request_ids.txt', 'w') as f:
        sys.stdout = f
        for line in log_lines:
            if REQUEST_ID_SHORT in line:
                id_index = line.find(REQUEST_ID_SHORT)  # get the index where REQUEST_ID_SHORT parameter begins
                # extracts the value for REQUEST_ID_SHORT (hardcoding +4/-4 to extract only the ID)
                short_id = line[len(REQUEST_ID_SHORT) + id_index + 4: line.rfind('Date') - 4]
                print(f'short request ID: {short_id}')

            if REQUEST_ID_LONG in line:
                id_index = line.find(REQUEST_ID_LONG)  # get the index where REQUEST_ID_LONG parameter begins
                # extracts the value for REQUEST_ID_LONG (hardcoding +4/-4 to extract only the ID)
                long_id = line[len(REQUEST_ID_LONG) + id_index + 4: line.rfind('x-amz-request-id') - 4]
                print(f'long request ID: {long_id}')

if __name__ == '__main__':
    parse_s3_log(filepath=FILEPATH)
