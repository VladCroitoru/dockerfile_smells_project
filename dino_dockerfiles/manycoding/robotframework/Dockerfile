FROM openjdk:jre-alpine
MAINTAINER Valery M. <vamukhs@gmail.com>

RUN apk add --update --no-cache \
    python \
    python-dev \
    py-pip

RUN pip install -U \
    pip \
    robotframework==3.0.2 \
    robotframework-selenium2library==1.8.0 \
    selenium==2.53.6 \
    robotframework-ftplibrary
