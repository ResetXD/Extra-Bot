#Very Baisic Api
class values():
    def getData(value):
        guild1_id=1009880989318791289
        guild2_id=850066291225133068
        guilds=[guild1_id, guild2_id]

        welcome_channel = 1009880989796933754
        welcome_message = "WELCOME TO OUR TESTING SERVER THIS SERVER WAS MADE FOR TESTING THE BOT"
        server_name = "Testing Server"

        embedColor=0x2852fa
        prefix="-"

        if value.lower() == "guilds":
            return guilds
        elif value.lower() == "color":
            return embedColor
        elif value.lower() == "prefix":
            return prefix
        elif value.lower() == "wlc_chnl":
            return welcome_channel
        elif value.lower() == "guild_name":
            return server_name
        elif value.lower() == "wlc_message":
            return welcome_message