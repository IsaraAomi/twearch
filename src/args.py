import argparse
import os
from datetime import datetime
from utils import *


def get_args(date_time=format(datetime.now(), "%Y%m%d-%H%M%S"),
             description=None
             ):
    """
    - Get command line arguments.
    - Arguments set the default values of command line arguments.
    """
    if description is None:
        description = "Search tweets application."
    parser = argparse.ArgumentParser(description)
    parser.add_argument("--date-time", "-d",
                        type=str, default=date_time,
                        help="Date and Time.")
    args = parser.parse_args()
    return args


def print_current_args(args):
    """
    - Args:
        - args (Namespace)
    - Returns:
    """
    print_info("date_time           : {}".format(args.date_time))


def main():
    """
    - Args:
    - Returns:
    """
    args = get_args()
    print_current_args(args)


if __name__ == '__main__':
    main()
