#Pre-built JDK 8 image
FROM kurron/docker-oracle-jdk-8:latest

MAINTAINER Ron Kurr <kurr@jvmguy.com>

RUN mkdir /opt/example
RUN mkdir /config

VOLUME /config

ADD http://mirrors.ibiblio.org/apache/jmeter/binaries/apache-jmeter-2.13.tgz /opt/example/jmeter.tgz

WORKDIR /opt/example
RUN tar zxvf /opt/example/jmeter.tgz

ADD configuration.jmx /config/configuration.jmx

WORKDIR /opt/example/apache-jmeter-2.13

ENTRYPOINT ["bin/jmeter", "-n", "-t", "/config/configuration.jmx"]

