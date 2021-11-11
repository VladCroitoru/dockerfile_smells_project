FROM microsoft/aspnetcore:2.0.8-stretch

LABEL maintainer="Burak Ince <burak.ince@linux.org.tr>"

ENV FILEBEAT_VERSION=6.3.0

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        tar \
        supervisor \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /filebeat
RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-$FILEBEAT_VERSION-amd64.deb \
    && dpkg -i filebeat-$FILEBEAT_VERSION-amd64.deb \
    && rm filebeat-$FILEBEAT_VERSION-amd64.deb
