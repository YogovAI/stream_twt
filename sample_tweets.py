import tweepy
import config


consumer_key=config.API_KEY
consumer_secret=config.API_KEY_SECRET

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_KEY_SECRET)


api=tweepy.API(auth, wait_on_rate_limit=True)


public_tweets=api.home_timeline()
count=0
for tweet in public_tweets:
    count=count+1
    print("Tweet #"+str(count)+"\n")
    twt=tweet.text
    twt=twt.encode('utf-8')
    print(twt)
    print("----------------------------------------------------------------------------------------------------------------------------------")

