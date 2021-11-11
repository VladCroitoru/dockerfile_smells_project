# VERSION 2.1
# AUTHOR: Matthieu "Puckel_" Roisil
# DESCRIPTION: Basic Grafana-based
# BUILD: docker build --rm -t puckel/grafana
# SOURCE: https://github.com/puckel/docker-grafana

FROM puckel/docker-base
MAINTAINER Puckel_

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
# Work around initramfs-tools running on kernel 'upgrade': <http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>
ENV INITRD No

ENV GRAFANA_VERSION 2.1.2

RUN apt-get update -yqq \
    && apt-get install -yqq \
    libfontconfig1 \
    && curl -k -sO https://grafanarel.s3.amazonaws.com/builds/grafana_${GRAFANA_VERSION}_amd64.deb \
    && dpkg -i grafana_${GRAFANA_VERSION}_amd64.deb \
    && rm -f grafana_${GRAFANA_VERSION}_amd64.deb \
    && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/* \
    /usr/share/man \
    /usr/share/doc \
    /usr/share/doc-base

EXPOSE 3000

CMD ["/usr/sbin/grafana-server", "-config=/etc/grafana/grafana.ini","-homepath=/usr/share/grafana"]
