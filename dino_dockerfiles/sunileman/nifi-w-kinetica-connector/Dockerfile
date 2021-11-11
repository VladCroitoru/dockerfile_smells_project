FROM alpine:latest
MAINTAINER sunile manjee smanjee@kinetica.com

ENV PATH $PATH:/nifi/bin

ARG NIFI_VERSION=1.3.0

ARG TAR=nifi-${NIFI_VERSION}-bin.tar.gz

LABEL Description="Nifi" \
      "Nifi Version"="$NIFI_VERSION"

WORKDIR /


RUN \
    apk add --no-cache bash openjdk8-jre-base wget tar && \
    #if [ "${NIFI_VERSION:0:3}" = "0.7" ]; then \
    #    url="http://www.apache.org/dyn/closer.lua?filename=nifi/${NIFI_VERSION}/${TAR}&action=download"; \
    #else \
        url="http://archive.apache.org/dist/nifi/${NIFI_VERSION}/${TAR}"; \
    #fi && \
    wget -t 100 --retry-connrefused -O "${TAR}" "$url" && \
    tar zxf "${TAR}" && \
    rm -fv  "${TAR}" && \
    ln -sv "nifi-${NIFI_VERSION}" nifi && \
    #{ rm -rf nifi/docs; : ; } && \
    apk del wget tar


RUN apk add --update openssl
RUN wget https://s3.amazonaws.com/kinetica-se/NiFi-Connector/6.1/nifi-GPUdbNiFi-nar-6.1.0.nar -P /nifi/lib

EXPOSE 8080

CMD nifi.sh start; tail -f /nifi/log*/*
