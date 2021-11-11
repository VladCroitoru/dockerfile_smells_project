FROM alpine:3.4
MAINTAINER Florian Holzapfel <flo.holzapfel@gmail.com>
RUN apk add --update py-pip py-docutils py-sphinx py-sphinx_rtd_theme && rm -rf /var/cache/apk/*
RUN pip install imagesize recommonmark
