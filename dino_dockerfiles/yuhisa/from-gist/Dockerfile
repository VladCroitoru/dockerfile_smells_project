FROM alpine:3.4

MAINTAINER "yuhisa-jp"

ENV GISTURL="yuhisa-jp/4cbcd6dc79570c55f6d948a82dbfca91"

RUN apk update && apk add curl && rm -rf /var/cache/apk/*

COPY start.sh /tmp/start.sh
RUN chmod +x /tmp/start.sh

ENTRYPOINT ["/tmp/start.sh"]
