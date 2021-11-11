FROM alpine
MAINTAINER TTP/ITP <admin@particle.kit.edu>

RUN apk update && apk upgrade && apk add \
    vim bash git make java-gcj-compat rrdtool python ruby \
    perl perl-module-build perl-rrd perl-net-snmp perl-namespace-autoclean \
    perl-log-log4perl perl-html-template perl-net-ssleay \
    perl-net-server perl-date-manip perl-io-socket-inet6 \
    perl-log-dispatch perl-dbi perl-dbd-sqlite perl-http-server-simple \
    perl-file-copy-recursive perl-fcgi perl-uri ttf-dejavu \
    dcron wget curl g++ perl-dev pcre-dev expat expat-dev tzdata &&\
    adduser -u 497 -D munin &&\
    git clone git://github.com/munin-monitoring/munin /munin &&\
    cd /munin && perl Build.PL && yes| ./Build installdeps &&\ 
    ./Build && make && make install && cd / && rm -rf /munin &&\
    cp /usr/share/zoneinfo/Europe/Berlin /etc/localtime &&\
    echo "Europe/Berlin" > /etc/timezone &&\
    apk del tzdata g++ perl-dev pcre-dev expat expat-dev git make &&\
    install -m 755 -d -o munin -g munin /var/run/munin /var/lib/munin /var/log/munin &&\
    mkdir /usr/local/etc/munin/plugins &&\
    mkdir /usr/local/etc/munin/munin-conf.d &&\
    mkdir /usr/local/etc/munin/plugin-conf.d  &&\
    cp /usr/local/etc/munin/munin-node.conf.sample /usr/local/etc/munin/munin-node.conf

ADD init.sh /init.sh
ADD fetch_inventory.sh /usr/local/bin/
ADD munin.conf /usr/local/etc/munin/munin.conf

ENV MUNIN_CRON="*/5 * * * *" \
    MUNIN_WORKERS="16" \
    MUNIN_TIMEOUT="20" \
    HOSTS_URL="" \
    NOTIFICATION_FROM="admin@munin" \
    NOTIFICATION_TO="admin@munin" \
    NOTIFICATION_NAME="admin" \
    NOTIFICATION_RELAY="smarthost.example.com"

VOLUME /usr/local/etc/munin/
VOLUME /var/lib/munin/

ENTRYPOINT ["./init.sh"]
CMD ["/usr/local/bin/munin-httpd"]
