from twython import Twython

import settings


MAX_TWEETS = 200
CLIENT = Twython(settings.APP_KEY, settings.APP_SECRET, settings.TOKEN, settings.TOKEN_SECRET)


def fetch_tweets():
    tweets = CLIENT.get_user_timeline(count=MAX_TWEETS)
    for tweet in tweets:
        yield tweet
    while tweets:
        tweets = CLIENT.get_user_timeline(count=MAX_TWEETS)
        for tweet in tweets:
            yield tweet

def delete_tweets():
    for tweet in fetch_tweets():
        tweet_id = tweet['id']
        print("Deleting tweet \"{}\".".format(tweet['text']))
        CLIENT.destroy_status(id=tweet_id)


if __name__ == '__main__':
    delete_tweets()
