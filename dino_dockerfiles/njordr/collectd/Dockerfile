FROM ubuntu:14.04.3

MAINTAINER "Giovanni Colapinto" alfheim@syshell.net

COPY collectd.list  /etc/apt/sources.list.d/collectd.list

RUN rm -rf /var/lib/apt/lists/ \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    supervisor \
    sudo \
    software-properties-common \
    python-software-properties \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/

RUN add-apt-repository -y ppa:rullmann/collectd

RUN rm -rf /var/lib/apt/lists/ \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
    collectd \
    collectd-utils \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/

COPY collectd.conf /etc/collectd/collectd.conf

EXPOSE 25826

CMD ["/usr/sbin/collectd", "-C", "/etc/collectd/collectd.conf", "-f"]
