FROM ubuntu:14.04
MAINTAINER patrick@oberdorf.net

ENV VERSION 1.5.9
ENV DEBIAN_FRONTEND noninteractive
ENV DNS_SERVER 223.5.5.5

WORKDIR /usr/local/src/
ADD assets/sha256checksum sha256checksum

# RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak
# ADD ./sources.list.trusty /etc/apt/sources.list
RUN apt-get update && apt-get install -y \
	build-essential \
	tar \
	wget \
	libssl-dev \
	libevent-dev \
	libevent-2.0-5 \
	libexpat1-dev \
	dnsutils \
	byacc \
	supervisor \
	subversion \
	git \
# RUN wget http://mirrors.xu1s.com/unbound-${VERSION}.tar.gz -P /usr/local/src/ \
#	&& sha256sum -c sha256checksum \
#	&& tar -xvf unbound-${VERSION}.tar.gz \
#	&& rm unbound-${VERSION}.tar.gz \
#	&& cd unbound-${VERSION} \

	&& svn co http://unbound.nlnetlabs.nl/svn/branches/edns-subnet/ \
	&& cd edns-subnet \
	&& ./configure --enable-subnet --prefix=/usr/local --with-libevent \
	&& make -j2\
	&& make install \
	&& cd ../ \

	&& apt-get -y install software-properties-common \
	&& add-apt-repository ppa:anton+/dnscrypt \
	&& apt-get update && apt-get -y --force-yes install dnscrypt-proxy  \

	&& git clone --depth=1 https://github.com/felixonmars/dnsmasq-china-list.git \

	&& apt-get autoremove build-essential subversion git --purge -y \
	&& apt-get clean

RUN cd dnsmasq-china-list \
	&& sed -e "s|^server=/\(.*\)/114.114.114.114$$|\1|" accelerated-domains.china.conf | egrep -v '^#' > accelerated-domains.china.raw.txt \
	&& sed -e "s|^server=/\(.*\)/114.114.114.114$$|\1|" google.china.conf | egrep -v '^#' > google.china.raw.txt \
	&& sed -e "s|\(.*\)|forward-zone:\n  name: \"\1.\"\n  forward-addr: ${DNS_SERVER}\n|" accelerated-domains.china.raw.txt > accelerated-domains.china.unbound.conf \
	&& sed -e "s|\(.*\)|forward-zone:\n  name: \"\1.\"\n  forward-addr: ${DNS_SERVER}\n|" google.china.raw.txt > google.china.unbound.conf \
	&& cp ./accelerated-domains.china.unbound.conf /usr/local/etc/unbound/accelerated-domains.china.unbound.conf \
	&& cp ./google.china.unbound.conf /usr/local/etc/unbound/google.china.unbound.conf \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/local/src/*

ADD assets/dnscrypt-proxy /etc/default/dnscrypt-proxy
ADD assets/unbound.conf /usr/local/etc/unbound/unbound.conf
ADD assets/custom.conf /usr/local/etc/unbound/custom.conf

RUN useradd --system unbound --home /home/unbound --create-home
RUN chown -R unbound:unbound /usr/local/etc/unbound/
ENV PATH $PATH:/usr/local/lib
RUN ldconfig

USER unbound
RUN unbound-anchor -a /usr/local/etc/unbound/root.key ; true
RUN unbound-control-setup \
	&& wget ftp://FTP.INTERNIC.NET/domain/named.cache -O /usr/local/etc/unbound/root.hints

USER root
RUN mkdir -p /var/log/supervisor
COPY /assets/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 53/udp
EXPOSE 53

CMD ["/start.sh"]
