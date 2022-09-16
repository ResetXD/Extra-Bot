import nextcord
from nextcord.ext import commands
import lib.values as v

guilds=v.values.getData("guilds")
embedColor=v.values.getData("color")

class GetID(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Get ID Command Self Explanatory
    @nextcord.slash_command(guild_ids=guilds, description="Get The Id Of A Specific Member")
    async def getid(self, interaction: nextcord.Interaction, member: nextcord.Member):
        IdEmbed = nextcord.Embed(
            title=f"{member._user}'s Id",
            color=embedColor,
            description=f"The Id Of {member._user} is {member.id}")
        IdEmbed.set_thumbnail(member.avatar.url)
        await interaction.response.defer()
        await interaction.followup.send(embed=IdEmbed)

# Setup
def setup(client):
    client.add_cog(GetID(client))
