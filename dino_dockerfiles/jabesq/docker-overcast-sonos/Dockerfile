# Use an official Python runtime as a base image
FROM python:2.7-slim
MAINTAINER Hugo Dupras <jabesq@gmail.com>

EXPOSE 8140

WORKDIR /code

RUN apt-get update && apt-get install -y --no-install-recommends\
 git \
 libxml2-dev\
 libxslt-dev\
 python-dev \
 zlib1g-dev \
 build-essential \
&& apt-get clean && rm -rf /var/lib/apt/lists/*

RUN git clone -n https://github.com/jacobian/overcast-sonos.git
WORKDIR overcast-sonos
RUN git checkout master

RUN pip install -r requirements.txt

ENV OVERCAST_USERNAME=you@there.com
ENV OVERCAST_PASSWORD=1234 

ENTRYPOINT python overcast-sonos.py
