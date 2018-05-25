import tweepy
import textblob
import sys

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

customer_key = 'OL17271oHF6LshYq348gagKyb'
customer_secret = 'FaFioKFtYRsXWgWz9eUayBH0jWrl6Oc5SWjQt2267qAGQB6ZdR'

access_token = '999913247665876992-DXzbVUJWwnBbXidQB3oO47RPUysAz2q'
access_token_secret = 'deSMGo0unYa2mik1FShfd4wH0pGFCO88o0m3uLdF1gmiE'

auth = tweepy.OAuthHandler(customer_key,customer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
c=0
#public_tweets = []
for i in range(10):

    public_tweets = api.search('Trump' , rpp = 100)


    for tweet in public_tweets:
        c += 1
        a = tweet.text
        print(a.translate(non_bmp_map))
        analysis = textblob.TextBlob(a.translate(non_bmp_map))
        print(analysis.sentiment)

print(c)
