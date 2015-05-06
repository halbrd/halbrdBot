lennyFile = open("res/lenny.txt")
_lenny = lennyFile.read()
lennyFile.close()

tableflipFile = open("res/tableflip.txt")
_tableflip = tableflipFile.read()
tableflipFile.close()

tablesetFile = open("res/tableset.txt")
_tableset = tablesetFile.read()
tablesetFile.close()

helpText = """Everything Bot command list:   (required field)   [optional field]
!help - Returns list of available commands
!ping - Pong!
!members - Returns a list of the full names of all members in the chat
!profile (skypename) - Returns various information about the specified Skype user (must be in chat)
!lenny - """ + _lenny + """
!fc - Returns list of friend codes for the members of the 3DS convo
!gostats (username) - Returns link to csgo-stats.com page for username
!tableflip - """ + _tableflip + """
!tableset - """ + _tableset + """
!coinflip - Returns heads or tails randomly
!nt (URL) - Prevents automatic page title retrieval
!twitch (channel) - Returns link to specified Twitch channel
!hug [name] - Personally hug the specified person
!bothug [name] - Get the bot to do your hugging for you
!lwc - Literally Who Cares. For when the salt is flying hard and fast."""

def help():
    return helpText
