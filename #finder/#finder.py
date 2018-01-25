from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = '9zlg7bmDonGmJw7WTyuqkhRlU'
csecret = 'LEoYFjlsyxXzWZi7Y6AKoAE65YMG7ahWBRcW6FBVAPEdLPHfzt'
atoken = '797023459306041345-GWX8o22txQvT2vgxK5nNLAw2hmGfs3n'
asecret = '4A9aOufn7iteuYVglssGTQwtws2MBGHBZj4rqPxmELkwZ'


class listener(StreamListener):

    def on_data(self,data):
        try:
            
            tweet = data.split(',"text":"')[1].split('",source"')[0]
            print(tweet)

            saveThis = str(time.time())+'::'+tweet
            saveFile = open('twitDB3.csv','a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException as e:
            print('Failed ondata',str(e))
            time.sleep(5)
    
    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#awesome"])
