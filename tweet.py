import tweepy
import keys
import sys

def api():
    auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
    auth.set_access_token(keys.access_token, keys.access_token_secret)

    return tweepy.API(auth)

def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)

    print('Tweeted successfully!')

def tweet_help():
    print("tweet.py -t <text>")
    print("tweet.py -h")
    print("tweet.py -t <text> -i <img>")
    sys.exit()
def get_argvs():
    agv = sys.argv
    try:
        if agv.index("-h"):
            tweet_help()
    except:
        pass
    try:
        text = agv[agv.index("-t")+1]
    except:
        tweet_help()
        sys.exit()

    try:
        img_path = agv[agv.index("-i")+1]
        tweet(api(), text, img_path)
    except:
        img_path = None
        tweet(api(), text)
    
if __name__ == '__main__':
    get_argvs() 
     
