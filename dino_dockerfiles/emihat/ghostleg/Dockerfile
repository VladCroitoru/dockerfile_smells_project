FROM alpine:3.2

MAINTAINER emihat <hattori.emi@imsbio.co.jp>

RUN apk add --update perl && rm -rf /var/cache/apk/*

COPY ghostleg.pl /

ENTRYPOINT ["/usr/bin/perl", "/ghostleg.pl"]
