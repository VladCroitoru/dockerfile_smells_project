FROM ubuntu:14.04

MAINTAINER  Erik Osterman "e@osterman.com"

# http://www.sebastian.korotkiewicz.eu/2013/05/21/own-irc-server-on-debian-with-anope-and-mysql/
# http://www.anope.org/ilm.php?p=lm
# https://github.com/dockerimages/docker-unrealircd/blob/master/deploy-unrealirc.sh

# Anope
ENV ANOPE_VERSION 2.0.3
ENV ANOPE_GEOIP_DATABASE country
ENV ANOPE_SMTP_HOST 127.0.0.1

ENV ANOPE_ADMIN_EMAIL ops@localhost
ENV ANOPE_NAMESERVERS 8.8.8.8 8.8.4.4

ENV ANOPE_UPLINK_HOST localhost
ENV ANOPE_UPLINK_PORT 7000
ENV ANOPE_UPLINK_PASSWORD secret

ENV ANOPE_SERVERINFO_NAME anope.localnet
ENV ANOPE_SALT            salt

ENV ANOPE_URL http://localhost/

# Mysql
ENV MYSQL_USER irc
ENV MYSQL_PASSWORD password
ENV MYSQL_DATABASE anope
ENV MYSQL_HOST localhost
ENV MYSQL_PORT 3306
ENV MYSQL_PREFIX anope_

# System
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
ENV TERM xterm

WORKDIR /usr/src

ADD config.cache /usr/src/anope-$ANOPE_VERSION-source/config.cache

RUN echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf.d/01buildconfig && \
    echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf.d/01buildconfig && \
    echo 'APT::Get::force-yes "true";' >> /etc/apt/apt.conf.d/01buildconfig  && \
    echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf.d/01buildconfig && \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y build-essential curl libssl-dev ca-certificates cmake libpcre3-dev libmysqlclient-dev mysql-client unzip wget gettext && \
    groupadd -g 1000 anope && \
    useradd -u 1000 -g anope -d /anope/ anope && \
    curl -s --location https://github.com/anope/anope/releases/download/$ANOPE_VERSION/anope-$ANOPE_VERSION-source.tar.gz | tar xz && \
    cd anope-$ANOPE_VERSION-source && \
    cd modules/ && \
    ln -s extra/m_mysql.cpp . && \
    ln -s extra/m_sql_authentication.cpp . && \
    ln -s extra/m_sql_log.cpp . && \
    ln -s extra/m_sql_oper.cpp . && \
    ln -s extra/m_regex_pcre.cpp . && \
    ln -s extra/stats . && \
    cd ../ && \
    ./Config -quick && \
    cd build/ && \
    make && \
    make install && \
    sed -i -r 's/^(geoip_database)=.*/\1=$ANOPE_GEOIP_DATABASE/' /anope/bin/geoipupdate.sh && \
    sed -i -r 's/^(mysql_host)=.*/\1=$MYSQL_HOST/' /anope/bin/geoipupdate.sh && \
    sed -i -r 's/^(mysql_user)=.*/\1=$MYSQL_USER/' /anope/bin/geoipupdate.sh && \
    sed -i -r 's/^(mysql_password)=.*/\1=$MYSQL_PASSWORD/' /anope/bin/geoipupdate.sh && \
    sed -i -r 's/^(mysql_database)=.*/\1=$MYSQL_DATABASE/' /anope/bin/geoipupdate.sh && \
    sed -i -r 's/^(prefix)=.*/\1=$MYSQL_PREFIX/' /anope/bin/geoipupdate.sh && \
    sed -i -r 's/^(die)=.*/\1=no/' /anope/bin/geoipupdate.sh && \
    sed -i -r 's/\$prefix"geoip_country6\.csv"//' /anope/bin/geoipupdate.sh && \
    rm -rf /anope/logs && \
    mkdir -p /anope/logs && \
    rm -rf /anope/confg && \
    mkdir -p /anope/conf && \
    chown -R anope:anope -R /anope/ && \
    apt-get -y remove build-essential cmake && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/src/* 

VOLUME [ "/anope/log" ]

WORKDIR /anope

ADD start /start
ADD templates/ /anope/templates

USER anope

EXPOSE 8080

ENTRYPOINT ["/start"]
