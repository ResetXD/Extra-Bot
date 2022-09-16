import nextcord
import os
from nextcord.ext import commands

import lib.values as v

prefix=v.values.getData("prefix")
configData=v.values.getData("tokendetails")

token = os.getenv('BOTTOKEN')

intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True
intents.typing = False
intents.presences = False
client = commands.Bot(command_prefix=prefix, intents=intents, help_command=None, case_insensitive=True)


# useful code
@client.event
async def on_ready():
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="/help"))
    print("The Bot Is Up And Running")
    print("-------------------------")


# Cogs
innitial_extensions = []

for i in os.listdir("cogs"):
    if i.endswith(".py"):
        innitial_extensions.append("cogs." + i[:-3])

if __name__ == "__main__":
    for extension in innitial_extensions:
        client.load_extension(extension)

client.run(token)  # runs the bot
