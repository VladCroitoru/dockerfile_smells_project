FROM python:2.7-alpine
MAINTAINER Craig Tracey <craigtracey@gmail.com>

WORKDIR /usr/src/flotilla
RUN apk update && apk add git
COPY . ./
RUN pip install -r requirements.txt
RUN python setup.py install
