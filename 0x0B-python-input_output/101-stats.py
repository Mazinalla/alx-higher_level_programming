#!/usr/bin/python3


import sys
from collections import defaultdict
import signal

# Initialize variables
total_file_size = 0
status_code_counts = defaultdict(int)
lines_processed = 0

def print_statistics(signum, frame):
    # Print statistics upon interruption (CTRL + C)
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
    sys.exit(0)

# Register signal handler for CTRL + C
signal.signal(signal.SIGINT, print_statistics)

try:
    # Read stdin line by line
    for line in sys.stdin:
        # Split the input line into components
        parts = line.split(" ")

        # Extract relevant information
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1
        lines_processed += 1

        # Print statistics every 10 lines
        if lines_processed % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code in sorted(status_code_counts.keys()):
                print(f"{code}: {status_code_counts[code]}")

except KeyboardInterrupt:
    # Handle manual interruption (CTRL + C)
    pass

# Print final statistics
print_statistics(None, None)

