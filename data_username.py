# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 23:38:49 2018

@author: Bansi
"""

import tweepy
 
# Fill the X's with the credentials obtained by 
# following the above mentioned procedure.
consumer_key = "w8wyoAKvlN9MEDR18HFzKyzUA"
consumer_secret = "W4R5i6VAkTgs6Tr6Ij3Jfk8x6k1rkqdPzb5R2JkFq2ccTQqdVr"
access_key = "Y4rxXI6s8TDmJD5YQZLRqHLPb7d9iTBFi40eoO7weE7Sw"
access_secret = "4157664553-PmCikHvFMBXmUf71TruTVi4hg8L4s2kdYaZgg5i" 
username = input('Enter person name: ');
# Function to extract tweets
def get_tweets(username):
         
        # Authorization to consumer key and consumer secret
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 
        # Access to user's access key and access secret
        auth.set_access_token(access_key, access_secret)
 
        # Calling api
        api = tweepy.API(auth)
 
        # 200 tweets to be extracted
        number_of_tweets=200
        tweets = api.user_timeline(screen_name=username)
 
        # Empty Array
        tmp=[] 
 
        # create array of tweet information: username, 
        # tweet id, date/time, text
        tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created 
        for j in tweets_for_csv:
 
            # Appending tweets to the empty array tmp
            tmp.append(j) 
 
        # Printing the tweets
        print(tmp)
 
 
# Driver code
if __name__ == '__main__':
 
    # Here goes the twitter handle for the user
    # whose tweets are to be extracted.
    get_tweets("twitter-handle") 