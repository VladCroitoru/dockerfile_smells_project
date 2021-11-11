# Dockerfile for yunojuno/heroku
#
# Read setup.sh for a better rundown.
# 
# Images get tagged with the Python major version:
#
#    e.g yunojuno/heroku:3.9-latest

FROM heroku/heroku:20

LABEL maintainer "YunoJuno <code@yunojuno.com>"

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

COPY setup.sh /tmp/setup.sh

RUN /tmp/setup.sh
