# https://github.com/Rapptz/discord.py/blob/async/examples/reply.py
import discord
import json

with open('secret.json') as secret_json:
    creds = json.load(secret_json)

TOKEN = creds["oauth"]["token"]

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content == 'yo' and message.author.id == '288370172744695809':
        msg = '{0.author.mention} yo'.format(message)
        await client.send_message(message.channel, msg)
        msg = '{0.author.mention} What time we playing?'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)