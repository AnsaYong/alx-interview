#!/usr/bin/python3
"""This module provides reads staandard inout line by line and
computes metrics"""
import sys
import re
import signal


# Initialize variables
total_size = 0
line_count = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}


def handler(signal, frame):
    """Signal handler for SIGINT

    Args:
        signal: the signal number
        frame: the current stack frame

    Returns:
        None
    """
    print_stats()
    sys.exit(0)


def parse_line(line):
    """Parses a line of format
    `<IP Address> -
        [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`
    and extracts the relevant metrics

    Args:
        line (str): a line of the log file

    Returns:
        file_size (int): the total file size
        status_code (int): the status code
        ip_address: the IP address
        date: the date
        None: if the line does not match the pattern
    """
    pattern = (r"(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] \"GET /projects/260 HTTP/1\.1\" (\d+) (\d+)")
    match = re.match(pattern, line)
    if match:
        ip_address, date, status_code, file_size = match.groups()
        return int(file_size), int(status_code), ip_address, date
    else:
        return None


def print_stats():
    """Prints the computed metrics

    Args:
        None
    Returns:
        None
    """
    print("File size: {}".format(total_size))
    for k, v in sorted(status_codes.items()):
        if v > 0:
            print("{}: {}".format(k, v))


# Register signal handler (to handle ctrl+c)
signal.signal(signal.SIGINT, handler)

# Read line by line from stdin
for line in sys.stdin:
    line = line.strip()
    metrics = parse_line(line)
    if metrics:
        file_size, status_code, ip_address, date = metrics
        total_size += file_size
        status_codes[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats()
