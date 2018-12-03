import string
import config
import json

import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


if __name__ == '__main__':
    # Call API tokens from separate file 'config.py' !!! must be in same dir
    auth = OAuthHandler(config.consumer_key, config.consumer_secret)
    auth.set_access_token(config.access_token, config.access_secret)
    api = tweepy.API(auth)

    # Location = Washington, DC
    # Uses Yahoo's WOEID
    location_array = ['2514815']
    json_string = json.dumps(api.trends_place(id = location_array[0]))
    storage_loc = json.loads(json_string)
    print(storage_loc)
    f = open('locationData.json', 'wb')
    f.write(json.dumps(storage_loc, indent = 4, sort_keys = True))
    f.close

"""
TODO:
    add selection menu for different WOEIDs
    gui?
    statistics

WOEIDs
    Washington, DC
        2514815
    New York, NY
        2459115
    Atlanta, GA
        2357024
    San Francisco, CA
        2487956
    Houston, TX
        12590119
    Austin, TX
        12590014
    Boston, MA
        2367105
    Miami, FL
        2450022
    Nashville, TN
        2457170
    Denver, CO
        2391279
    St. Louis, MO
        2486982
    Baltimore, MD
        12588678
    Salt Lake City, UT
        2487610
    Chicago, IL
        2379574
    Boise, ID
        12588041
    Orlando, FL
        2466256
    Detroit, MI
        2391585
"""