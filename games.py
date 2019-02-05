import random
from discord.ext import commands

class Games():
    def __init__(self, client):
        self.client = client

    @commands.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers a yes/no question",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
    async def eight_ball(self, context):
        possible_responses = [
        "That is a No-No",
        "Can't happen",
        "Sorry broke down while thinking",
        "yeah it's true for me",
        "yes, like yeah fucking yeah",
        "uhmm i don't know much about it",
        ]
        await self.client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


def setup(client):
    client.add_cog(Games(client))