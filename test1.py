import tweepy
# assuming twitter_authentication.py contains each of the 4 oauth elements (1 per line)
#from twitter_authentication import API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

auth = tweepy.OAuthHandler("w8wyoAKvlN9MEDR18HFzKyzUA", "W4R5i6VAkTgs6Tr6Ij3Jfk8x6k1rkqdPzb5R2JkFq2ccTQqdVr")
auth.set_access_token("4157664553-PmCikHvFMBXmUf71TruTVi4hg8L4s2kdYaZgg5i", "Y4rxXI6s8TDmJD5YQZLRqHLPb7d9iTBFi40eoO7weE7Sw")

api = tweepy.API(auth)

query = 'narendramodi'
max_tweets = 10
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
print(searched_tweets)