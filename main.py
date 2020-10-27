# bot.py
import os
import random

# Adds the main discord api functions
from keep_alive import keep_alive
from discord.ext import commands
from dotenv import load_dotenv
import discord
keep_alive()
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bot Command Prefix
bot = commands.Bot(command_prefix='>')

init_extensions = ['cogs.general',
                   'cogs.messaging', 
                   'cogs.admins', 
                   'cogs.games', 
                   'cogs.useful']

if __name__ == '__main__':
    for extension in init_extensions:
        bot.load_extension(extension)



#Informs user if incorrect role
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')








# Final line
bot.run(TOKEN)
