FROM fanningert/baseimage-alpine

MAINTAINER fanningert <thomas@fanninger.at>

RUN apk update && \
	apk add --no-cache --update bash && \
	apk add --no-cache --update aria2

RUN apk --update add \
  ca-certificates \
  ruby \
  ruby-bundler \
  ruby-xmlrpc \
  ruby-dev && \
  rm -fr /usr/share/ri

ADD root/ /

RUN chmod -v +x /etc/services.d/*/run /etc/cont-init.d/*

VOLUME ["/download"]
VOLUME ["/conf"]
EXPOSE 6800
