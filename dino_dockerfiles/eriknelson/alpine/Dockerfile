FROM gliderlabs/alpine:3.1

RUN apk update && apk upgrade
RUN apk add bash

# Vim for maintenance
RUN apk add vim
ADD vimrc /root/.vimrc
