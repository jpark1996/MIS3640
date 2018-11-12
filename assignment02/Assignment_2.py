import re 
import tweepy 
from tweepy import OAuthHandler 
from textblob import TextBlob 
  
class TwitterClient(object): # generic class for sentiment analysis
    def __init__(self): # Keys and Token from Twitter API. (I borrowed from Donghyun since it took time to get accepeted for developer's twitter account)
        access_token = '295995929-EF7PArCGbluVIJjVRUz3aYPwhkQA76lNkFTXlBQ3'
        access_token_secret = '1hkQaoUXT8DLjmDxbyGEHE8KDxvFH1e7asIorx4OFKUch'
        consumer_key = 'mVOQriBHMwFeT6sWsj6gIl4PE'
        consumer_secret = 'hkbTzvBP32JINElkMQ2TY3Lxi8qB0X5izqW9inzI5qP8iQ41ob'
         
        try: # authenticaion process.    
            self.auth = OAuthHandler(consumer_key, consumer_secret) # creating OAuthHandler Object 
            self.auth.set_access_token(access_token, access_token_secret) # Then setting access token and secret  
            self.api = tweepy.API(self.auth) # Lastly, creating Tweepy API object to fetch tweets 
        except: 
            print("Error: Authentication Failed") 

    def clean_tweet(self, tweet): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])(\w+:\/\/\S+)", " ", tweet).split()) # In order to make the tweet look clean, erased special characters and links. 

    def get_tweet_sentiment(self, tweet): 
        analysis = TextBlob(self.clean_tweet(tweet)) # using TextBlob to do sentiment analysis on tweet that I searched (and cleaned from clean_tweet function)
        if analysis.sentiment.polarity > 0: 
            return 'positive' # if polarity of the sentiment analysis is greater than 0, it will classify as positive 
        elif analysis.sentiment.polarity == 0: 
            return 'neutral' # if polarity of the sentiment analysis is equal to 0, it will classfiy as neutral
        else: 
            return 'negative' # if else, which means it is less than 0, it will classify as negative 
  
    def get_tweets(self, query, count = 10): # main function to fetch and parse tweets
        tweets = [] # empty list in order to store the tweets 
        try: 
            fetched_tweets = self.api.search(q = query, count = count) # call api to fetch tweets
  
            for tweet in fetched_tweets: 
                parsed_tweet = {} # empty dictionary to store required parsed tweet
   
                parsed_tweet['text'] = tweet.text  #saving text of the tweets
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) #saving sentiment of the tweets 
  
                if tweet.retweet_count > 0: # in order to make sure the tweet is not duplicated, if there is more than one retweet, the tweet will append only one time 
                    if parsed_tweet not in tweets: 
                        tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet) 
  
            return tweets 
  
        except tweepy.TweepError as e:  
            print("Error : " + str(e)) # print error if any error occurs 
  
def main(): 
    api = TwitterClient()  
    tweets = api.get_tweets(query = '#Jimmybutlertrade', count = 250)  # Calling function to get tweets (tweets you want and totla count of that tweets)
  
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive'] # picking positve tweets from the tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))  # percentage of that postive tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']  # picking negative tweets from the tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets))) # percentage of that negative tweets 
  
    # printing first 5 positive tweets 
    print("\n\nPositive tweets:") 
    for tweet in ptweets[:10]: 
        print(tweet['text']) 
  
    # printing first 5 negative tweets 
    print("\n\nNegative tweets:") 
    for tweet in ntweets[:10]: 
        print(tweet['text']) 
  
if __name__ == "__main__": 
    main()