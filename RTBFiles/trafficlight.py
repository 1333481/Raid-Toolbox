import discord
import asyncio
import random
import sys
import aiohttp

useproxies = sys.argv[2]
if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()
token = sys.argv[1]


@client.event
async def on_ready():
    while not client.is_closed():
        randoms = ['1','2','3']
        presence = (random.choice(randoms))
        if presence == '1':
            await client.change_presence(status=discord.Status.online)
            await asyncio.sleep(3)
        elif presence == '2':
            await client.change_presence(status=discord.Status.idle)
            await asyncio.sleep(3)
        elif presence == '3':
            await client.change_presence(status=discord.Status.do_not_disturb)
            await asyncio.sleep(3)
try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
