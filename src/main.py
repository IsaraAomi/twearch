from args import *
from private_info import *
from libs import *
from word_cloud import *

"""
Setting
"""
SEARCH_END_TIME    = "2022-09-25T00:00:00Z"  # UTC
SEARCH_START_TIME  = "2022-01-01T00:00:00Z"  # UTC

def main():
    """
    - Args:
    - Returns:
    """
    User = GetUser(TwitterMyAccountInfo.user_id)
    print(User)
    TweetsList = GetUsersAllTweets(user_id=User["user_id"], end_time=SEARCH_END_TIME, start_time=SEARCH_START_TIME, max_results=100)
    file_path = SaveTweetsListAsCsv(TweetsList)
    create_word_cloud_from_csv(file_path)


if __name__ == '__main__' :
    main()
