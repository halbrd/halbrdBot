import urllib2
import urllib
import urlparse
import requests
import json
from collections import namedtuple
from BeautifulSoup import BeautifulSoup



def urlget(url):
    if "youtube.com" in url:
        url_data = urlparse.urlparse(url)
        query = urlparse.parse_qs(url_data.query)
        video = query["v"][0]
        new_url = "https://www.googleapis.com/youtube/v3/videos?id=" + video + "&key=AIzaSyD860e0YpYvAtiFGbLavC4_tyhhpAHTq_M&part=contentDetails,snippet"
        response = urllib.urlopen(new_url)
        data = json.loads(response.read())
        title = data['items'][0]['snippet']['title']
        description = data['items'][0]['snippet']['description'][:100] + "..."
        duration = data['items'][0]['contentDetails']['duration']
        duration = duration[2:-1].split("M")
        
        return "[Title] " + title + " [" + duration[0] + " min " + duration[1] + "s]\n[Description] " + description
    else:
        resp = requests.get(url)
        data = resp.text
        soup = BeautifulSoup(data)
        return "[Title] " + soup.title.string
