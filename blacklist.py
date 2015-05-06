import re
import pickle

admins = []
with open("res/admins.txt", 'rb') as f:
    admins = pickle.load(f)
    f.close()

blacklist = []
with open("res/blacklist.txt", 'rb') as f:
    blacklist = pickle.load(f)
    f.close()

def blacklist(sender, arguments):
    ret = ""
    if sender in admins:
        if re.match("(add|del|lst) [a-zA-Z0-9]+", arguments):
            cmd = arguments[0:3]
            target = arguments[4:]

            if cmd == "add":
                blacklist.append(target)
                ret = target + " added to blacklist."
            elif cmd == "del":
                blacklist.remove(target)
                ret = target + " removed from the blacklist."
            elif cmd == "lst":
                ret = str(blacklist)
        else:
            ret = "Incorrectly formatted command."
    else:
        ret = "!blacklist requires admin rights."
    
    with open("res/blacklist.txt", 'wb') as f:
        pickle.dump(blacklist, f)
    
    return ret
