FROM debian:jessie
MAINTAINER Rudi Kramer <rudi.kramer@gmail.com>

RUN apt-get update && apt-get install -y curl python --no-install-recommends && rm -r /var/lib/apt/lists/* && \
  export DEBIAN_FRONTEND=noninteractive && \
  curl -k -s https://repo.varnish-cache.org/GPG-key.txt | apt-key add - && \
  apt-get update && apt-get install -y apt-transport-https && \
  echo "deb https://repo.varnish-cache.org/debian jessie varnish-4.1" >> /etc/apt/sources.list && \
  apt-get update && apt-get -y dist-upgrade && \
  apt-get -y install varnish && \
  rm -rf /var/lib/apt/lists/*


ADD varnish /etc/default/varnish
COPY ./docker-entrypoint.sh /

CMD ["/docker-entrypoint.sh"]