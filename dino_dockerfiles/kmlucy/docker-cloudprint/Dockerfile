FROM golang:1-stretch
LABEL maintainer "Kyle Lucy <kmlucy@gmail.com>"

RUN mkdir /config \
  && apt-get update \
  && apt-get install -y build-essential libcups2-dev libsnmp-dev libavahi-client-dev git bzr \
  && go get github.com/google/cloud-print-connector/... \
  && apt-get purge -y build-essential git bzr \
  && apt-get autoremove --purge -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/

VOLUME /config

CMD gcp-cups-connector -config-filename /config/gcp-cups-connector.config.json --log-to-console
