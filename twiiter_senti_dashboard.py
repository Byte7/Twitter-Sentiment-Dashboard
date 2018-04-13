from tweepy import Stream
from tweepy import OAuthHandler
from tweepy import StreamListener
import json
import sqlite3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from unidecode import unidecode


analyzer = SentimentIntensityAnalyzer()


conn = sqlite3.connect('twitter.db')
c = conn.cursor()


#consumer key, consumer secret, access token, access secret.
ckey=""
csecret=""
atoken=""
asecret=""


class listener(StreamListener):


    def on_data(self, data):
        print(data)
        return (True)


    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)


twitterStream = Stream(auth, listener())
twitterStream.filter(track=["deeplearning"])