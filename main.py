from discord.ext.commands import Bot
import os
from keep_online import keep_online
from host_address import get_Host_name_IP
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

startup_extensions = ["general", "games","general_bot"] 

BOT_PREFIX = "?a"
token = os.environ.get("TOKEN")
client = Bot(command_prefix=BOT_PREFIX)
 

@client.event
async def on_ready():
    print("--------\nOnline")
    print('logged in as: {} \nBot Id is: {}\n--------'.format(client.user,client.user.id))


@client.command()
async def load(extension_name : str):
    """Loads an extension."""
    try:
        client.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await client.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await client.say("{} loaded.".format(extension_name))


@client.command()
async def unload(extension_name : str):
    """Unloads an extension."""
    client.unload_extension(extension_name)
    await client.say("{} unloaded.".format(extension_name))

@client.event
async def on_message( message):
    if message.author == client.user:
        return
    if message.content.startswith('?hi'):
        msg = "Hello {0.author.mention}".format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('?bot'):
        await client.send_message(message.channel, "Yes")
    await client.process_commands(message)


get_Host_name_IP()
keep_online()


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    client.run(token)