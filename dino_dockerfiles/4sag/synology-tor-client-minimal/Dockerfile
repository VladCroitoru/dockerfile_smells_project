FROM alpine:latest

MAINTAINER 4saG <4sag@bk.ru>

ENV TIMEZONE  Asia/Yekaterinburg

RUN apk update && apk upgrade && apk add bash python curl tzdata tor
RUN cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && echo "${TIMEZONE}" > /etc/timezone && apk del tzdata

EXPOSE 9150

RUN rm /var/cache/apk/*

ADD ./torrc /etc/tor/torrc

USER tor
CMD /usr/bin/tor -f /etc/tor/torrc
