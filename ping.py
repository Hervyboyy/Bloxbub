import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

        @commands.Cog.listner()
        async def on_ready(self):
            print("Ping.py Is ready!")

            @commands.command()
            async def ping(ctx):
             bot_latency = round(client.latency * 1000)

             await ctx.send(f"Pong! {bot_latency} ms.")

             async def setup(client):
                await client.add_cog(Ping{client})

                async def main():
                   async with client:
                      await load()
                      await client.start("")

                      
