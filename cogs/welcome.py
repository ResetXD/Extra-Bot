import nextcord
from nextcord.ext import commands
import lib.values as v

guilds=v.values.getData("guilds")
embedColor=v.values.getData("color")
channel_var=v.values.getData("wlc_chnl")
welcome_message=v.values.getData("wlc_message")
server_name=v.values.getData("guild_name")

class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Command
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(channel_var)
        embed = nextcord.Embed(title=f"Hello Welcome To {server_name}",description=welcome_message)
        await member.send(embed = embed)
        await channel.send(f"Welcome To The Server, <@{member.id}>")
# Setup
def setup(client):
    client.add_cog(Welcome(client))
