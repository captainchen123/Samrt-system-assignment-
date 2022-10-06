# this code is reference from https://github.com/mlachha/Twitter_nlp/blob/main/twitter

import numpy as np
import pandas as pd
import tweepy
from IPython.core.display_functions import display
from tweepy import Client

keyword = input('insert search term : ')
query = f'{keyword} -is:retweet lang:en'
num_tweets = int(input('how many tweets do you want? '))

# connecting to the Twitter API using client and the bearer_token credentials from my account
bt = "AAAAAAAAAAAAAAAAAAAAABx5hgEAAAAATZmJf8E%2FJ9gpDZ4DDIMmOsXhseo" \
     "%3Dn8S0Y5VCbf3tnAhBPORztxSYuNNiLsvt0Qs3p8j2XP8uv3qWGa "
client = Client(bearer_token=bt)

# using tweepy paginator to get over the number of tweets users want to from Twitter api
tweets = []
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query,
                              tweet_fields=['id', 'created_at', 'public_metrics', 'text', 'source'],
                              max_results=100).flatten(limit=num_tweets):
    tweets.append(tweet)

# print 10  tweets from Twitter api
print(num_tweets, "tweets from twitter api")
print("10 tweets from twitter api")
print('-----------------------------------------')
for tweet in tweets[:10]:
    print(tweet.text)
    print()
print("\n")

# create a Pandas dataframe
data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
data['len'] = np.array([len(tweet.text) for tweet in tweets])
data['ID'] = np.array([tweet.id for tweet in tweets])
data['Date'] = np.array([tweet.created_at for tweet in tweets])
data['Source'] = np.array([tweet.source for tweet in tweets])
display(data.head(10))

# this aims to get the average of text length
mean = np.mean(data['len'])
print("The length's average in tweets: {}".format(mean))
print("--------------------------------")
print("\n")

# This is to get the platforms to send the twitter and print it
platform = []
for source in data['Source']:
    if source not in platform:
        platform.append(source)

print("Creation of platforms sources:")
for source in platform:
    print("* {}".format(source))
