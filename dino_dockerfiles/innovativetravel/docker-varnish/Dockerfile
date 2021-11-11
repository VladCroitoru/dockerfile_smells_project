# Varnish
#
# WEBSITE https://github.com/Zenedith/docker-varnish
# VERSION 1.1.1

FROM ubuntu
MAINTAINER Mateusz Stępniak "zenedith@wp.pl"

# make sure the package repository is up to date
RUN apt-get update
RUN apt-get install git pkg-config dpkg-dev autoconf curl make autotools-dev automake libtool libpcre3-dev libncurses-dev python-docutils bsdmainutils debhelper dh-apparmor gettext gettext-base groff-base html2text intltool-debian libbsd-dev libbsd0 libcroco3 libedit-dev libedit2 libgettextpo0 libpipeline1 libunistring0 man-db po-debconf xsltproc -y

# download repo key
RUN curl -s http://repo.varnish-cache.org/debian/GPG-key.txt | apt-key add -
RUN echo "deb http://repo.varnish-cache.org/ubuntu/ $(lsb_release -sc) varnish-3.0" | tee -a /etc/apt/sources.list
RUN echo "deb-src http://repo.varnish-cache.org/ubuntu/ $(lsb_release -sc) varnish-3.0" | tee -a /etc/apt/sources.list

# update varnish packages
RUN apt-get update && apt-get clean

# install varnish
RUN cd /opt && apt-get source varnish=3.0.5-2
RUN cd /opt/varnish-3.0.5 && ./autogen.sh
RUN cd /opt/varnish-3.0.5 && ./configure
RUN cd /opt/varnish-3.0.5 && make -j3
RUN cd /opt/varnish-3.0.5 && make install

# install varnish libvmod-throttle
RUN git clone https://github.com/nand2/libvmod-throttle.git /opt/libvmod-throttle
RUN cd /opt/libvmod-throttle && ./autogen.sh
RUN cd /opt/libvmod-throttle && ./configure VARNISHSRC=/opt/varnish-3.0.5
RUN cd /opt/libvmod-throttle && make -j3
RUN cd /opt/libvmod-throttle && make install

ENV LISTEN_ADDR 0.0.0.0
ENV LISTEN_PORT 8080

ENV BACKEND_ENV_PORT 5000
ENV BACKEND_PORT_5000_TCP_ADDR 0.0.0.0

ENV TELNET_ADDR 0.0.0.0
ENV TELNET_PORT 6083
ENV CACHE_SIZE 25MB
ENV THROTTLE_LIMIT 150req/30s
ENV VCL_FILE /etc/varnish/default.vcl
ENV GRACE_TTL 30s
ENV GRACE_MAX 1h

ADD config/default.vcl.source /etc/varnish/default.vcl.source
ADD bin/run.sh /bin/run.sh
ADD bin/reload.sh /bin/reload.sh
RUN chmod +x /bin/reload.sh

EXPOSE 8080

CMD /bin/run.sh
