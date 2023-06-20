import nextcord
import config
import os
from nextcord.ext import commands

Intents = nextcord.Intents.all()
Intents.members = True

bot = commands.Bot(command_prefix='/'),

@bot.event
async def on_ready():
    print('Logged in as {bot.user.name} ({bot.user.id})')
    print(_______________________________________________)















    bot.run(config.TOKEN)


