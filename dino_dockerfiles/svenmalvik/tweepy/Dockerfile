FROM python:3.5

RUN mkdir -p /usr/src/app

COPY follow.py /usr/src/app/
COPY unfollow.py /usr/src/app/

WORKDIR /usr/src/app

RUN pip install tweepy
