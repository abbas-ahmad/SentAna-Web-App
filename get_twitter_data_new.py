from tweepy import OAuthHandler
import sent_mod as s
import json
import urllib
import oauth2



#consumer key, consumer secret, access token, access secret.
ckey="OIKCszkBhnEFfb23n4CDNyM9Q"
csecret="ZmqXnvesSBVtOJtpy9SymtiJX0ejYjMCTN1cohjrMiEIj4tNx9"
atoken="754575162696015872-OiByOkiFnRD3wZRYYIqdVZLgSdPFD1A"
asecret="0uCtVHGQpQzAOSs61Lp3ZdSZKKr3m9HFhGgKJbCn5nQUm"

#auth = OAuthHandler(ckey, csecret)
#auth.set_access_token(atoken, asecret)

def oauth_req(url, http_method="GET", post_body='', http_headers=None):
    consumer = oauth2.Consumer(key=ckey, secret=csecret)
    token = oauth2.Token(key=atoken, secret=asecret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content


def get_tweet(keyword):
        maxTweets = 100
        url = 'https://api.twitter.com/1.1/search/tweets.json?'
        data = {'q': keyword, 'lang': 'en', 'result_type': 'recent', 'count': maxTweets, 'include_entities': 0}

        url += urllib.urlencode(data)

        response = oauth_req(url)
        jsonData = json.loads(response)
        #tweet = jsonData['text']
        #sentiment_value = s.sentiment(tweet)
        #print(tweet , sentiment_value)       
        tweets = []
        if 'errors' in jsonData:
            print "API Error"
            print jsonData['errors']
        else:
            for item in jsonData['statuses']:
                tweet = item['text']
                if len(tweets) < 11:
                    tweets.append(tweet)
                sent = s.sentiment(tweet)
                #print(tweet + ':' , sent)
                output = open("twitter_out.txt" , 'a')
                output.write(sent)
                output.write("\n")
                output.close()
        return tweets
#testing
#get_tweet("hawking")
