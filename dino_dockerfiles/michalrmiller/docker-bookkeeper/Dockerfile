FROM java:openjdk-8-jre-alpine
MAINTAINER Gardner Vickers <gardner.vickers@onyxplatform.org>

RUN apk add --no-cache wget bash \
    && mkdir -p /opt \
    && wget -q -O - https://archive.apache.org/dist/bookkeeper/bookkeeper-4.3.2/bookkeeper-server-4.3.2-bin.tar.gz | tar -xzf - -C /opt \
    && mv /opt/bookkeeper-server-4.3.2 /opt/bookkeeper \
    && rm -rf /opt/bookkeeper/conf

WORKDIR /opt/bookkeeper

COPY conf-dir /opt/bookkeeper/conf/
COPY bookkeeper /opt/bookkeeper/bin/

RUN ["mkdir", "-p", "/data/journal", "/data/index", "/data/ledger"]

VOLUME ["/data"]

EXPOSE 3181/tcp

ENTRYPOINT ["/opt/bookkeeper/bin/bookkeeper"]
#"/usr/local/bin/bk-docker.sh"
CMD ["bookie"]
