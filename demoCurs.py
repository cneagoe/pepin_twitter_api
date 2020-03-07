import tweepy as tw
from configparser import SafeConfigParser
configParser = SafeConfigParser()
configParser.read('config.ini')
consumer_key = configParser.get('config', 'consumer_key')
consumer_secret = configParser.get('config', 'consumer_secret')
access_token_key = configParser.get('config', 'access_token_key')
access_token_secret = configParser.get('config', 'access_token_secret')
auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)  ##aici s-a creat obiectul conexiune twitter
api.verify_credentials() ##endpoint  account/verify_credentials
usr_id = api.get_user(screen_name="CiprianNeagoe1").id
directMessage = api.send_direct_message(usr_id, "Scoala de Valori e SUPER.")##endpoint direct_messages/events/new.json
print("Mesajul a fost transmis")
