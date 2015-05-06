import urllib
import urlparse
import requests
import json
from BeautifulSoup import BeautifulSoup



def urlget(url):
    if "youtube.com" in url:
        url_data = urlparse.urlparse(url)
        query = urlparse.parse_qs(url_data.query)
        video = query["v"][0] # video_id
        new_url = "https://gdata.youtube.com/feeds/api/videos/" + video +  "?v=2&alt=jsonc"
        response = urllib.urlopen(new_url)
        data = json.loads(response.read())
        return "[Title] " + data['data']['title'] + " [" + str(int(data['data']['duration'])/60) + "." + str(int(data['data']['duration']) % 60) + " minutes]"
    else:
        resp = requests.get(url)
        data = resp.text
        soup = BeautifulSoup(data)
        return "[Title] " + soup.title.string
