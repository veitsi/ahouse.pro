"""this module checked with python 3.5 and uses only standart  python library
it processes csv file sample.csv and estimates when current user joined facebook
"""
import urllib.request
import json


def first_post_date(token):
    if token == '':
        raise ValueError("token cannot be empty")
    offset = 0
    baseurl = "https://graph.facebook.com/v2.8/me/feed?access_token=" + token
    while True:
        url = baseurl + "&offset=" + str(offset)
        rez = urllib.request.urlopen(url).read().decode('utf8')
        rez = json.loads(rez)
        l = len(rez["data"])
        if l > 0:
            date = rez["data"][l - 1]["created_time"][:10]
            offset += 20
        else:
            break
    return date


if __name__ == '__main__':
    fi = open("sample.csv", "r")
    fo = open("output.csv", "w")
    for s in fi.readlines():
        data = s.split(",")
        # as facebook doesn't provide joining date in direct way,
        # we estimate this date as users first post date
        d = first_post_date(data[1])
        out = data[2].strip() + "," + data[0] + "," + d + "\n"
        fo.write(out)


    fi.close()
    fo.close()
