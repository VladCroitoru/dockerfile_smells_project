FROM alpine
LABEL maintener="pokido99@gmail.com"

# Proxy settings if necessary
# ENV http_proxy=http://proxy:8080
# ENV https_proxy=http://proxy:8080
# ENV no_proxy="127.0.0.1,localhost,.mydomain.com"

# Install Java
RUN apk --no-cache add openjdk8-jre

# Install misc tools
RUN apk --no-cache add curl tar

# Install Nexus
ENV NEXUS_USER nexus
ENV NEXUS_HOME /opt/nexus
ENV NEXUS_VERSION 3.3.1-01

RUN mkdir -p /opt/sonatype-work/nexus3 && adduser -D -h $NEXUS_HOME $NEXUS_USER && curl -s https://sonatype-download.global.ssl.fastly.net/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz | tar -xz -C $NEXUS_HOME --strip-components=1 nexus-${NEXUS_VERSION} && chown -R ${NEXUS_USER}: $NEXUS_HOME /opt/sonatype-work

USER $NEXUS_USER
WORKDIR $NEXUS_HOME

EXPOSE 8081
CMD ${NEXUS_HOME}/bin/nexus run
