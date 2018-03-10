import discord.game
from discord import Game
import discord
import requests
import asyncio
import json
import cat
from discord.ext.commands import Bot

BOT_PREFIX = ("?", "!")

TOKEN = "NDIwMjQxNDgyMjM1MTE3NTk4.DX70fQ.wOSpU15CjHpQObM__qS6xbpH0Mg"

client = Bot (command_prefix=BOT_PREFIX)

from random import *

@client.command(name ="xkcd",
brief="Generates webcomic from xkcd.com")
async def suggestion():
    xkcd_numb = randint(1,1964)
    comic_id = ("https://xkcd.com/" + str(xkcd_numb) + "/")
    await client.say(comic_id)

import random
@client.command(name="8ball",
                description="Answers a yes/no question. To properly use put the trigger in front of the question. Trigger Words:",
                brief="Rolls an 🎱.",
                aliases=["eight_ball", "8", "8Ball", "Eight Ball", "Eight ball", "Magic 8 Ball", "magic 8 ball", "Magic 8 ball", "magic 8 Ball", "eight Ball", "🎱"],
pass_context=True)
async def eight_ball(context):
    possible_responses = [
    "That is a resounding no!",
    "It is not likely",
    "Fat chance!",
    "It is likely",
    "Most definitely!"
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name="dice",
                description="Rolls a 🎱. To properly use put the trigger in front of the question. Trigger Words:",
                brief="Rolls a 🎲.",
                aliases=["Dice", "🎲"],
pass_context=True)
async def Dice(context):
    possible_responses = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6"
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name="coinflip",
                description="Flips a coin. To properly use put the trigger in front of the question. Trigger Words:",
                brief="Flips a coin.",
                aliases=["coin", "Coin", "coinFlip", "Coinflip"],
pass_context=True)
async def Dice(context):
    possible_responses = [
    "Heads",
    "Tails"
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

@client.command(name="catgen",
                description="Generates a picture of a cat. To properly use put the trigger in front of the question. Trigger Words:",
                brief="Cat pics.",
                aliases=["cat", "Cat", "catpic", "Cat Picture"],
pass_context=True)
async def catgen():
    getCat()
    url = 'getCat()'
    await client.say(url))


@client.command(name = "icon",
brief="(Broken)")
async def icon():
    server_icon_url = str(Server. icon_url)
    await client.say(server_icon_url)


@client.command(
pass_context=True,
brief="Squares a number"
)
async def square(context , number):
    squared_value = int(number) * int(number)
    await client.say(str(number) + " squared is " + str(squared_value) + "," + context.message.author.mention + ".")

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="Development"))
    print("Logged in as " + client.user.name)

@client.command(
pass_context=True,
description="Generates the price of bitcoin in USD$. To properly use put the trigger in front of the question. Trigger Words:",
brief="Bitcoin price ($)",)
async def bitcoin(context):
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    response = requests.get(url)
    value = response.json()['bpi']['USD']['rate']
    await client.say("Bitcoin price is: $" + value + " in USD, " +  context.message.author.mention + ".")


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current Server(s):")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(36000)



client.loop.create_task(list_servers())
client.run(TOKEN)
