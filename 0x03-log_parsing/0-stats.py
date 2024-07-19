#!/usr/bin/python3
"""
log parser module
"""
import sys


def print_stats(codes, tot_size):
    print("File size: {}".format(tot_size))
    for k, v in codes.items():
        if v != 0:
            print("{}: {}".format(k, v))


if __name__ == "__main__":
    counter = 0
    tot_size = 0
    codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
    }

    try:
        for line in sys.stdin:
            data = line.rstrip().split(' ')[-2:]
            s_code = data[0]
            f_size = int(data[1])

            codes[s_code] += 1
            tot_size += f_size

            counter += 1
            if counter == 10:
                print_stats(codes, tot_size)
                counter = 0
    except KeyboardInterrupt:
        print_stats(codes, tot_size)
