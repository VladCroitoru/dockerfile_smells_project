FROM debian:jessie

ENV PERL5LIB /opt/nagios/libexec:/opt/nagios/perl/lib
ENV NAGIOS_VERSION 4.2.4
ENV NAGIOS_PLUGINS_VERSION 2.1.4
ENV NRPE_VERSION 3.0

WORKDIR /tmp
RUN useradd nagios && \
    groupadd nagcmd && \
    usermod -a -G nagcmd nagios && \
    apt-get update && \
    apt-get install -y --no-install-recommends wget build-essential unzip apache2-utils ca-certificates && \
    wget https://assets.nagios.com/downloads/nagioscore/releases/nagios-${NAGIOS_VERSION}.tar.gz && \
    tar -zxvf nagios-${NAGIOS_VERSION}.tar.gz && \
    cd nagios-${NAGIOS_VERSION} && \
    ./configure --prefix=/opt/nagios --sysconfdir=/etc/nagios --localstatedir=/var/lib/nagios --with-nagios-group=nagios --with-command-group=nagcmd && \
    make all && \
    make install && \
    make install-commandmode && \
    make install-config && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN apt-get update && \
    apt-get install -y --no-install-recommends libmysqlclient-dev libssl-dev dnsutils openssh-client && \
    wget http://www.nagios-plugins.org/download/nagios-plugins-${NAGIOS_PLUGINS_VERSION}.tar.gz && \
    tar -zxvf nagios-plugins-${NAGIOS_PLUGINS_VERSION}.tar.gz && \
    cd nagios-plugins-${NAGIOS_PLUGINS_VERSION} && \
    ./configure --prefix=/opt/nagios --with-nagios-user=nagios --with-nagios-group=nagios --enable-perl-modules --with-ping-command="/bin/ping -w 4 -n -c %d %s" && \
    make && \
    make install && \
    rm -rf /tmp/nagios-plugins-${NAGIOS_PLUGINS_VERSION}.tar.gz /tmp/nagios-plugins-${NAGIOS_PLUGINS_VERSION}

RUN apt-get update && \
    apt-get install -y --no-install-recommends openssl && \
    wget --no-check-certificate https://github.com/NagiosEnterprises/nrpe/archive/${NRPE_VERSION}.tar.gz && \
    tar -zxvf ${NRPE_VERSION}.tar.gz && \
    cd nrpe-${NRPE_VERSION} && \
    ./configure --prefix=/opt/nagios --enable-command-args --enable-ssl --enable-bash-command-substitution && \
    make check_nrpe && \
    make install-plugin && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /
COPY docker-entrypoint.sh /docker-entrypoint.sh

VOLUME ["/var/lib/nagios", "/etc/nagios"]
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/opt/nagios/bin/nagios", "/etc/nagios/nagios.cfg"]
