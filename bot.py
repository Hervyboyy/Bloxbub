import discord
from discord.ext import commands



client = commands.Bot(command_prefix="!" , intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Sucess Bot is connected to Discord ")

async def load():
   for filename in os.listdir("./cogs"):
       if filename.endswith(".py"):
           await client.load_extension(f"cogs.{filename[:-3]}")


           async def main():
               async with client:
                   await load()
                   await client.start("MTEyMTIyMDg3ODk4MjcyMTYzNg.GbRovN.jEgU6bcvVaHvL62r0lqnMJAMoLq58lspXg9KFY")




client.run("")
