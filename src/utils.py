import sys


def print_error(object, file=sys.stdout):
    """
    - Args:
        - object
        - file
    - Returns:
    """
    print("[ERROR] {}".format(object), file=file)
    print("[ERROR] Exit this program...", file=file)
    sys.exit(1)


def print_warning(object, file=sys.stdout):
    """
    - Args:
        - object
        - file
    - Returns:
    """
    print("[WARNING] {}".format(object), file=file)


def print_info(object, file=sys.stdout):
    """
    - Args:
        - object
        - file
    - Returns:
    """
    print("[INFO] {}".format(object), file=file)


def main():
    print_info("test info")
    print_warning("test warning")
    print_error("test error")


if __name__ == '__main__':
    main()
