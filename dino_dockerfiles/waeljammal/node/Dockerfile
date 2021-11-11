# Start from base node alpine image
FROM node:6.10.2-alpine

# update packages
RUN apk update

# install imagemagick
RUN apk add --no-cache imagemagick

# install bash for wercker
RUN apk add --no-cache bash

# install deps for phantom
RUN apk add --no-cache curl && curl -Ls "https://github.com/dustinblackman/phantomized/releases/download/2.1.1/dockerized-phantomjs.tar.gz" | tar xz -C /

# try fix
RUN ln -s /bin/sh /bin/source

ENTRYPOINT ["/bin/sh", "-c"]