FROM alpine:3.6
MAINTAINER Stephen Oliver <steve@infincia.com>

RUN apk --no-cache add znc

RUN adduser irc -D -H

RUN mkdir /etc/irc
RUN chown irc:irc /etc/irc

VOLUME /etc/irc


EXPOSE 7000
EXPOSE 6667
EXPOSE 8080
CMD su -c 'znc --foreground --datadir=/etc/irc' irc
