FROM ubuntu:latest
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
RUN apt-get update && apt-get -y upgrade \
    && apt-get -y install python \
    && apt-get -y install python-dev \
    && apt-get -y install python-argparse \
    && apt-get clean \
    && mkdir /version \
    && rm -r /var/lib/apt/lists/*
ADD get_version.py /version/
ADD ioutil.py /version/
ENV PATH $PATH:/version
