from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

auth = Oauth1Authenticator(
    consumer_key=os.environ['CONSUMER_KEY'],
    consumer_secret=os.environ['CONSUMER_SECRET'],
    token=os.environ['TOKEN'],
    token_secret=os.environ['TOKEN_SECRET']
)

# client = Client(auth)

# params = {
#     'term': 'food',
#     'lang': 'en'
# }

# response = client.search('Fayetteville, NC', **params)

# for business in response.businesses: 
# 	print(business.name) 

def get_businesses(term, location):
	client = Client(auth)
	response = client.search(location, {'term': term, 'lang':'en'})
	businesses = []

	for business in response.businesses:
		#print(business.name, business.phone, business.rating)
		businesses.append({"name": business.name,
				"rating": business.rating,
				"phone": business.phone 
		})
	return businesses

businesses = get_businesses('food', 'Fayetteville NC')

print(businesses)