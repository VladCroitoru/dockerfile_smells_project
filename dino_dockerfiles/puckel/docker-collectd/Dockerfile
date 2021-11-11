# VERSION 1.0
# AUTHOR: Matthieu "Puckel_" Roisil
# DESCRIPTION: Basic collectd-based
# BUILD: docker build --rm -t puckel/collectd
# SOURCE: https://github.com/puckel/docker-collectd

FROM puckel/docker-base
MAINTAINER Puckel_

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
# Work around initramfs-tools running on kernel 'upgrade': <http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>
ENV INITRD No

RUN apt-get update -yqq \
    && apt-get install -yqq \
    collectd \
    supervisor \
    python-pip \
    && pip install envtpl \
    && apt-get clean \
    && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/* \
    /usr/share/man \
    /usr/share/doc \
    /usr/share/doc-base

ADD config/collectd.conf.tpl /etc/collectd/collectd.conf.tpl
ADD config/write_graphite.conf.tpl /etc/collectd/collectd.conf.d/write_graphite.conf.tpl
ADD config/write_influxdb.conf.tpl /etc/collectd/collectd.conf.d/write_influxdb.conf.tpl
ADD config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD scripts/run.sh /root/run.sh
RUN chmod +x /root/run.sh

CMD ["/root/run.sh"]
