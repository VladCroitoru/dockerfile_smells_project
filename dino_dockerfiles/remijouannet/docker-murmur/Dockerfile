FROM alpine:3.3
MAINTAINER Rémi Jouannet remijouannet@gmail.com

ENV version=1.2.14

ENV PORT 64738
ENV PASSWORD changeme
ENV BANDWITH 72000

WORKDIR /app

RUN apk update && apk upgrade

ADD http://mumble.info/snapshot/murmur-static_x86-${version}.tar.bz2 /app/

RUN tar xjf /app/murmur-static_x86-${version}.tar.bz2
RUN mv /app/murmur-static_x86-${version}/murmur.x86 /app/
RUN adduser -h /app -s /bin/false murmur -D -H
RUN chown murmur:murmur /app 

COPY . /app/

CMD ["sh", "/app/run.sh"]
