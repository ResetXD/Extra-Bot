import nextcord
from nextcord.ext import commands
from mojang import MojangAPI
import lib.values as v

guilds=v.values.getData("guilds")
embedColor=v.values.getData("color")
channel=v.values.getData("wlc_chnl")

class Minecraft(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Command
    @nextcord.slash_command(guild_ids=guilds, description="Check If A Minecraft Name Is Availble Or Not")
    async def checkmcname(self, interaction:nextcord.Interaction, name: str = nextcord.SlashOption(description="The Name Of The Minecraft Player You Want To Check", required=True)):
        player = MojangAPI.get_uuid(name)

        if not player:
            McEmbed = nextcord.Embed(title=name, description=f"The Minecraft Name {name} Is Availbe", color=embedColor)
            await interaction.response.defer()
            await interaction.followup.send(embed=McEmbed)

        elif " " in name == True:
            await interaction.response.defer()
            await interaction.followup.send("The Requested Name Contains an invalid character")

        else:
            McEmbed = nextcord.Embed(title=name, description=f"The Minecraft Name {name} Is Unvailbe", color=embedColor)
            await interaction.response.defer()
            await interaction.followup.send(embed=McEmbed)
        

# Setup
def setup(client):
    client.add_cog(Minecraft(client))