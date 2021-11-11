#
# Monera-static-transformer
#
# VERSION                1.0.1

FROM node
MAINTAINER Mauro Mandracchia <info@ideabile.com>
LABEL Description="Get a static content (.md, .sass, .js, etc..) and create a static website." Vendor="ideabile.com" Version="1.0.1"
VOLUME ["/dest", "/content"]

ENV WWW=/dest
ENV MAIN=./

WORKDIR /
ADD ${MAIN}package.json /package.json
RUN npm install
ADD $MAIN /
RUN apt-get clean

ENTRYPOINT /node_modules/.bin/gulp
