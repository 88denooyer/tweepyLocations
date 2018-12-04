# tweepyLocations
Pulling twitter data using Tweepy

## Requirements
- Twitter Dev Account
  - Apply for one [here](https://developer.twitter.com/)
- Tweepy
  - run `pip install tweepy` on the command line

## How to Run!

```
mkdir <folder name>
cd <folder name>
vi config.py
```

Add the following lines to the `config.py` file
```
consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''
```
Get your keys and tokens from your Dev account

run `python twitter_location_data.py`

This will create a JSON file titled `locationData.json` in the directory
