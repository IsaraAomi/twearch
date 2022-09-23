import csv
import time
import tweepy
import multiprocessing
from tqdm import tqdm
import pprint
from args import *
from private_info import *
from utils import *


SHORT_PROGRESS_BAR="{l_bar}{bar:20}{r_bar}{bar:-10b}"


def Client():
    """
    - Args:
    - Returns:
        - (Client)
    """
    client = tweepy.Client(
        bearer_token        = TwitterApiInfo.bearer_token,
        consumer_key        = TwitterApiInfo.consumer_key,
        consumer_secret     = TwitterApiInfo.consumer_secret,
        access_token        = TwitterApiInfo.access_token,
        access_token_secret = TwitterApiInfo.access_token_secret
    )
    return client


def SearchTweets(search, tweet_max):
    """
    - Args:
        - search (str)
        - tweet_max (int)
    - Returns:
        - (list(dict))
    """
    tweets = Client().search_recent_tweets(query=search, max_results=tweet_max)
    results = []
    tweets_data = tweets.data
    if tweets_data != None:
        for tweet in tweets_data:
            obj = {}
            obj["tweet_id"] = tweet.id
            obj["text"] = tweet.text
            results.append(obj)
    else:
        results.append('')
    return results


def SearchTweetsInTweetsList(TweetsList, word_0, word_1):
    """
    - Args:
        - TweetsList (list(dict))
        - word_0 (str)
        - word_1 (str)
    - Returns:
        - results (list(dict))
    """
    results = []
    for Tweet in TweetsList:
        if ((word_0 in Tweet["text"]) and (word_1 in Tweet["text"])):
            results.append(Tweet)
    return results


def GetTweet(tweet_id):
    """
    - Args:
        - tweet_id (int)
    - Returns:
        - (dict)
    """
    GetTwt = Client().get_tweet(id=tweet_id, expansions=["author_id"], user_fields=["username"])
    twt_result = {}
    twt_result["tweet_id"] = tweet_id
    twt_result["user_id"]  = GetTwt.includes["users"][0].id
    twt_result["username"] = GetTwt.includes["users"][0].username
    twt_result["text"]     = GetTwt.data
    twt_result["url"]      = "https://twitter.com/" + GetTwt.includes["users"][0].username + "/status/" + str(tweet_id)
    return twt_result


def GetUsersTweets(user_id, end_time, start_time, max_results=100):
    """
    - Args:
        - user_id (int)
        - end_time (str)
        - start_time (str)
        - max_results (int)
    - Returns:
        - list(dict)
    """
    tweets = Client().get_users_tweets(id=user_id, end_time=end_time, exclude=["retweets", "replies"], expansions=["author_id"], max_results=max_results, start_time=start_time, user_fields=["name", "username"])
    # print(tweets)
    results = []
    tweets_data = tweets.data
    if tweets_data != None:
        for tweet in tweets_data:
            obj = {}
            # obj["tweet_id"] = tweet.id
            # obj["user_id"]  = tweets.includes["users"][0].id
            obj["name"] = tweets.includes["users"][0].name
            obj["userurl"] = "https://twitter.com/" + tweets.includes["users"][0].username
            obj["text"] = tweet.text
            results.append(obj)
    else:
        results.append('')
    return results


def GetUsersAllTweets(user_id, end_time, start_time, max_results=100, next_token=None):
    """
    - Args:
        - user_id (int)
        - end_time (str)
        - start_time (str)
        - max_results (int)
    - Returns:
        - list(dict)
    """
    results = []
    trial_id = 0
    while True:
        print(f"trial_id = {trial_id}")
        tweets = Client().get_users_tweets(id=user_id, end_time=end_time, exclude=["retweets", "replies"], expansions=["author_id"], start_time=start_time, max_results=max_results, user_fields=["name", "username"], pagination_token=next_token)
        # pprint.pprint(tweets)
        if (tweets.data != None):
            for tweet in tweets.data:
                obj = {}
                # obj["tweet_id"] = tweet.id
                # obj["user_id"]  = tweets.includes["users"][0].id
                obj["name"] = tweets.includes["users"][0].name
                obj["userurl"] = "https://twitter.com/" + tweets.includes["users"][0].username
                obj["text"] = tweet.text
                results.append(obj)
        else:
            results.append('')
        # pprint.pprint(results)
        print(tweets.meta["result_count"])
        if ("next_token" not in tweets.meta):
            break
        next_token = tweets.meta["next_token"]
        trial_id += 1
        # time.sleep(12)
    return results


def wrap_GetUsersTweets(args):
    return GetUsersTweets(*args)


def GetUser(user_id):
    """
    - Args:
        - user_id (int)
    - Returns:
        - (dict)
    """
    GetUser = Client().get_user(id=user_id).data
    result = {}
    result["user_id"]  = user_id
    result["name"]     = GetUser.name
    result["username"] = GetUser.username
    return result


def GetUser_Following(user_id):
    """
    - Args:
        - user_id (int)
    - Returns:
        - (list(dict))
    """
    followers = Client().get_users_following(id=user_id, max_results=1000)
    results = []
    followers_data = followers.data
    if followers_data != None:
        for tweet in followers_data:
            obj = {}
            obj["user_id"]  = tweet.id
            obj["name"]     = tweet.name
            obj["username"] = tweet.username
            results.append(obj)
    else:
        results.append('')
    return results


def GetTweets(UsersList, end_time, start_time, max_results=100, process="multi"):
    """
    - Args:
        - UsersList (list)
    - Returns:
        - results (list(dict))
    """
    results = []
    if (process == "single"):
        for FollowingUser in tqdm(UsersList, bar_format=SHORT_PROGRESS_BAR):
            UserTweets = GetUsersTweets(user_id=FollowingUser["user_id"], end_time=end_time, start_time=start_time, max_results=max_results)
            if UserTweets != ['']:
                for UserTweet in UserTweets:
                    results.append(UserTweet)
    elif (process == "multi"):
        pool = multiprocessing.Pool(processes=multiprocessing.cpu_count()-1)
        args = []
        for FollowingUser in UsersList:
            args.append((FollowingUser["user_id"], end_time, start_time, max_results))
        imap = pool.imap(wrap_GetUsersTweets, args)
        UserTweetsList = list(tqdm(imap, total=len(args), bar_format=SHORT_PROGRESS_BAR))
        for UserTweets in UserTweetsList:
            if UserTweets != ['']:
                for UserTweet in UserTweets:
                    results.append(UserTweet)
    else:
        print_error("process is incorrect.")
    return results


def SaveTweetsListAsCsv(TweetsList, prefix=None):
    """
    - Args:
        - TweetsList (list(dict))
        - prefix (str)
    - Returns:
        - file_path (str)
    """
    args = get_args()
    save_dir = os.path.join("..", "data")
    if (prefix):
        save_filename = prefix+"_list_"+args.date_time+".csv"
    else:
        save_filename = "list_"+args.date_time+".csv"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    file_path = os.path.join(save_dir, save_filename)
    with open(file_path, 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for Tweet in TweetsList:
            TweetLine = [Tweet["name"], Tweet["userurl"], Tweet["text"].replace('\n', '')]
            writer.writerow(TweetLine)
    return file_path


def main():
    """
    - Args:
    - Returns:
    """
    UsersTweets = GetUsersTweets(user_id=TwitterMyAccountInfo.user_id, end_time="2022-06-15T00:00:00Z", start_time="2022-06-10T00:00:00Z")
    print(UsersTweets)
    print(len(UsersTweets))


if __name__ == '__main__' :
    main()
