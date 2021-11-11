FROM ubuntu:14.04
MAINTAINER Jason Kulatunga <jason@thesparktree.com>

RUN \
  sed -i 's/^# \(.*-backports\s\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get install -y wget curl build-essential
  apt-get build-dep -y haproxy=1.5.3-1~ubuntu14.04.1

RUN mkdir -p /tmp/haproxy/
WORKDIR /tmp/haproxy/
RUN wget http://www.haproxy.org/download/1.5/src/haproxy-1.5.4.tar.gz
RUN tar xzvf haproxy-1.5.4.tar.gz
RUN cd haproxy-1.5.4 && make TARGET=linux26 && make install

ADD haproxy.cfg /etc/haproxy/haproxy.cfg
ADD startup.sh /startup.sh
RUN chmod u+x /startup.sh
ADD hap.sh /hap.sh
RUN chmod u+x /hap.sh

RUN curl -L -o /tmp/consul-template https://github.com/hashicorp/consul-template/releases/download/v0.3.0/consul-template_0.3.0_linux_amd64.tar.gz && \
  cd /tmp && \
  tar -xf consul-template && \
  cp consul-template_0.3.0_linux_amd64/consul-template /usr/local/bin/consul-template && \
  chmod a+x /usr/local/bin/consul-template

ADD haproxy.template /etc/haproxy/haproxy.template

WORKDIR /

CMD ["/startup.sh"]
