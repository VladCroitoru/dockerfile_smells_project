FROM alpine:3.3
MAINTAINER Hans Höchtl <hhoechtl@1drop.de>
RUN apk add --update py-sphinx py-sphinx_rtd_theme && rm -rf /var/cache/apk/*

RUN mkdir documents

WORKDIR /documents
VOLUME /documents
