import tweepy
import textblob
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xFFFD)

auth = tweepy.OAuthHandler(customer_key, customer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
c = 0
# public_tweets = []
for i in range(10):

    public_tweets = api.search("Trump", rpp=100)

    for tweet in public_tweets:
        c += 1
        a = tweet.text
        print(a.translate(non_bmp_map))
        analysis = textblob.TextBlob(a.translate(non_bmp_map))
        print(analysis.sentiment)

print(c)
