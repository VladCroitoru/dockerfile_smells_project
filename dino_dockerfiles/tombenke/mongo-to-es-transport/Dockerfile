FROM ubuntu:16.04

MAINTAINER Tamás Benke <tombenke@gmail.com>

## See also: https://github.com/compose/transporter/releases/tag/v0.4.0-rc.1
ENV TRANSPORTER_VERSION 0.4.0-rc.1
ENV TRANSPORTER_PLATFORM linux-amd64
ENV TRANSPORTER_DOWNLOAD_URI https://github.com/compose/transporter/releases/download/v${TRANSPORTER_VERSION}/transporter-${TRANSPORTER_VERSION}-${TRANSPORTER_PLATFORM}

ENV DB_NAME test
ENV MONGODB_URI mongodb://localhost:27017
ENV ELASTICSEARCH_URI http://localhost:9200

## install
RUN apt-get update && \
	apt-get install -y \
		curl \
        sudo \
        netcat \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

RUN curl --verbose -SL -o /usr/local/bin/transporter "${TRANSPORTER_DOWNLOAD_URI}" && \
  chmod +x /usr/local/bin/transporter

COPY ./pipeline.js . 
COPY ./wait-for.sh . 
COPY ./wait-for-then-run.sh . 

CMD ./wait-for-then-run.sh
