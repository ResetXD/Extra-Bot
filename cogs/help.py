import nextcord
from nextcord.ext import commands
import lib.values as v

guilds=v.values.getData("guilds")
embedColor=v.values.getData("color")

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Help command
    @nextcord.slash_command(guild_ids=guilds, description="Help Command")
    async def help(self, interaction: nextcord.Interaction):
        embed = nextcord.Embed(
            title="Commands",
            color=embedColor
        )
        embed.add_field(name="Music", value="-play [url] - Plays the audio from the spicified url\n-stop - Stops the currently playing audio")
        embed.add_field(name="Moderation",value="/kick [member] - Kicks the specified member\n/ban - Bans the specified member")
        embed.add_field(name="Misc", value="/ytsearch [Query] - Search Youtube For Something\n/gsearch [Query] - Search Google For Something\n/myid - Sends You Your Discord ID\n/getid [member] - Get Some Data About a Spicific member\n/checkmcname [name] - Checks If A Minecraft Name Is Availbe\n/help - Display This Message")
        embed.add_field(name="Fun", value="/yesorno [Question] - Ask the bot a question")
        await interaction.response.defer()
        await interaction.followup.send(embed=embed)


# setup
def setup(client):
    client.add_cog(Help(client))
