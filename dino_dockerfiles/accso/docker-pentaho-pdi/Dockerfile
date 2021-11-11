# See https://github.com/accso/docker-pentaho-pdi
FROM debian:stretch-slim
MAINTAINER marcus.rickert@accso.de
RUN adduser --disabled-login --uid 1000 pentaho
RUN chown pentaho.pentaho /home/pentaho
ARG MAJOR_MINOR_VERSION=8.0
ARG VERSION=8.0.0.0-28
ENV FILENAME=pdi-ce-${VERSION}.zip
ENV URL=https://kent.dl.sourceforge.net/project/pentaho/Pentaho%20${MAJOR_MINOR_VERSION}/client-tools/${FILENAME}
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y install \
	   curl \
	   unzip \
	   libwebkitgtk-1.0-0 \
	   libxtst6 \
    && mkdir -p /opt \
    && echo "Downloading ${URL}" \
    && curl -k -s -o /opt/${FILENAME} -L ${URL} \
    && cd /opt \
    && unzip ${FILENAME} \
    && rm ${FILENAME}
COPY assets/docker-entrypoint.sh /docker-entrypoint.sh
ENV DOCKER_USER=pentaho
RUN mkdir -p /home/${DOCKER_USER}/home_on_host
ENTRYPOINT [ "/docker-entrypoint.sh" ]
