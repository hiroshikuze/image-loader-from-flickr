# image-loader-from-flickr
Download a large amount of images little by little for the keywords specified from the [flickerAPI](https://www.flickr.com/services/api/).

## Setup

1. Install flickrapi

```shell
pip install flickrapi
```

2. Edit at the begining og the source code.

```python
#example
key = "12345678901234567890123456789012"
secret = "abcdefghijklmnop"
wait_time = 1
keyword = "hogehoge"
savedir = "./images"
getImageCount = 1000
```

## Usage

```shell
python ImageLoaderFromFlickr.py
```

## LICENCE

MIT License.
