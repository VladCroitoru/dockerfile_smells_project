FROM ubuntu:14.04

MAINTAINER Leonardo Gamas <leogamas@gmail.com>

ENV BUILD_DEPS git openjdk-7-jdk maven
ENV RUNTIME_DEPS openjdk-7-jre-headless
ENV SECOR_VERSION 0.20

RUN apt-get update \
	&& apt-get install -y $BUILD_DEPS $RUNTIME_DEPS --no-install-recommends \
	&& git clone --branch v${SECOR_VERSION} https://github.com/pinterest/secor.git \
	&& cd secor && mvn clean package && cd .. \
	&& mkdir /opt/secor \
	&& tar zxvf secor/target/secor-${SECOR_VERSION}-SNAPSHOT-bin.tar.gz -C /opt/secor \
	&& apt-get purge -y --auto-remove $BUILD_DEPS \
	&& rm -rf secor

RUN ln -s /opt/secor/secor-${SECOR_VERSION}-SNAPSHOT.jar /opt/secor/secor.jar

ADD run.sh /opt/secor/run.sh

WORKDIR /opt/secor

ENTRYPOINT ["/opt/secor/run.sh"]

