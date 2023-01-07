import tweepy
import config

client=tweepy.Client(bearer_token=config.BEARER_TOKEN)

#client=tweepy.Client("AAAAAAAAAAAAAAAAAAAAAHhFkwEAAAAAMVh%2FcqXshg9SKxqSN%2BSNSMkF7mo%3D7DgdZo4mLn6Af05tadTsLBaDtWsr48VGrXG1dg4Vc0COQZisBl")

query='DMK -is:retweet'

response = client.search_recent_tweets(query=query, max_results=100)

# print(response)

result=[]
for i in response.data:
    txt=i.text
    txt=txt.encode('utf-8')
    print(txt)
    # result.append(i.text)
    # print(i.text)
