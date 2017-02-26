import twitter 
## https://github.com/bear/python-twitter
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                  consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                  access_token_key=os.environ['TWTTER_ACCESS_TOKEN'],
                  access_token_secret=os.environ['TWITTER_TOKEN_SECRET'])

def get_statuses(handle):
	user = handle
	statuses = api.GetUserTimeline(screen_name=user)
	return([s.text for s in statuses])

print(get_statuses('emilielimaburke'))

def post_status(update):
	status = api.PostUpdate(update)
	return(status)

print(post_status('I feel very successful now.'))
