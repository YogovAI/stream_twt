import tweepy
import config


consumer_key=config.API_KEY
consumer_secret=config.API_KEY_SECRET

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_KEY_SECRET)


api=tweepy.API(auth, wait_on_rate_limit=True)

search_words="DMK"

data = tweepy.Cursor(api.search_tweets, q=search_words, tweet_mode='extended').items(10)


for tweet in data:
    text=tweet._json['full_text']
    text=text.encode('utf-8')
    print(text)