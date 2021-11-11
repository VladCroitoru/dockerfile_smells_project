#
# Unofficial alpine-rvm Dockerfile 
#
# https://github.com/nicdoye/alpine-rvm
#

# Pull base image
FROM nicdoye/alpine-rvm-gcc

RUN apk update && \
    apk upgrade

# Delete all the cruft used to build alpine-rvm-gcc 
# Don't delete bash - that stays the shell of the rvm user
# procps stays too, just to stop the shell moaning so much
RUN apk del gcc gnupg curl ruby musl-dev make linux-headers && \
    rm -rf /var/cache/apk/*
