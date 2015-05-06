#import Skype4Py

def profile(skypeName, members):
    found = False
    for member in members:
        if member.Handle == skypeName:
            found = True
                
            ret = """Profile of """ + member.Handle + """
            Full name: """ + member.FullName + """
            Sex: """ + member.Sex + """
            Mood text: """ + member.RichMoodText + """
            Bio: """ + member.About + """
            Currently """ + member.OnlineStatus + "\n"
            if member.OnlineStatus == "OFFLINE":
                ret += "Last online: " + str(member.LastOnline)
            ret += """Birthday: """ + str(member.Birthday) + """
            Country: """ + member.Country + """
            City: """ + member.City + """
            Language: """ + member.Language + """
            Website: """ + member.Homepage

    if not found:
        ret = "Profile not found."
    return ret
