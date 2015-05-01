## TO DO
#  qhelp
#  finish reminder + add to help documentation
#       fix parse error message
# 		probably create reminder class and instantiate for each reminder
# clean up !profile results
# !meme
# print notification of method call to console
# read/write friendcodes as normal lines in file
# Write logs to console and to file with start and end datetime on KeyboardInterrupt
# !add [skypename]
# !removebot - bot leaves chat if FromHandle = william-holt
# Leave chat or disable functions if william-holt is not in it


import Skype4Py
import time
import re
import datetime
from time import mktime
from multiprocessing import Process
import string
import random
import urllib2
import hashlib
import sys
import csv



class SkypeBot(object):

    ### Initialize program data ###
    lennyFile = open("lenny.txt")
    _lenny = lennyFile.read()
    lennyFile.close()

    tableflipFile = open("tableflip.txt")
    _tableflip = tableflipFile.read()
    tableflipFile.close()

    tablesetFile = open("tableset.txt")
    _tableset = tablesetFile.read()
    tablesetFile.close()

    # Return message
    _msgRet = ""

    # !help message
    _msgHelp = "Everything Bot command list:   (required field)   [optional field]\n"
    _msgHelp += "!help - Returns list of available commands\n"
    _msgHelp += "!ping - Pong!\n"
    _msgHelp += "!members - Returns a list of the full names of all members in the chat\n"
    _msgHelp += "!profile (skypename) - Returns various information about the specified Skype user (must be in chat)\n"
    _msgHelp += "!lenny - " + _lenny + "\n"
    _msgHelp += "!fc - Returns list of friend codes for the members of the 3DS convo\n"
    _msgHelp += "!gostats (username) - Returns link to csgo-stats.com page for username\n"
    _msgHelp += "!tableflip - " + _tableflip + "\n"
    _msgHelp += "!tableset - " + _tableset + "\n"
    _msgHelp += "!coinflip - Returns heads or tails randomly\n"

    # Friendcode database
    _fc = []

    # Load friendcodes
    with open("fcdb.csv", "rb") as f:
        fcreader = csv.reader(f)
        for row in fcreader:
            _fc.append(row)
        f.close()
    #print _fc



    ### Command functions ###
    def help(self):
        self._msgRet = self._msgHelp

    def ping(self):
        self._msgRet = "Pong!"

    def members(self, members):
        for member in members:
            self._msgRet = member.FullName + ", "
        self._msgRet = self._msgRet[:-2]

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
            self._msgRet = "Profile not found."

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


    # Old, disgusting, brute force !meme code
    
    def meme(self, string_length):
        print "Running meme()"
        CHARS = string.ascii_letters+string.digits # Characters used for random URLs.
        STRING_LENGTH = string_length
        ERRORS_DISPLAY = True # Should all errors display?
        IMAGE_EXTENSION = ".png" # Extension for search.
        IMAGE_SIZE_MIN = 1024 * 20 # Minimum filesize for downloaded images.
        IMAGES_DEFAULT = 1 # Number of images to download if not specified at command line.
        IMGUR_URL_PREFIX = "http://i.imgur.com/" # Prefix for Imgur URLs.

        rand_string = ''.join([random.choice(CHARS) for x in range(STRING_LENGTH)])

        print "Variables initialized. Starting loop"

        end = False
        while not end:
            image_name = rand_string + IMAGE_EXTENSION
            url = IMGUR_URL_PREFIX+image_name
            print "Requesting"
            req = urllib2.Request(url)
            #data = None
            print "Setting data"
            data = urllib2.urlopen(req)

            if data:
                print "Reading data"
                data = data.read()
                if 'd835884373f4d6c8f24742ceabe74946' == hashlib.md5(data).hexdigest():
                    self._msgRet = "Received placeholder image: "+image_name
                elif IMAGE_SIZE_MIN > sys.getsizeof(data):
                    self._msgRet = "Received image is below minimum size threshold: "+image_name
                else:
                    end = True
                    self._msgRet = url
    

    # New, futuristic, attractive, Imgur API code
    # lol

    def lenny(self):
        self._msgRet = self._lenny

    def stayinalive(self):
        time.sleep(0.577)
        self._msgRet = "!stayinalive"

    def istheeverythingbotback(self):
        self._msgRet = "No."

    def fc(self):
        for i in range(0, len(self._fc), 2):
            self._msgRet += self._fc[i][0] + ": " + self._fc[i+1][0] + "\n"

    def gostats(self, user):
        self._msgRet = "http://csgo-stats.com/" + user

    def tableflip(self):
        self._msgRet = self._tableflip

    def tableset(self):
        self._msgRet = self._tableset

    def coinflip(self):
        random.seed()
        if random.random() < 0.5:
            retString = "Heads"
        else:
            retString = "Tails"
        self._msgRet = retString

    def lmao(self):
        self._msgRet = "ayyy"

    ### Program body ###

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
            #if msg.Body[0] == "!":   # this used to be a thing but it was changed since it was superfluous and I needed the "lmao" command

            # !help command
            # Returns list of commands
            if re.match("!help", msg.Body):
                self.help()

            # !ping command
            # Returns "Pong!"
            elif msg.Body == "!ping" or re.match("!ping ", msg.Body):
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

            #elif msg.Body == "!meme":
            #    self.meme(5)
            #elif msg.Body == "!meme7":
            #    self.meme(7)

            #elif msg.Body == "!lenny" or re.match("!lenny ", msg.Body):
            #    self.lenny()

            elif msg.Body == "!edit":
                msg.Body = "Edited!"

            elif msg.Body == "!lenny" or re.match("!lenny ", msg.Body):
                self.lenny()

            #elif msg.Body == "!stayinalive" or re.match("!stayinalive ", msg.Body):
            #    self.stayinalive()

            elif msg.Body == "!istheeverythingbotback":
                self.istheeverythingbotback()

            elif re.match("!friendcodes ", msg.Body) or msg.Body == "!friendcodes" or re.match("!fc ", msg.Body) or msg.Body == "!fc":
                self.fc()

            elif msg.Body == "!gostats" or msg.Body == "!gostats ":
                self._msgRet = "Invalid username."
            elif re.match("!gostats ", msg.Body):
                self.gostats(msg.Body[9:])

            elif msg.Body == "!tableflip" or re.match("!tableflip ", msg.Body):
                self.tableflip()

            elif msg.Body == "!tableset" or re.match("!tableset ", msg.Body):
                self.tableset()

            elif msg.Body == "!coinflip" or re.match("!coinflip ", msg.Body):
                self.coinflip()

            elif re.search("l+ *m+ *a+ *o+", msg.Body, re.IGNORECASE):
                self.lmao()




            #####################

            # Prints the finished message
            #if self._msgRet == "":
            #    self._msgRet += "Unknown command. Type !help for a list of commands."

            if not self._msgRet == "":
                msg.Chat.SendMessage(self._msgRet)
            self._msgRet = ""
 
print 'Activating bot...'
bot = SkypeBot()
print 'Bot activated.'

# Run forever
while True:
    time.sleep(1)
