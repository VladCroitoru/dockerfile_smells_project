FROM openjdk:8

LABEL MAINTAINER Bitworks Software info@bitworks.software

ENV INFLUX_URL=http://localhost:8086/ \
    INFLUX_USER=puls \
    INFLUX_PASSWORD=puls \
    INFLUX_DB=secret \
    NGINX_CACHE_TIME=15s \
    NGINX_RATE_LIMIT=20r/s \
    DEBUG=false \
    version=1.0.3.2-SNAPSHOT \
    scala_version=2.12 \
    jetty_version=9.4.6.v20170531

ADD ./docker /opt/bin/docker

RUN apt-get update && \
    apt-get install -y --no-install-recommends nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /opt/bin && \
    mkdir -p /var/lib/jetty/webapps && \
    curl -o /opt/bin/jetty.jar http://central.maven.org/maven2/org/eclipse/jetty/jetty-runner/${jetty_version}/jetty-runner-${jetty_version}.jar && \
    curl -o /var/lib/jetty/webapps/cs-pulse-server.war https://oss.sonatype.org/content/repositories/snapshots/com/bwsw/cs-pulse-server_${scala_version}/${version}/cs-pulse-server_${scala_version}-${version}.war && \
    mv /opt/bin/docker/nginx.conf /etc/nginx/nginx.conf && \
    rm /etc/nginx/sites-available/default && \
    rm -Rf /var/cache/apt/* && \
    rm -Rf /var/lib/apt/lists/*

EXPOSE 9090

CMD ["/bin/bash", "/opt/bin/docker/run.sh"]