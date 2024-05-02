#!/usr/bin/env python3
"""This module provides reads staandard inout line by line and
computes metrics"""
from collections import defaultdict

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
    parts = line.split()
    if len(parts) < 10:
        return None
    ip_address = parts[0]
    status_code = parts[-2]
    file_size = parts[-1]
    if not status_code.isdigit():
        return None
    return ip_address, status_code, int(file_size)

def print_stats(file_sizes, status_codes):
    """Prints the computed metrics

    Args:
        file_sizes (list): a list of file sizes
        status_codes (dict): a dictionary of status codes and their counts

    Returns:
        None
    """
    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def main():
    """Reads standard input line by line and computes metrics

    Args:
        None

    Returns:
        None
    """
    file_sizes = []
    status_codes = defaultdict(int)
    try:
        while True:
            try:
                line = input().strip()
            except EOFError:
                break
            parsed = parse_line(line)
            if not parsed:
                continue
            ip_address, status_code, size = parsed
            file_sizes.append(size)
            status_codes[status_code] += 1
            if len(file_sizes) % 10 == 0:
                print_stats(file_sizes, status_codes)
    except KeyboardInterrupt:
        print_stats(file_sizes, status_codes)

if __name__ == "__main__":
    main()
