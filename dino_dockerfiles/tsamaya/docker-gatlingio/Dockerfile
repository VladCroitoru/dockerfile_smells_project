# Gatling  is Open-Source Load & Performance Testing Tool For Web Applications
#
# Documentation: http://gatling.io/docs
# Cheat sheet: http://gatling.io/#/cheat-sheet/
FROM openjdk:8-jdk-alpine

WORKDIR /opt

# Gatling.io version
ENV GATLING_VERSION 2.3.0

# create directory for gatling install
RUN mkdir -p gatling

# install gatling
RUN apk add --update wget && \
  mkdir -p /tmp/downloads && \
  wget -q -O /tmp/downloads/gatling-$GATLING_VERSION.zip \
  https://repo1.maven.org/maven2/io/gatling/highcharts/gatling-charts-highcharts-bundle/$GATLING_VERSION/gatling-charts-highcharts-bundle-$GATLING_VERSION-bundle.zip && \
  mkdir -p /tmp/archive && cd /tmp/archive && \
  unzip /tmp/downloads/gatling-$GATLING_VERSION.zip && \
  mv /tmp/archive/gatling-charts-highcharts-bundle-$GATLING_VERSION/* /opt/gatling/ && \
  rm -rf /tmp/*

# working directory for gatling
WORKDIR  /opt/gatling

# set directories below to be mountable from host
VOLUME ["/opt/gatling/conf", "/opt/gatling/results", "/opt/gatling/user-files"]

# set environment variables
ENV PATH /opt/gatling/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
ENV GATLING_HOME /opt/gatling
ENV JAVA_OPTS ""

ENTRYPOINT ["gatling.sh"]
