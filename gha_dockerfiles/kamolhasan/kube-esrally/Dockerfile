FROM python:3.8.11-alpine
#FROM python:3.6.14-alpine

RUN apk add --update --no-cache git build-base linux-headers  python3-dev libffi-dev openjdk8

RUN python3 -m pip install esrally==2.2.1
RUN python3 -m pip install urllib3==1.24.3

COPY rally.ini /root/.rally/