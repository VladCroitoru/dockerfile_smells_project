FROM openjdk:8-alpine

MAINTAINER Nils Bokermann <nils.bokermann@bermuda.de>

ENV CROWD_VERSION 4.4.0
# Setup useful environment variables
ENV CROWD_DATA     /var/atlassian/crowd
# Must match entry in crowd-init.properties
ENV CROWD_INSTALL  /opt/atlassian/crowd

EXPOSE 8080
EXPOSE 8443

VOLUME ${CROWD_DATA}

RUN set -x \
    && apk --no-cache add curl bash \
    && mkdir -p ${CROWD_INSTALL} \
    && mkdir -p ${CROWD_DATA} \
    && curl -Ls https://product-downloads.atlassian.com/software/crowd/downloads/atlassian-crowd-${CROWD_VERSION}.tar.gz | tar -xz --directory "${CROWD_INSTALL}" --strip-components=1 --no-same-owner

COPY config/crowd-init.properties ${CROWD_INSTALL}/crowd-webapp/WEB-INF/classes
COPY config/server.xml ${CROWD_INSTALL}/apache-tomcat/conf

WORKDIR /var/atlassian/crowd

CMD ${CROWD_INSTALL}/start_crowd.sh -fg
