#
# Docker image for OpenWhisk ThumbnailAction
#

FROM node:alpine
MAINTAINER Shaun Murakami (stmuraka@us.ibm.com)

# Add edge and test repositories
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories \
 && echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

# Install prereq packages
RUN apk update \
 && apk add build-base \
            libwebp-dev@edge \
            fftw-dev@edge \
            vips-dev@testing

# Install Application in root dir
RUN mkdir -p /root/server/src
COPY server/ /root/server/
WORKDIR /root/server
RUN npm install .

EXPOSE 8080
CMD node ./app.js
