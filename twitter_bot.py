import tweepy
import time

auth = tweepy.OAuthHandler("cP8lU6MTJ1OjKimQXtFipA8Ee",
                          "35T0gkUSahEYHFPZSIbb60dCdJtQ4xMjqEytZ24nnAPj3m6SZK")

auth.set_access_token("1369166210005430272-owNgAVnExovA4TNAuXUGNnSFhm2Vnj",
                      "iaLpko9bZnev21Lz5peOwlzvxmgWXmtB4bbYQcGHONFch")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()


search = 'vai corinthians'
nrTweets = 90

for tweets in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print("Tweet retuitado")
        tweets.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
api.update_status("Test tweet from Tweepy Python")
