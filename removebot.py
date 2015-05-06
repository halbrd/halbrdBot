import pickle

admins = []
with open("res/admins.txt", 'rb') as f:
    admins = pickle.load(f)
    f.close()

def removebot(senderHandle):
    if senderHandle in admins:
        return True
    else:
        return False
