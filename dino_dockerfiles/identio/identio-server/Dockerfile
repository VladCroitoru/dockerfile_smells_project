FROM azul/zulu-openjdk-alpine:8

# Add the sources to the application
ADD . /tmp/identio-server-build

# Prepare system
RUN apk update \
    && apk upgrade \
    && apk add bash libstdc++ git \
    && addgroup -S identio \
    && adduser -S -g identio identio \
    && mkdir /opt

# Install Identio
RUN cd /tmp/identio-server-build \
	&& ./gradlew releaseTarGz \
	&& cd /opt \
	&& tar -xzvf /tmp/identio-server-build/build/distributions/identio-server.tar.gz \
	&& cp /tmp/identio-server-build/docker/entrypoint.sh / \
	&& rm -rf /tmp/identio-server-build \
	&& chown -R identio:identio /opt/identio-server/config/work

USER identio
 
WORKDIR /opt/identio-server

ENTRYPOINT ["/entrypoint.sh"]
