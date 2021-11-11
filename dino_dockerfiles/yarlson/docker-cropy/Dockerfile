# Version: 0.0.1
FROM ubuntu:14.04
MAINTAINER Yar Kravtsov <yarlson@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install build-essential libfreetype6-dev libjpeg-dev liblcms1-dev libpq-dev python-dev python-scipy python-setuptools python2.7-dev uwsgi uwsgi-plugin-python zlib1g-dev -y
RUN apt-get build-dep python-numpy cython python-scipy -y

RUN ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
RUN ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
RUN ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/
RUN ln -s /usr/include/freetype2 /usr/local/include/freetype

RUN easy_install pip

RUN pip install PIL --allow-external PIL --allow-unverified PIL
RUN pip install scikit-image cropy

ENV DEBIAN_FRONTEND newt
