#!/usr/bin/python2.7
import requests
from slackclient import SlackClient
import time



SLACK_TOKEN = "YOUR TOKEN"

SLACK_CHANNEL = "#weather"

# example location, feel free to change to desired location
tel_aviv = "32.109333,34.855499"

Kiryat_Ekron = "31.8625,34.8220"

client = SlackClient(SLACK_TOKEN)



req = requests.get("https://api.darksky.net/forecast/5a90be64679ebcbef214eefa1be6c2f5/" + Kiryat_Ekron + "?lang=en&units=si")
json_KE = req.json()
client.api_call("chat.postMessage", channel=SLACK_CHANNEL, text=("@Here   Today in Kiryat Ekron will be : " + json_KE['currently']['summary'] + ". The Temperature High : " + str(json_KE['daily']['data'][0]['temperatureHigh']) + " and Temperature Low : " + str(json_KE['daily']['data'][0]['temperatureLow'])) ,username='Kiryat Ekron' , icon_emoji=':weather:')

time.sleep(5)

req2 = requests.get("https://api.darksky.net/forecast/5a90be64679ebcbef214eefa1be6c2f5/" + tel_aviv + "?lang=en&units=si")
json_TA = req2.json()
client.api_call("chat.postMessage", channel=SLACK_CHANNEL, text=("@Here   Today in Tel Aviv will be : " + json_TA['currently']['summary'] + ". The Temperature High : " + str(json_TA['daily']['data'][0]['temperatureHigh']) + " and Temperature Low : " + str(json_TA['daily']['data'][0]['temperatureLow'])) ,username='Tel Aviv', icon_emoji=':weather:')
print(1)
