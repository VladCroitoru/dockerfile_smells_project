# This dockerfile uses the ubuntu image
# VERSION 1 - EDITION 1
# Author: KingMario

FROM ubuntu

MAINTAINER KingMario <gcyyq@hotmail.com>

# Commands to build the env
RUN apt-get update && apt-get install -y python python-pip libjpeg-dev libfreetype6 python-dev python-setuptools zlib1g-dev curl && apt-get clean && pip install pillow && mkdir ~/mapCut && mkdir ~/mapCut/precut && mkdir ~/mapCut/result && curl https://raw.githubusercontent.com/KingMario/Baidu-Map-Indoor-Lite/master/mapCut.py -o ~/mapCut/mapCut.py && chmod +x ~/mapCut/mapCut.py

# Commands when creating a new container
ENTRYPOINT /bin/bash