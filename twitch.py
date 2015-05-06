import requests, json

def twitch(user):
	url = "https://api.twitch.tv/kraken/channels/" + user
	data = requests.get(url)
	user_info = json.loads(data.text)
	if user_info['status'] == 404:
		return "Twitch user does not exist."
	else:
		return user_info['display_name'] + " playing " + user_info['game'] + " http://twitch.tv/" + user_info['display_name']
