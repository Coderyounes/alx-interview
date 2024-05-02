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


line_count = 0

try:
    for line in sys.stdin:
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
