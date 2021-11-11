FROM node:8-alpine

MAINTAINER Mike Leo "mike@foundplaces.com"

RUN apk -Uuv add --no-cache bash git openssh

RUN npm install --global lerna

RUN \
	mkdir -p /aws && \
	apk -Uuv add groff less python py-pip && \
	pip install awscli && \
	apk --purge -v del py-pip && \
	rm /var/cache/apk/*
