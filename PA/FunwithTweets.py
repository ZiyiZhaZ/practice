def tweet_length(tweet):
    x = tweet.split(' ')
    return len(x)

def average_tweet_length(tweet_list):
    x = 0
    if len(tweet_list) == 0:
        return 0
    for i in tweet_list:
        x += tweet_length(i)
    return x / len(tweet_list)

def get_long_tweets(tweet_list):
    x = []
    for i in tweet_list:
        if tweet_length(i) > average_tweet_length(tweet_list):
            x.append(i)
    return x

print(get_long_tweets(['are u telling me a shrimp fried this rice?', 'Anyone see the new Marvel movie?', 'beach vibez today', 'can we talk about the political and economic state of the world?']))