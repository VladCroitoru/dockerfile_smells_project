FROM kiyoto/fluentd:0.12.1-2.1.5
MAINTAINER mimperatore@gmail.com

RUN \
  apt-get update && \
  apt-get install --yes make libcurl4-gnutls-dev && \
  /usr/local/bin/gem install fluent-plugin-record-reformer fluent-plugin-elasticsearch --no-rdoc --no-ri && \
  mkdir /etc/fluent

ADD fluent.conf /etc/fluent/
ADD start.sh /start
CMD ["/start"]
