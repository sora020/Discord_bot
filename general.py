import discord
from discord.ext import commands

class General():
    def __init__(self, client):
        self.client = client
    
    @commands.command(name="ping",
                description="pongs back",
                brief="pongs back",
                pass_context=True)
    async def ping(self, context):
        await self.client.say(":ping_pong: pong!!")
    

    @commands.command(pass_context=True)
    async def joined_at(self, context, member: discord.Member = None):
        if member is None:
            member = context.message.author

        await self.client.say('{0} joined at {0.joined_at}'.format(member))



    @commands.command(pass_context=True)
    async def info(self, context, user: discord.Member = None):
        if user is None:
            user = context.message.author
        await self.client.say(("```\nusername: {0}\n"
        "user ID: {0.id}\n"
        "user status: {0.status}\n"
        "highest role: {0.top_role}\n"
        "joined at: {0.joined_at}```").format(user))


def setup(client):
    client.add_cog(General(client))