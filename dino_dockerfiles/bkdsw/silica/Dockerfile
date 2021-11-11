# Get Golang
FROM golang:alpine

# Maintainer of the File
MAINTAINER Kayle Gishen <k@bkdsw.com>

RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories

RUN apk update
RUN apk add openjdk8-jre nodejs git yarn gzip
RUN apk add brotli@edge

# Download silica
RUN yarn global add silica
