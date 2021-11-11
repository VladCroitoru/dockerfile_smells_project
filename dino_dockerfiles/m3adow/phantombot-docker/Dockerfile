FROM openjdk:8-jre-alpine

COPY ./start-phantombot.sh /
COPY ./botlogin.txt /

RUN apk add --no-cache bash curl \
  && mkdir -p /data \
  && chmod +x /start-phantombot.sh \
  && sync \
  && /start-phantombot.sh dontrun

EXPOSE 25000 25001 25002 25003 25004 25005

VOLUME ["/data"]

ENTRYPOINT ["/start-phantombot.sh"]
