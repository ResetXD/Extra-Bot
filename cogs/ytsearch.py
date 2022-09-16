import nextcord
from nextcord.ext import commands
import lib.values as v

guilds=v.values.getData("guilds")
embedColor=v.values.getData("color")

class YTSearch(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Youtube Search Command
    @nextcord.slash_command(guild_ids=guilds, description="Youtube Search Command")
    async def ytsearch(self, interaction:nextcord.Interaction, query: str = nextcord.SlashOption(description="Query", required=True)):
        ytEmbed = nextcord.Embed(
            title=query,
            color=embedColor,
            description=f"Click The Text Above To Got To Your Youtube Search",
            url=f"https://www.youtube.com/results?search_query={query}"
        )
        ytEmbed.set_thumbnail("https://cdn.discordapp.com/attachments/991958269012758548/1003381079832543363/youtube.png")
        await interaction.response.defer()
        await interaction.followup.send(embed=ytEmbed)

# Setup
def setup(client):
    client.add_cog(YTSearch(client))
