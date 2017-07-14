import discord
import re
from random import randint

# Kaz Bishop
# Apache License
# https://github.com/EvilLogic/Dice-Bot

client = discord.Client()

def roll(dice):
    print(dice)
    # list all matching dice operations
    oplist = re.findall("[0-9]+[d\+\-\*\/][0-9]+", dice)
    while len(oplist) >= 1:
        op = oplist[0]
        numsum = 0
        
        if 'd' in op:
            for i in range(0,int(op[0:op.find('d')])):
                numsum += randint(1, int(op[op.find('d')+1:]))
        if '+' in op or '-' in op or '*' in op or '/' in op:
            numsum = eval(op)
        
        # set dice to new num and recreate oplist
        dice = dice.replace(op, str(numsum), 1)
        print(dice)
        oplist = re.findall("[0-9]+[d\+\-\*\/][0-9]+", dice)
    return dice

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    # or to reply in a different channel
    # alpha should make the text ignored
    if (message.channel.name != 'rolz' or
    message.author == client.user or
    message.content[0].isalpha()):
        return

    if message.content == '1datlantis':
        msg = 'https://goo.gl/JDdsav'.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content == '3d8wolves':
        msg = 'https://goo.gl/ixkXuL'.format(message)
        for wolf in range(3, 24):
            await client.send_message(message.channel, msg)
        return

    # make a list of dice
    dice = message.content.split(' ')
    for d in dice:
        d = roll(d)
        msg = '{0.author.mention} '.format(message) + str(d)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('INSERTBOTTOKENHERE')
