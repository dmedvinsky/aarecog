#!/usr/bin/env python
"""
aarecog -- ASCII Art Recognizer
"""
import io
import os
import sys
import logging

from recognizer import Recognizer


def main(args):
    """Entry point."""
    # TODO Replace with argparse
    if len(args) > 1 and os.path.isfile(args[1]):
        with io.open(args[1], 'r', encoding='utf-8') as f:
            data = f.read()
    else:
        stream = io.open(sys.stdin.fileno(), 'r', encoding='utf-8')
        data = stream.read()
    # TODO add '--verbose' flag to disable logging
    logging.basicConfig(format='%(levelname)s %(name)s: %(message)s',
                        level=logging.DEBUG)
    recognizer = Recognizer()
    result = recognizer.recognize(data)
    print(','.join(result))


if __name__ == "__main__":
    main(sys.argv)
