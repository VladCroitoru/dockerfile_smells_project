FROM ubuntu:xenial
MAINTAINER Nutthaphon Suwanwong

RUN (mv /etc/localtime /etc/localtime.old; ln -s /usr/share/zoneinfo/Asia/Bangkok /etc/localtime)

RUN apt-get update && apt-get install -y \
	python-pip \
	python-dev \
	build-essential \
	libssl-dev \
	libffi-dev

RUN pip install --upgrade pip && pip install scrapy

RUN scrapy startproject tutorial

COPY quotes_spider.py tutorial/tutorial/spiders

RUN scrapy crawl quotes