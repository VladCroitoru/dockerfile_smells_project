FROM debian:wheezy

MAINTAINER Philip Vieira <philip@chatspry.com>

ENV DEBIAN_FRONTEND noninteractive
ENV RIAK_VERSION 2.0.2-1

RUN apt-get update -y && \
  apt-get install -y apt-transport-https curl adduser logrotate

RUN curl https://packagecloud.io/gpg.key | apt-key add -

RUN \
  echo "deb https://packagecloud.io/basho/riak/debian/ wheezy main" >> /etc/apt/sources.list && \
  echo "deb-src https://packagecloud.io/basho/riak/debian/ wheezy main" >> /etc/apt/sources.list

RUN apt-get update -y && \
  apt-get install -y --force-yes riak=${RIAK_VERSION} && \
  apt-get clean -y

RUN curl -L https://github.com/kelseyhightower/confd/releases/download/v0.7.0-beta1/confd-0.7.0-linux-amd64 > confd
RUN \
  mv confd /usr/local/bin/confd && \
  chmod +x /usr/local/bin/confd

RUN \
  ln -sf /dev/stdout /var/log/riak/console.log && \
  ln -sf /dev/stderr /var/log/riak/error.log && \
  ln -sf /dev/stderr /var/log/riak/crash.log && \
  chown -Rf riak:riak /var/log/riak

RUN mkdir -p \
  /etc/confd/conf.d \
  /etc/confd/templates

ADD ./riak.conf.tmpl /etc/confd/templates/riak.conf.tmpl
ADD ./riak.toml /etc/confd/conf.d/riak.toml

ADD ./run.sh /opt/run.sh
RUN chmod +x /opt/run.sh
RUN chown riak:riak /opt/run.sh

USER riak

EXPOSE 8098 8087

CMD /opt/run.sh