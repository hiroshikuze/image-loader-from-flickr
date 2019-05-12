# Flickrからキーワード指定された画像を指定された場所へ格納する
# 最初に pip install flickrapi が必要

from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
import glob
import json

key = "<<Your flickr API key>>"
secret = "<<Your flickr secret>>"
wait_time = 1
keyword = "<<Search Keyword>>"
savedir = "<<Save Folder>>"
getImageCount = 1000

# FlickrAPIにアクセス

page = 1
files = glob.glob((savedir + '/*.jpg').replace('//', '/'))
nowImageCount = len(files)

while nowImageCount < getImageCount:
    flickr = FlickrAPI(key, secret, format='parsed-json')
    result = flickr.photos.search(
        text = keyword,
        per_page = 500,
        page = page,
        media = 'photos',
        sort = 'relevance',
        safe_search = 1,
        license = '1,2,3,4,5,6',
        extras = 'url_l,owner_name'
    )
    photos = result['photos']
    for i, photo in enumerate(photos['photo']):
        try:
            url_q = photo['url_l']
        except:
            continue
        filepath = savedir + '/' + photo['id'] + '.jpg'
        if os.path.exists(filepath): continue
        try:
            urlretrieve(url_q, filepath)
        except:
            continue

        # save JSON
        filepath = savedir + '/' + photo['id'] + '.json'
        json_data = {}
        json_data['id'] = photo['id']
        json_data['owner'] = photo['owner']
        json_data['ownername'] = photo['ownername']
        json_data['title'] = photo['title']
        f = open(filepath,'w')
        json.dump(json_data,f)
        f.close()

        line = str(i) + ' ' + photo['id'] + ' ' + photo['owner'] + ' ' + photo['ownername'] + ' ' + photo['title']
        print(line)

        nowImageCount += 1
        if getImageCount <= nowImageCount:
            break

        time.sleep(wait_time)

    page += 1