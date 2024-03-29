# image-loader-from-flickr
Download a large amount of images and owner jsonfile little by little for the keywords specified from the [flickerAPI](https://www.flickr.com/services/api/).

## Setup

1. Install flickrapi

```shell
pip install flickrapi
```

2. Edit at 'config.json'.

```json
{
    "key" : "12345678901234567890123456789012",
    "secret" : "abcdefghijklmnop",
    "wait_time" : 1,
    "keyword" : "hogehoge",
    "savedir" : "./images",
    "getImageCount" : 1000,
    "api_license" : "1,2,3,4,5,6",
    "api_extras" : "url_l,owner_name"
}
```

## Usage

```shell
python ImageLoaderFromFlickr.py
```

## Contribution

1. Fork it ( http://github.com/hiroshikuze/image-loader-from-flickr/fork )
2. Create your feature branch (git checkout -b my-new-feature)
3. Commit your changes (git commit -am 'Add some feature')
4. Push to the branch (git push origin my-new-feature)
5. Create new Pull Request

## LICENCE

MIT License.

## Author

[hiroshikuze](https://github.com/hiroshikuze)

## Donation

[Author's wish list by Amazon(Japanese)](https://www.amazon.jp/hz/wishlist/ls/5BAWD0LZ89V9?ref_=wl_share)
