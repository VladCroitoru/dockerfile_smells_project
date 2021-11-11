#
# Alpine image with NPM and Node installed
#
# (c) 2018 - Steven Cooney
########################################################

FROM alpine:3.7

RUN apk add --update --no-cache nodejs nodejs-npm && rm -rf /var/cache/apk/* && npm install npm@latest -g
