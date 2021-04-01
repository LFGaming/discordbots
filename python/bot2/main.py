# bot.py

import discord
from helpers import reply_to_self, upside_down
from random import randint

# Vul deze 2 waarden zelf in. Je username vind je in Discord dit is inclusief de # en het getal, je token in het Discord Developer portal:
# https://discord.com/developers/applications

client = discord.Client()

@reply_to_self(client, USERNAME)
def send_message(message):
    # In deze functie kun je het gedrag van jouw bot programmeren om deze op berichten te laten reageren. Uiteindelijk moet deze functie een string returnen, en deze string zal in het kanaal-voor-bots kanaal verschijnen.
    if randint(0,12%10) == 0:
        return upside_down(message.content)
    else:
        return message.content

#eigen
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added.")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del",1)[1])
      delete_encouragment(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)
    
  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on.")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off.")

  if msg.startswith('$hello'):
       await message.channel.send('Hello!')

  if msg.startswith('$author'):
       await message.channel.send('I am made by @LFGaming, https://github.com/LFGaming')
       
  if message.content.startswith('$help'):
       await message.channel.send(" $hello : sents a `Hello!` back \n $help : sents a help message \n $inspire : sents a inpiering message \n $new : sents a encouragement to you \n $list : lists the messages \n $author : sents a credit message.")


client.run(TOKEN)