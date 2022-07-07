import tweepy
from args import *
from private_info import *


def ClientInfo():
    """
    - Args:
    - Returns:
    """
    client = tweepy.Client(bearer_token        = TwitterApiInfo.bearer_token,
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
    """
    tweets = ClientInfo().search_recent_tweets(query = search, max_results = tweet_max)
    results     = []
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


def GetTweet(tweet_id):
    """
    - Args:
        - tweet_id (int)
    - Returns:
    """
    GetTwt = ClientInfo().get_tweet(id=tweet_id, expansions=["author_id"], user_fields=["username"])
    twt_result = {}
    twt_result["tweet_id"] = tweet_id
    twt_result["user_id"]  = GetTwt.includes["users"][0].id
    twt_result["username"] = GetTwt.includes["users"][0].username
    twt_result["text"]     = GetTwt.data
    twt_result["url"]      = "https://twitter.com/" + GetTwt.includes["users"][0].username + "/status/" + str(tweet_id)
    return twt_result


def GetUser(user_id):
    """
    - Args:
        - user_id (int)
    - Returns:
    """
    GetUser = ClientInfo().get_user(id=user_id).data
    result  = {}
    result["user_id"]  = user_id
    result["name"]     = GetUser.name
    result["username"] = GetUser.username
    return result


def GetUser_Following(user_id):
    """
    - Args:
        - user_id (int)
    - Returns:
    """
    followers = ClientInfo().get_users_following(id=user_id)
    results     = []
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
