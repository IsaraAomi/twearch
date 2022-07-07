from args import *
from private_info import *
from libs import *


def main():
    """
    - Args:
    - Returns:
    """
    print(GetUser(TwitterMyAccountInfo.user_id))
    print(GetUser_Following(TwitterMyAccountInfo.user_id))


if __name__ == '__main__' :
    main()
