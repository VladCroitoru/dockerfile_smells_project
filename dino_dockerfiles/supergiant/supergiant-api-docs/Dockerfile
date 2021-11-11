FROM ubuntu:14.04
MAINTAINER Qbox Inc.

RUN apt-get update
RUN apt-get install -y curl build-essential
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs

EXPOSE 8080

ADD . supergiant-api-docs

WORKDIR supergiant-api-docs

RUN npm install

CMD node .
