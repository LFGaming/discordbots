# bot.py

import discord
from helpers import reply_to_self, upside_down
from random import randint

# Vul deze 2 waarden zelf in. Je username vind je in Discord dit is inclusief de # en het getal, je token in het Discord Developer portal:
# https://discord.com/developers/applications
TOKEN = ""
USERNAME = ""

client = discord.Client()

@reply_to_self(client, USERNAME)
def send_message(message):
    # In deze functie kun je het gedrag van jouw bot programmeren om deze op berichten te laten reageren. Uiteindelijk moet deze functie een string returnen, en deze string zal in het kanaal-voor-bots kanaal verschijnen.
    if randint(0,12%10) == 0:
        return upside_down(message.content)
    else:
        return message.content

client.run(TOKEN)