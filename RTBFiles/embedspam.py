import discord
import sys
import random
import aiohttp

token = sys.argv[1]
title = sys.argv[2]
author = sys.argv[3]
iconurl = sys.argv[4]
thumburl = sys.argv[5]
footer = sys.argv[6]
textchan = sys.argv[7]
useproxies = sys.argv[8]

if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    proxy = random.choice(proxy_list)
    con = aiohttp.ProxyConnector(proxy="http://"+proxy)
    client = discord.Client(connector=con)
else:
    client = discord.Client()

# set embed
embed=discord.Embed(title=title)
embed.set_author(name=author, icon_url=iconurl)
embed.set_thumbnail(url=thumburl)
embed.set_footer(text=footer)

@client.event
async def on_ready():
    try:
        txtchan = client.get_channel(int(textchan))
        while True:
            await txtchan.send(embed=embed)
    except Exception:
        pass
try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
