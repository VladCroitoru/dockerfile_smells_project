#
# my mini base image
#
#

FROM  alpine:latest

MAINTAINER Gunnar Falk <docker@grundstil.de>
# inspired by https://github.com/colstrom/docker-alpine 

## Taken directly form https://github.com/colstrom/docker-alpine:
# This includes the main, testing, and community repositories,
# but all packages outside main are masked. 
# To import them, just use apk add package@tag.
##

RUN echo http://dl-cdn.alpinelinux.org/alpine/latest-stable/main | tee /etc/apk/repositories \
  && echo http://dl-cdn.alpinelinux.org/alpine/latest-stable/community | tee -a /etc/apk/repositories
  
RUN apk --no-cache add \
curl \
wget \
bash \
tree \
sed \
rsync \
openssh \
vim \
nano \
ca-certificates \
sudo \
screen \
busybox-suid \
build-base 

