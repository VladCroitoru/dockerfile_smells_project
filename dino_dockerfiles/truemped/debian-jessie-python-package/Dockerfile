FROM debian:jessie
MAINTAINER Daniel Truemper truemped@gmail.com

RUN DEBIAN_FRONTEND=noninteractive                                   \
    mkdir -p /var/cache/apt/archives                                 \
    apt-get clean && apt-get update && apt-get upgrade  &&           \
    apt-get install --yes debhelper dh-virtualenv python python-dev  \
            libxml2-dev libcurl4-openssl-dev libssl-dev libxslt1-dev \
            python-pgmagick libtiff5-dev libpng12-dev libjpeg-dev    \
            libjasper-dev libwebp-dev python-setuptools lsb-release  \
            devscripts python-pip python-gevent libevent-dev &&      \
    pip install -U pip && \
    pip install -U setuptools
