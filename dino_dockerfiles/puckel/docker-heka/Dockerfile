# VERSION 1.0
# AUTHOR: Matthieu "Puckel_" Roisil
# DESCRIPTION: Basic Heka container
# BUILD: docker build --rm -t puckel/docker-heka
# SOURCE: https://github.com/puckel/docker-heka

FROM puckel/docker-base
MAINTAINER Puckel_

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
# Work around initramfs-tools running on kernel 'upgrade': <http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>
ENV INITRD No

ENV HEKA_VERSION 0.10.0b1

RUN curl -sOL https://github.com/mozilla-services/heka/releases/download/v${HEKA_VERSION}/heka_${HEKA_VERSION}_amd64.deb \
    && dpkg -i heka_${HEKA_VERSION}_amd64.deb \
    && rm -f heka_${HEKA_VERSION}_amd64.deb \
    && apt-get clean \
    && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/* \
    /usr/share/man \
    /usr/share/doc \
    /usr/share/doc-base

ADD config/hekad /etc/heka/conf.d
EXPOSE 4352 5514 8125/udp

CMD ["/usr/bin/hekad", "-config=/etc/heka/conf.d"]
