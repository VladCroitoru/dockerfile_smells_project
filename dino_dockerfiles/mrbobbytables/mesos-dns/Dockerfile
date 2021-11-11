################################################################################
# mesos-dns:1.3.0
# Date: 12/18/2015
# Mesos-DNS Version: 0.5.1
#
# Description:
# Provides DNS for almost all services hosted in Mesos. 
#################################################################################

FROM mrbobbytables/ubuntu-base:1.1.0
MAINTAINER Bob Killen / killen.bob@gmail.com / @mrbobbytables

ENV VERSION_MESOSDNS=0.5.1

RUN apt-get update      \
 && apt-get -y install  \
    wget                \
 && wget -O /usr/local/bin/mesos-dns \
    https://github.com/mesosphere/mesos-dns/releases/download/v${VERSION_MESOSDNS}/mesos-dns-v${VERSION_MESOSDNS}-linux-amd64  \
 && chmod +x /usr/local/bin/mesos-dns  \
 && mkdir -p /etc/mesos-dns            \
 && mkdir -p /var/log/mesos-dns        \
 && apt-get -y autoremove              \
 && apt-get -y clean                   \
 && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./skel /

RUN chmod +x ./init.sh  \
 && chown -R logstash-forwarder:logstash-forwarder /opt/logstash-forwarder

EXPOSE 53 8123

CMD ["./init.sh"]
