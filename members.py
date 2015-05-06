import Skype4Py

def members(members):
    ret = ""
    for member in members:
        ret += member.FullName + ", "
    ret = ret[:-2]
    return ret
