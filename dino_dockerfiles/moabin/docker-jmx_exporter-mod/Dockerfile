FROM anapsix/alpine-java:8
MAINTAINER moabin <moabin@gmail.com>

RUN apk update && apk upgrade && apk --update add curl && rm -rf /tmp/* /var/cache/apk/*

ENV VERSION 0.11-SNAPSHOT
ENV JAR jmx_prometheus_httpserver-$VERSION-jar-with-dependencies.jar

RUN curl --insecure -L https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64 -o usr/local/bin/dumb-init && chmod +x /usr/local/bin/dumb-init

RUN mkdir -p /opt/jmx_exporter
RUN curl -L https://github.com/moabin/jmx_exporter_mod/raw/master/jmx_prometheus_httpserver/target/$JAR -o /opt/jmx_exporter/$JAR
COPY start.sh /opt/jmx_exporter/
RUN chmod +x /opt/jmx_exporter/start.sh
COPY config.yml /opt/jmx_exporter/

CMD ["usr/local/bin/dumb-init", "/opt/jmx_exporter/start.sh"]
