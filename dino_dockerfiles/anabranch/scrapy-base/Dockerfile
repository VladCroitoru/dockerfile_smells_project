FROM ubuntu:14.04

MAINTAINER Bill Chambers, http://billchambers.me

ENV DEBIAN_FRONTEND noninteractive

# Install packages
RUN apt-get -y update && apt-get install -y wget nano locales curl unzip wget openssl gcc libxml2-dev libxslt1-dev python-dev libffi-dev libssl-dev
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8

RUN locale-gen en_US.UTF-8
RUN dpkg-reconfigure locales

RUN echo "America/Los_Angeles" > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python get-pip.py
RUN pip install lxml Scrapy

