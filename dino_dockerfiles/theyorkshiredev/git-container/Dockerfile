#
# Container with Git installed
#
# (c) 2018 - Steven Cooney
########################################################

FROM alpine:3.7

RUN apk update --no-cache && rm -rf /var/cache/apk/*
RUN apk add --no-cache git && rm -rf /var/cache/apk/*
