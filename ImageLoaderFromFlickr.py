# Flickrからキーワード指定された画像を指定された場所へ格納する
# 最初に pip install flickrapi が必要

from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys
import glob
import json

with open('config.json','r',encoding='utf-8') as f:
    config = json.load(f)

# FlickrAPIにアクセス

page = 1
files = glob.glob((config['savedir'] + '/*.jpg').replace('//', '/'))
nowImageCount = len(files)

while nowImageCount < config['getImageCount']:
    flickr = FlickrAPI(config['key'], config['secret'], format='parsed-json')
    result = flickr.photos.search(
        text = config['keyword'],
        per_page = 500,
        page = page,
        media = 'photos',
        sort = 'relevance',
        safe_search = 1,
        license = config['api_license'],
        extras = config['api_extras']
    )
    photos = result['photos']
    for i, photo in enumerate(photos['photo']):
        try:
            url_q = photo['url_l']
        except:
            continue
        filepath = config['savedir'] + '/' + photo['id'] + '.jpg'
        if os.path.exists(filepath): continue
        try:
            urlretrieve(url_q, filepath)
        except:
            continue

        # save JSON
        filepath = config['savedir'] + '/' + photo['id'] + '.json'
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
        if config['getImageCount'] <= nowImageCount:
            break

        time.sleep(config['wait_time'])

    page += 1