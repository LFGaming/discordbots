from upsidedown import ud_letters

def reply_to_self(client, user):
    username, discriminator = user.split('#')
    def reply_to_self_impl(func):
        @client.event
        async def on_message(message):
            if message.author.name != username or message.author.discriminator != discriminator or message.channel.name != 'kanaal-voor-bots':
                return
            reply = func(message)
            if reply != None and reply != "":
                await message.channel.send(reply)
        return on_message
    return reply_to_self_impl

def reply_to_all(client):
    def reply_to_all_impl(func):
        @client.event
        async def on_message(message):
            if message.author == client.user:
                return
            if message.channel.name != 'kanaal-voor-bots':
                return
            reply = func(message)
            if reply != None and reply != "":
                await message.channel.send(reply)
        return on_message
    return reply_to_all_impl


def upside_down(message):
    result = ''
    for letter in message:
        if letter in ud_letters:
            result += ud_letters[letter]
        else:
            result += letter
    return result[::-1]