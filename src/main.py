from args import *
from private_info import *
from libs import *


"""
Setting
"""
SEARCH_END_TIME    = "2022-06-15T00:00:00Z"  # UTC
SEARCH_START_TIME  = "2022-06-10T00:00:00Z"  # UTC
SEARCH_WORD_CIRCLE = "あなたのサークル"
SEARCH_WORD_SAT    = "土曜日"
SEARCH_WORD_SUN    = "日曜日"


def main():
    """
    - Args:
    - Returns:
    """
    FollowingUsersList = GetUser_Following(TwitterMyAccountInfo.user_id)
    FollowingUsersTweetsList = GetFollowingUsersTweets(FollowingUsersList, end_time=SEARCH_END_TIME, start_time=SEARCH_START_TIME, process="multi")
    TweetsList_sat = SearchTweetsInTweetsList(FollowingUsersTweetsList, word_0=SEARCH_WORD_CIRCLE, word_1=SEARCH_WORD_SAT)
    TweetsList_sun = SearchTweetsInTweetsList(FollowingUsersTweetsList, word_0=SEARCH_WORD_CIRCLE, word_1=SEARCH_WORD_SUN)
    SaveTweetsListAsCsv(TweetsList_sat, prefix="sat")
    SaveTweetsListAsCsv(TweetsList_sun, prefix="sun")


if __name__ == '__main__' :
    main()
