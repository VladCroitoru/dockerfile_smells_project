#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "update.sh"
#
# PLEASE DO NOT EDIT IT DIRECTLY.
#

FROM alpine:edge

# Default to UTF-8 file.encoding
ENV LANG C.UTF-8

RUN { \
	echo '#!/bin/sh'; \
	echo 'set -e'; \
	echo; \
	echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \
} > /usr/local/bin/docker-java-home \
&& chmod +x /usr/local/bin/docker-java-home
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin

ENV JAVA_VERSION 8u111
ENV JAVA_ALPINE_VERSION 8.111.14-r1
ENV LOG_LEVEL INFO
ENV CONF_DIR /etc/aws-kinesis
ENV LOG_DIR /var/log

RUN set -x \
	&& apk add --no-cache openjdk8="$JAVA_ALPINE_VERSION" \
	&& [ "$JAVA_HOME" = "$(docker-java-home)" ]

#COPY custom.log4j.xml /custom.log4j.xml
RUN apk add --no-cache --virtual .build maven git\
	&& mkdir src \
	&& cd src \
	&& git clone --depth 1 https://github.com/awslabs/amazon-kinesis-agent.git \
	&& cd amazon-kinesis-agent/ \
	&& mkdir -p src/main/resources/com/amazon/kinesis/streaming/agent \
	&& cp src/com/amazon/kinesis/streaming/agent/custom.log4j.xml src/main/resources/com/amazon/kinesis/streaming/agent/custom.log4j.xml \
	&& mvn package \
	&& mvn dependency:copy-dependencies \
	&& mkdir -p /aws-kinesis-agent/lib $CONF_DIR\
	&& mv /src/amazon-kinesis-agent/target/amazon-kinesis-agent-1.1.jar /aws-kinesis-agent/lib \
	&& mv /src/amazon-kinesis-agent/target/dependency/* /aws-kinesis-agent/lib \
	&& cd / \
	&& apk del --purge .build \
	&& rm -rf /src /root/.m2

COPY agent.json /etc/aws-kinesis/agent.json
COPY start.sh /start.sh

CMD /start.sh -L $LOG_LEVEL -l /dev/stdout
