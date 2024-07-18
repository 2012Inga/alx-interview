#!/usr/bin/python3
import sys
import signal
import re

# Initialize global variables
total_file_size = 0
status_code_counts = {
    '200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0
}
line_count = 0

# Regular expression to match the log format
log_regex = re.compile(r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')

def print_stats():
    """Prints the current statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handles the keyboard interruption (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Set the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        match = log_regex.match(line)
        if match:
            status_code = match.group(1)
            file_size = int(match.group(2))
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        
        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except Exception as e:
    print(f"Error: {e}")

# Final stats print at the end of the input
print_stats()
