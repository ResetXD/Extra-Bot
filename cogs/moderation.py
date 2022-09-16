import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
import lib.values as v
from datetime import timedelta

guilds=v.values.getData("guilds")
embedColor=v.values.getData("color")

# can be placed in better place?
def time_to_seconds(time):
    time = time.lower()
    if time.endswith("s"):
        return int(time[:-1])
    elif time.endswith("m"):
        return int(time[:-1]) * 60
    elif time.endswith("h"):
        return int(time[:-1]) * 3600
    elif time.endswith("d"):
        return int(time[:-1]) * 86400
    else:
        return int(time)

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
@@ -15,7 +29,10 @@ def __init__(self, client):
    @nextcord.slash_command(guild_ids=guilds, description="Kick The Specified Member")
    @has_permissions(kick_members=True)
    async def kick(self, interaction: nextcord.Interaction, member: nextcord.Member, *, reason: str = nextcord.SlashOption(description="The Reason You Want To Kick The Member", required=True)):
        try:
            await member.send(f"You Got Kick From The Server \nReason:{reason}")
        except:
            pass
        await member.kick(reason=reason)
        await interaction.response.defer()
        await interaction.followup.send(f"Kicked {member}\nReason:{reason}")
@@ -29,16 +46,36 @@ async def kick_error(self, ctx, error):
    @nextcord.slash_command(guild_ids=guilds, description="Ban Sepcified Member")
    @has_permissions(ban_members=True)
    async def ban(self, interaction: nextcord.Interaction, member: nextcord.Member, *, reason: str = nextcord.SlashOption(description="The Reason You Want To Ban The Member", required=True)):
        try:
            await member.send(f"You Got Ban From The Server \nReason:{reason}")
        except:
            pass
        await member.ban(reason=reason)
        await interaction.response.defer()
        await interaction.followup.send(f"Banned {member}\nReason:{reason}")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("You Don't Have The Permissions To Ban !")


    @nextcord.slash_command(guild_ids=guilds, description="Timeout Sepcified Member")
    @has_permissions(moderate_members=True)
    async def timeout(self, interaction: nextcord.Interaction, member: nextcord.Member, time:str = nextcord.SlashOption(description="Time Limit (s/m/h/d)", required=True), *, reason: str = nextcord.SlashOption(description="The Reason You Want To Timeout The Member", required=True)):
        await interaction.response.defer()
        try:
            await member.send(f"You Are In Timeout\nReason:{reason}")
        except:
            pass
        await member.timeout(timedelta(seconds=time_to_seconds(time)), reason=reason)
        await interaction.followup.send(f"{member} is in Timeout\nReason:{reason}")

    @timeout.error
    async def timeout_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.reply("You Don't Have The Permissions To Timeout !")

# Setup
def setup(client):
    client.add_cog(Moderation(client))