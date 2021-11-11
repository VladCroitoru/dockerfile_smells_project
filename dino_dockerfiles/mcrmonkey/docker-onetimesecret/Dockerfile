# Dockerfile for One-Time Secret http://onetimesecret.com

FROM alpine:latest as PKGGET
RUN apk --no-cache add zip

ADD https://github.com/onetimesecret/onetimesecret/archive/refs/heads/main.zip /tmp/onetime.zip

RUN /usr/bin/unzip /tmp/onetime.zip -d /extract/



FROM ruby:2.6-alpine

LABEL MAINTAINER ant <git@manchestermonkey.co.uk>

COPY --from=PKGGET /extract/* /var/lib/onetime/

WORKDIR /var/lib/onetime

RUN adduser ots -h /var/lib/onetime -D && \
	mkdir -p /var/log/onetime /var/run/onetime /etc/onetime && \
	chown ots /var/log/onetime /var/run/onetime /var/lib/onetime /etc/onetime && \
	cp -R etc/* /etc/onetime/ && \
	chown ots: /var/lib/onetime/* -R


RUN apk --no-cache --virtual .build-deps add build-base && \
    bundle update && \
	bundle install --frozen --deployment --without=dev && \
	bin/ots init && \
	apk del .build-deps

ADD config/config /etc/onetime/config
ADD config/fortunes /etc/onetime/fortunes

EXPOSE 7143

ENTRYPOINT ["su", "ots", "-c", "bundle exec thin -e dev -R config.ru -p 7143 start"]
