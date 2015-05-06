def requestfunction(sender, request):
    if request and not "\n" in request:
        with open("res/functionrequests.txt", "a") as requests:
            requests.write("\n" + sender + ": " + request)
            requests.close()
        return "Request submitted."
    else:
        return "Invalid request."
