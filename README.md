# ProgImageService

[![Build Status](https://travis-ci.org/msoufiane/ProgImageService.svg?branch=master)](https://travis-ci.org/msoufiane/ProgImageService)
[![Coverage Status](https://coveralls.io/repos/github/msoufiane/ProgImageService/badge.svg?branch=master)](https://coveralls.io/github/msoufiane/ProgImageService?branch=master)

ProgImageService is an image storage and processing service for ProgImage.com
____

## Features
ProgImageService provides an API to store, retrieve and convert images.
1. Image storage:
    * Url: `/image`
    * method: `POST`
    * param: `image`
    * param type: image file (see supported files in Notes section)
2. Image retrieval:
    * Url: `/image/{id}`
    * method: `GET
2. Image conversion:
    * Url: `/image/{id}.{extention}`
    * method: `GET

## Instalation
* Install using `pip`...

`pip install -r requirements.txt`

make sure the required services are running (edit the [local configuration file](https://github.com/msoufiane/ProgImageService/blob/master/ProgImageService/settings/local.py) if necessary)
* Using docker

build: `docker-compose build`
run: `docker-compose up -d`
check logs: `docker-compose logs -f`

## Notes:
### Supported files:
|File Extention| MIME Type              |
| ------------ |:----------------------:|
|.bmp          |image/bmp               |
|.gif          |image/gif               |
|.ico          |image/vnd.microsoft.icon|
|.jpg          |image/jpeg              |
|.jpeg         |image/jpeg              |
|.png          |image/png               |
|.svg          |image/svg+xml           |
|.tiff         |image/tiff              |
|.webp         |image/webp              |

## Links:
### External Services
|Service|Description|
|----|----|
|[CompressionService]()|A service for compressing images|
|[RotationService]()|A service for rotating images|
|[FiltersService]()|A service for applying filters to images|
|[ThumbnailService]()|A service for creating thumbnails from images|
|[MaskService]()|A service for applying masks to images|



### SDKs
* [ProgImage go SDK]()