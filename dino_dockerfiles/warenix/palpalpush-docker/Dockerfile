FROM ubuntu:15.10
MAINTAINER warenix <warenix@gmail.com>

RUN apt-get update

# python 2.7
RUN apt-get install -y ca-certificates python2.7 python-setuptools
RUN easy_install pip

# app dependency
RUN apt-get install -y python-tweepy

ADD files/root /root
WORKDIR /root/app
CMD ["sh", "/root/entrypoint.sh"]

