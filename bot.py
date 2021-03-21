# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} popped her pussy into the server!')
    print('Bot ID:{}'.format(client.user.id))

bot = commands.Bot(command_prefix='$')
@bot.command()
async def say(ctx, message=None):
    await ctx.send(message)


bot.run(TOKEN)
client.run(TOKEN)

