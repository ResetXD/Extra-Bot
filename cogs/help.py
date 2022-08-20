import nextcord
from nextcord.ext import commands
from configparser import ConfigParser

config=ConfigParser()
config.read(".\config.ini")
guild_id_1=config["options"]["guild1_id"]
guild_id_2=config["options"]["guild2_id"]
guilds=[int(guild_id_1),int(guild_id_2)]

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Help command
    @nextcord.slash_command(guild_ids=guilds, description="Help Command")
    async def help(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title="Commands",
            color=0x2852fa,
            description=f"-Help - Display This Message \n-Ban [Member] [Reason] - Ban A Spesific Member From The Server \n-Kick [Member] [Reason] - Kick A Spesific Member\n-YtSearch [Query] - Search On Youtube For Query \n-GSearch [Query] - Search On Google For Query \n-Myid - Tell You Your Id \n-YesOrNo [Question] - Ask The Bot A Question \n-CheckMcName [Name] - Check If A Minecraft Name Is Availbe Or Not \n-GetId [Member] - Get The Id Of A Member And Send It\n-Play [Song Url] - Play The Song From The Youtube Url\n-Stop - Stop The Song That's Currently Playing"
        )
        await interaction.response.defer()
        await interaction.followup.send(embed=embed)


# setup
def setup(client):
    client.add_cog(Help(client))
