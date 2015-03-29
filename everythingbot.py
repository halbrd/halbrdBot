## TO DO
#  qhelp
#  finish reminder + add to help documentation
#       fix parse error message


import Skype4Py
import time
import re
import datetime
import sqlite3
from time import mktime
from multiprocessing import Process

class SkypeBot(object):

    _msgRet = ""
    _msgHelp = "Everything Bot command list:   (required field)   [optional field]\n"
    _msgHelp += "!help - Returns list of available commands\n"
    _msgHelp += "!ping - Pong!\n"
    _msgHelp += "!members - Returns a list of the full names of all members in the chat\n"
    _msgHelp += "!profile (skypename) - Returns various information about the specified Skype user (must be in chat)\n"
    _reminders = []

    #Command functions
    def help(self):
        self._msgRet += self._msgHelp

    def ping(self):
        self._msgRet += "Pong!"

    def members(self, members):
        for member in members:
            self._msgRet += member.FullName + ", "
        self._msgRet = self._msgRet[:-2]

        return self._msgRet

    def profile(self, skypeName, activemembers):
        found = False

        for member in activemembers:
            if member.Handle == skypeName:
                found = True
                # The multiple commands is just to break the long string of concatenation up into multiple lines
                self._msgRet += "Profile of " + member.Handle
                self._msgRet += "\nFull name: " + member.FullName
                self._msgRet += "\nSex: " + member.Sex
                self._msgRet += "\nMood text: " + member.RichMoodText
                self._msgRet += "\nBio: " + member.About
                self._msgRet += "\nCurrently " + member.OnlineStatus
                if member.OnlineStatus == "OFFLINE":
                    self._msgRet += "\nLast online: " + str(member.LastOnline)
                self._msgRet += "\nBirthday: " + str(member.Birthday)
                self._msgRet += "\nCountry: " + member.Country
                self._msgRet += "\nCity: " + member.City
                self._msgRet += "\nLanguage: " + member.Language
                #self._msgRet += "\nTimezone: " + str(member.Timezone)
                self._msgRet += "\nWebsite: " + member.Homepage

        if not found:
            self._msgRet += "Profile not found."

    # NEVER allow this command to become common knowledge!
    def orangecrush(self):
        self._msgRet = "!orangecrush"

    def remind(self, dt, text):
        now = datetime.datetime.now()
        now = now.replace(second=0, microsecond=0)

        dt = datetime.datetime.fromtimestamp(mktime(dt))

        if dt <= now:
            self._msgRet = "Reminder trigger datetime must be in the future."
        else:
            while not dt == now:
                time.sleep(60)
                now = datetime.datetime.now()
                now = now.replace(second=0, microsecond=0)

            self._msgRet = "Reminder! [" + text + "]"

    ###################################################################################

    # Some weird shit Skype4Py does to instantiate listeners
    def __init__(self):
        self.skype = Skype4Py.Skype(Events=self)
        self.skype.FriendlyName = "Jack"   # Not sure if this is actually doing anything
        self.skype.Attach()   # This is the part that actually connects the script to your account
       
    # This part is powered by magic
    def MessageStatus(self, msg, status):
        if status == Skype4Py.cmsReceived or status == Skype4Py.cmsSent:
            # I have no idea what this line does other than it makes the bot respond to its own messages, and it only works in private chat
            # if msg.Chat.Type in (Skype4Py.chatTypeDialog, Skype4Py.chatTypeLegacyDialog):
            if msg.Body[0] == "!":
                # !help command
                # Returns list of commands
                if re.match("!help", msg.Body):
                    self.help()

                # !ping command
                # Returns "Pong!"
                elif re.match("!ping", msg.Body):
                    self.ping()

                # !members command
                # Returns list of members in the convo
                elif re.match("!members", msg.Body):
                    self.members(msg.Chat.Members)

                # !profile (n) command
                # Looks up member n and returns a bunch of info about them
                elif re.match("!profile ", msg.Body):
                    skypeName = msg.Body[9:]
                    self.profile(skypeName, msg.Chat.Members)

                # !orangecrush command
                # Recurses infinitely - keep this secret!
                elif re.match("!orangecrush", msg.Body):
                    self.orangecrush()

                # !remind (n) command
                # Sets a reminder
                elif re.match("!remind ", msg.Body):
                    #self._msgRet += "Unable to parse !remind command. Please refer to !help for assistance."

                    inDT = msg.Body[8:24]
                    text = msg.Body[25:]
                    # author = message sender?

                    dto = time.strptime(inDT, '%Y-%m-%d %H:%M')
                    p = Process(target=self.remind, args=(dto, text,))
                    p.start()
                    p.join()
                    #self.remind(dto, text)

                # Prints the finished message
                if self._msgRet == "":
                    self._msgRet += "Unknown command. Type !help for a list of commands."

                msg.Chat.SendMessage(self._msgRet)
                self._msgRet = ""
 
print 'Activating bot...'
bot = SkypeBot()
print 'Bot activated.'
 
# Run forever
while True:
    time.sleep(1)
