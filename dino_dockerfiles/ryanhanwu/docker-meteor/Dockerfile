FROM node:latest

MAINTAINER Ryan Wu "hello@ryanwu.me"

RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get install --no-install-recommends -y -q curl python build-essential git ca-certificates

RUN curl https://install.meteor.com/ | sh
