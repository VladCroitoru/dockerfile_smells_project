FROM ubuntu:16.04
MAINTAINER Yukimitsu Yabuki, yukimitsu.yabuki@gmail.com
RUN apt-get update && apt-get -y upgrade \
    && apt-get -y install mercurial \
    && apt-get -y install make \
    && apt-get -y install g++ \
    && apt-get -y install python-pip \
    && apt-get -y install zlib1g-dev \
    && pip install --upgrade pip \
    && pip install biopython \
    && hg clone http://last.cbrc.jp/last/ \
    && cd last \
    && make \
    && make install \
    && apt-get clean \
    && rm -r /var/lib/apt/lists/*
WORKDIR /last
ADD maf-convert.py /last/
