from ping import ping
from help import help
from members import members
from profile import profile
from friendcodes import friendcodes
from coinflip import coinflip
from url_get import url_get
from removebot import removebot
from restartbot import restartbot
from requestfunction import requestfunction
from hug import hug
from bothug import bothug
from twitch import twitch
#from blacklist import blacklist
from strats import strats

import Skype4Py
import time
import re
from datetime import datetime
from time import mktime
import string
import random
import urllib2
import hashlib
import sys
import os
import csv
import pickle



class SkypeBot(object):

    ### Initialize program data ###
    lennyFile = open("res/lenny.txt")
    _lenny = lennyFile.read()
    lennyFile.close()

    tableflipFile = open("res/tableflip.txt")
    _tableflip = tableflipFile.read()
    tableflipFile.close()

    tablesetFile = open("res/tableset.txt")
    _tableset = tablesetFile.read()
    tablesetFile.close()

    # get admins
    admins = []
    with open("res/admins.txt", 'rb') as f:
        admins = pickle.load(f)
        f.close()
    
    # get blacklist
    #blacklist = []
    #with open("res/blacklist.txt", 'rb') as f:
    #    blacklist = pickle.load(f)
    #    f.close()

    ############################# Program body #############################

    # Some weird shit Skype4Py does to instantiate listeners
    def __init__(self):
        self.skype = Skype4Py.Skype(Events=self)
        self.skype.FriendlyName = "Jack"   # Not sure if this is actually doing anything
        self.skype.Attach()   # This is the part that actually connects the script to your account
       
    # This part is powered by magic
    def MessageStatus(self, msg, status):
        if status == Skype4Py.cmsReceived or status == Skype4Py.cmsSent:
            # I have no idea what this line does other than it makes the bot respond to its own messages, and it only works in private chat
            #if not msg.Sender.Handle in self.blacklist:
            if msg.Body[0] == "!" and msg.Sender.Handle != "everythingbot":
                print "[" + str(datetime.now())[:-7] + "] " + msg.Sender.Handle + ": " + msg.Body

            # !help
            if re.match("!help(?!\S)", msg.Body):
                msg.Chat.SendMessage(help())

            # !ping
            elif re.match("!ping(?!\S)", msg.Body):
                msg.Chat.SendMessage(ping())

            # !members
            elif re.match("!members(?!\S)", msg.Body):
                msg.Chat.SendMessage(members(msg.Chat.Members))

            # !profile
            elif re.match("!profile(?!\S)", msg.Body):
                try:
                    skypeName = msg.Body[9:]
                    msg.Chat.SendMessage(profile(skypeName, msg.Chat.Members))
                except IndexError:
                    msg.Chat.SendMessage("Skype username required for profile lookup.")

            # !orangecrush
            # If you're reading this on the Github repo, congratulations on being the first to figure out that it's been public all along.
            elif re.match("!orangecrush(?!\S)", msg.Body):
                msg.Chat.SendMessage("!orangecrush")

            # !lenny
            elif re.match("!lenny(?!\S)", msg.Body):
                msg.Chat.SendMessage(self._lenny)

            # !friendcodes
            elif re.match("!friendcodes(?!\S)", msg.Body) or re.match("!fc(?!\S)", msg.Body):
                msg.Chat.SendMessage(friendcodes())

            # !gostats
            elif re.match("!gostats(?!\S)", msg.Body):
                msg.Chat.SendMessage("http://csgo-stats.com/" + msg.Body[9:])

            # !tableflip
            elif re.match("!tableflip(?!\S)", msg.Body):
                msg.Chat.SendMessage(self._tableflip)

            # !tableset
            elif re.match("!tableset(?!\S)", msg.Body):
                msg.Chat.SendMessage(self._tableset)

            # !coinflip
            elif re.match("!coinflip(?!\S)", msg.Body):
                msg.Chat.SendMessage(coinflip())

            # URL titles

            # This is the opt-into title code.
            #elif re.match("!title(?!\S)", msg.Body):
            #    if re.match('!title http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', msg.Body, re.IGNORECASE):
            #        url = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', msg.Body, re.IGNORECASE)
            #        msg.Chat.SendMessage(url_get(url.group(0)))
            #    else:
            #        msg.Chat.SendMessage("Invalid URL.")

            # This is the opt-out of title code.
            elif re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', msg.Body, re.IGNORECASE) and not re.search("!nt(?!\S)", msg.Body) and msg.Sender.Handle != "everythingbot":
                url = re.search('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', msg.Body, re.IGNORECASE)
                msg.Chat.SendMessage(url_get(url.group(0)))

            # !removebot
            elif re.match("!removebot(?!\S)", msg.Body):
                if removebot(msg.Sender.Handle):
                    msg.Chat.Leave()

            # !restartbot
            elif re.match("!restartbot(?!\S)", msg.Body):
                if removebot(msg.Sender.Handle):
                    msg.Chat.SendMessage("Restarting bot.")
                    execfile("~halbrdbot.py")
                    sys.exit()

            # !twitch (channel)
            # !gostats
            elif re.match("!twitch(?!\S)", msg.Body):
               # msg.Chat.SendMessage("http://twitch.tv/" + msg.Body[8:])
                msg.Chat.SendMessage(twitch(msg.Body[8:]))

            # !requestfunction (string)
            #elif re.match("!requestfunction(?!\S)", msg.Body):
            #    msg.Chat.SendMessage(requestfunction(msg.Sender.Handle, msg.Body[17:]))

            #elif msg.Body == "!chatname":
            #    msg.Chat.SendMessage(msg.Chat.Name)

            # !hug
            elif re.match("!hug(?!\S)", msg.Body) and msg.Sender.Handle != "everythingbot":
                msg.Chat.SendMessage(hug(msg.Sender.FullName, msg.Body[5:]))

            # !bothug
            elif re.match("!bothug(?!\S)", msg.Body):
                msg.Chat.SendMessage(bothug(msg.Body[8:]))

            # !blacklist
            #elif re.match("!blacklist(?!\S)", msg.Body):
            #    msg.Chat.SendMessage(blacklist(msg.Sender.Handle, msg.Body[11:]))

            # !strats
            elif re.match("!strats(?!\S)", msg.Body):
                msg.Chat.SendMessage(strats(msg.Body[8:]))

            # !lwc
            elif re.match("!lwc(?!\S)", msg.Body):
                msg.Chat.SendMessage("Literally who cares.\nhttp://lynq.me/lwc.mp4")





            # lmao
            # Keep this as the last thing that gets checked
            elif re.search("l+ *m+ *a+ *o+", msg.Body, re.IGNORECASE) and msg.Sender.Handle != "everythingbot":
                msg.Chat.SendMessage("ayyy")

print 'Activating bot...'
bot = SkypeBot()
print 'Bot activated.'

# Run forever
while True:
    time.sleep(0.5)
