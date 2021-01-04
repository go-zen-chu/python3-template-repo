#!/usr/bin/env python3
import argparse
import show

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='just print args')
    parser.add_argument('--debug', default=False)
    args = parser.parse_args()
    show.show(args)
    print("done")
