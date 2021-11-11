FROM openjdk:8-alpine
MAINTAINER  jay.pan@infinitus-int.com

ENV COLLECTOR_ADDRESS=127.0.0.1:10800
ENV SKYWLK_HOME = /usr/local/skywalking-ui

WORKDIR /usr/local/skywalking-ui
COPY webapp webapp
COPY bin bin

ADD docker-entrypoint.sh /
RUN chmod 755 /docker-entrypoint.sh && chmod 755 -R bin

EXPOSE 8080

# ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["bin/webappService.sh"]
