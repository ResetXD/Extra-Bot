import nextcord
from nextcord.ext import commands

class help(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    #Help command
    @commands.command()
    async def help(self,message):
        embed = nextcord.Embed(title="Commands" ,color=0x2852fa,description="-help - Display This Message \n-kick [Member] [Reason] - Kick A Spesific Member \n-spam [Message] [Number] - Spam A Spesific Message A Number Of Times \n-ytSearch [Query] - Search On Youtube For Query \n-gSearch [Quers] - Search On Google For Query \n-Myid - Tell You Your Id \n-Lyrics [Artist] [Song] - Search For A Song's Lyrics By Artist")
        await message.author.send(embed=embed)

#setup
def setup(client):
    client.add_cog(help(client))