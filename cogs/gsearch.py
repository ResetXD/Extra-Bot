import nextcord
from nextcord.ext import commands


class GoogleSearch(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Google Search Command
    @nextcord.slash_command(guild_ids=[977477205573652518], description="Google Search Command")
    async def gsearch(self, interaction:nextcord.Interaction, query: str = nextcord.SlashOption(description="Query", required=True)):
        gEmbed = nextcord.Embed(
            title=query,
            description=f"Click The Text Above To Go To Your Google Search",
            url=f"https://www.google.com/search?query={query}",
            color=0x2852fa,
        )
        gEmbed.set_thumbnail("https://cdn.discordapp.com/attachments/991958269012758548/1003379889069641758/google.png")
        await interaction.response.send_message(embed=gEmbed)

# Setup
def setup(client):
    client.add_cog(GoogleSearch(client))
