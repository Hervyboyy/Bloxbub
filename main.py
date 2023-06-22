import random
from _ast import List
from discord.ext import commands, tasks
from itertools import cycle
import discord
from discord.ext import commands


client = commands.Bot(command_prefix="!" , intents=discord.Intents.all())

@client.event
async def on_ready():
    print("Sucess Bot is connected to Discord ")


@client.command()
async def magic_eightball(ctx, *, question):
    with open("../respones.txt", "r") as f:
        random_response: List[str] = f.readlines()
        response: object = random.choice(random_response)

        await ctx.send(response)


bot_status = cycle({"Type !help for commands", "BETA BOT", "Timezone EST", "Have a good day!"})

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready():
    print("Success: Bot is connected to Discord")
    change_status.start()


async def load():
   for filename in os.listdir("./cogs"):
       if filename.endswith(".py"):
           await client.load_extension(f"cogs.{filename[:-3]}")


           async def main():
               async with client:
                   await load()
                   await client.start("")

asyncio.run(main{})


client.run("")
