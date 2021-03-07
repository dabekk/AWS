Description
----------

AWS Support will often ask you to provide S3 request IDs. These help support look at the logs of an S3 request with deeper context and allows for better troubleshooting. For more info see here ---> https://aws.amazon.com/premiumsupport/knowledge-center/s3-request-id-values/

This program will help you extract the S3 request IDs for a debug log file of an S3 request.

------------

Input: filepath to an S3 log file
Output: S3 request IDs from log file into a separate text file

Additional note: to extract S3 request ID via CLI. Run command with --debug flag e.g. aws s3 ls --debug 2> s3_log.txt

------------
