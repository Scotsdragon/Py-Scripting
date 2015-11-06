import tweepy

CONSUMER_KEY = 'Qn3eaOCFFEwGAyEq3FnZIEVN6'

CONSUMER_SECRET = '1SR9UBQui7A6nUb5Y1hdGe1ImbSssFo7qW1qfOkJuNeZxQLbks'

ACCESS_TOKEN = '41225557902-gpnDNFnltfTnORtRnjjDMqOQdIRPI7txTBkSlmo'

ACCESS_TOKEN_SECRET = 'Oq5z5ZjRV5dlncndkRabP2BC17sVC1Cmc2phhUGNcLF18'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitter = tweepy.API(auth)

twitter.update_status(status = "hello world")

print ("done, exiting")

