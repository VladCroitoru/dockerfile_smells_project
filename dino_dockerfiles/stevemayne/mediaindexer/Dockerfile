FROM alpine:latest
MAINTAINER Steve Mayne <steve.mayne@gmail.com>

RUN apk add --no-cache python gettext bash && rm -rf /var/cache/apk/*

ENV BASE_URL http://invalid.com/

COPY rawfiles /rawfiles

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

VOLUME /media

ENTRYPOINT ["/entrypoint.sh"]
CMD crond -l 2 -f
