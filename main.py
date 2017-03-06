import facebook
import urllib.request
import json
url="https://graph.facebook.com/v2.8/me/feed?access_token="

f = open("sample.csv", "r")
for s in f.readlines():
    data = s.split(",")
    print(url+data[1])
    rez=urllib.request.urlopen(url+data[1]).read().decode('utf8')
    rez=json.loads(rez)
    print(rez["data"][0]["created_time"][:10])
    break