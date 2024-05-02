#!/usr/bin/env python3
from collections import defaultdict

def parse_line(line):
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
    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

def main():
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
