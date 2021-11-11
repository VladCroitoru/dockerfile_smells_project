FROM java:openjdk-8-jre
MAINTAINER mkroli

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

ADD https://raw.githubusercontent.com/paulp/sbt-extras/master/sbt /usr/bin/sbt
RUN chmod 0755 /usr/bin/sbt

ADD build.sbt /tmp/shurl/build.sbt
ADD web.sbt /tmp/shurl/web.sbt
ADD project/plugins.sbt /tmp/shurl/project/plugins.sbt
ADD src /tmp/shurl/src

WORKDIR /tmp/shurl
RUN sbt packArchive && \
    mkdir -p /opt/shurl && \
    tar --strip-components=1 -C /opt/shurl -xzf /tmp/shurl/target/shurl*.tar.gz && \
    rm -rf /root/.ivy /root/.sbt /tmp/shurl

WORKDIR /opt/shurl
EXPOSE 8080
ENTRYPOINT JAVA_OPTS=-Dcassandra.seeds.0=${CASSANDRA_PORT_9042_TCP_ADDR} /opt/shurl/bin/shurl
