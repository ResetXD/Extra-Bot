import nextcord
from nextcord.ext import commands
import lib.values as v

guilds=v.values.getData("guilds")
embedColor=v.values.getData("color")

class MyID(commands.Cog):
    def __init__(self, client):
        self.client = client

        # Tell you your discord id useful in some cases

    @nextcord.slash_command(guild_ids=guilds, description="Tell You Your Id In Discord")
    async def myid(self, interaction: nextcord.Interaction):
        await interaction.response.defer()
        await interaction.followup.send(f"{interaction.user.id} Is Your Id")


# Setup
def setup(client):
    client.add_cog(MyID(client))
