#!/usr/bin/python3
"""Documentation"""
import re
import sys

count = {
    'File size': 0,
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}


def update_status(code: int) -> None:
    """
    Update the count of a given status code.

    Args:
        code (int): The status code to update.

    Returns:
        None
    """
    if code in count:
        count[code] += 1


def check_input(line):
    """
    Check if the given line matches the expected pattern for log entries.

    Args:
        line (str): The log entry to be checked.

    Returns:
        bool: True if the line matches the pattern, False otherwise.
    """
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - ' \
              r'\[.+\] "GET \/projects\/\d+ HTTP\/1\.1" \d+ \d+$'
    if re.match(pattern, line):
        return True
    else:
        return False


line_count = 0

try:
    for line in sys.stdin:
        if check_input(line):
            size = re.findall(r'\b\d+\b', line)[-1]
            status = re.findall(r'\b\d+\b', line)[-2]
            count['File size'] += int(size)
            update_status(int(status))
            line_count += 1
            if line_count % 10 == 0:
                print("File size: {}".format(count['File size']))
                for key in sorted(filter(lambda x:
                                         isinstance(x, int), count.keys())):
                    if count[key] > 0:
                        print("{}: {}".format(key, count[key]))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(count['File size']))
    for key in sorted(filter(lambda x: isinstance(x, int), count.keys())):
        if count[key] > 0:
            print("{}: {}".format(key, count[key]))
