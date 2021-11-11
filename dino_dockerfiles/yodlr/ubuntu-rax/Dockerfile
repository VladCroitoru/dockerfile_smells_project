FROM ubuntu:14.04
MAINTAINER Ross Kukulinski "ross@getyodlr.com"

ENV LAST_UPDATED 3_19__2015

RUN apt-get -qq update && \
  apt-get -yqq install apt-transport-https

ADD sources.list /etc/apt/

RUN apt-get -qq update && apt-get -yqq upgrade
