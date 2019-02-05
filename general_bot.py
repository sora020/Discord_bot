import discord
from discord.ext import commands

class Bot():
    def __init__(self,client):
        self.client = client

    @commands.command(pass_context=True)
    async def kick(self,context,user: discord.Member):
        await self.client.say(":boot: kicked {}.".format(user.name))
        await self.client.kick(user)
        
def setup(client):
    client.add_cog(Bot(client))