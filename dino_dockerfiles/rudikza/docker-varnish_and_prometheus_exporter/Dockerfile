FROM debian:jessie
MAINTAINER Rudi Kramer <rudi.kramer@gmail.com>

RUN apt-get update && apt-get install -y curl python supervisor golang git ca-certificates --no-install-recommends && \
  rm -r /var/lib/apt/lists/* && \
  curl http://repo.varnish-cache.org/GPG-key.txt | apt-key add -- && \
  echo "deb http://repo.varnish-cache.org/debian/ jessie varnish-4.1" >> /etc/apt/sources.list.d/varnish-cache.list && \
  apt-get update && apt-get install -y varnish --no-install-recommends && \
  rm -r /var/lib/apt/lists/*

RUN useradd -ms /bin/bash prometheus_varnish_exporter && \
  export GOPATH=/home/prometheus_varnish_exporter/go && \
  export PATH=$PATH:$GOROOT/bin:$GOPATH/bin && \
  go get github.com/jonnenauha/prometheus_varnish_exporter

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD varnish /etc/default/varnish

EXPOSE 9131

CMD ["/usr/bin/supervisord"]
