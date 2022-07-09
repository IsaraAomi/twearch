from args import *
from private_info import *
from libs import *


def main():
    """
    - Args:
    - Returns:
    """
    FollowingUsersList = GetUser_Following(TwitterMyAccountInfo.user_id)
    FollowingUsersTweetsList = GetFollowingUsersTweets(FollowingUsersList, end_time="2022-06-15T00:00:00Z", start_time="2022-06-10T00:00:00Z", process="multi")
    SearchedTweetsList = SearchTweetsInTweetsList(FollowingUsersTweetsList, word="あなたのサークル")
    for i, SearchedTweet in enumerate(SearchedTweetsList):
        print(i, SearchedTweet)
    SaveTweetsListAsCsv(SearchedTweetsList)


if __name__ == '__main__' :
    main()
