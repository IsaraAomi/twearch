from args import *
from private_info import *
from libs import *


"""
Setting
"""
SEARCH_END_TIME   = "2022-06-15T00:00:00Z"  # UTC
SEARCH_START_TIME = "2022-06-10T00:00:00Z"  # UTC
SEARCH_WORD       = "あなたのサークル"


def main():
    """
    - Args:
    - Returns:
    """
    FollowingUsersList = GetUser_Following(TwitterMyAccountInfo.user_id)
    FollowingUsersTweetsList = GetFollowingUsersTweets(FollowingUsersList, end_time=SEARCH_END_TIME, start_time=SEARCH_START_TIME, process="multi")
    SearchedTweetsList = SearchTweetsInTweetsList(FollowingUsersTweetsList, word=SEARCH_WORD)
    for i, SearchedTweet in enumerate(SearchedTweetsList):
        print_info("{} {}".format(i, SearchedTweet))
    SaveTweetsListAsCsv(SearchedTweetsList)


if __name__ == '__main__' :
    main()
