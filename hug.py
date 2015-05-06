def hug(sender, subject):
    if subject:
        return sender + " hugs " + subject
    else:
        return "In the absence of anyone to hug, " + sender + " hugs themself."
