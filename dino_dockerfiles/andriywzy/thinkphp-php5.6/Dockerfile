#for thinkphp

FROM debian:jessie
ADD mongodb-1.1.6.tgz /


RUN apt-get update && \
    apt-get install -y --fix-missing php5-cli php5-dev php5-common php5-curl php5-fpm php5-gd php5-imagick php5-json php5-mcrypt php5-mysql php5-readline php5-redis php5-memcache php5-memcached rsyslog supervisor && \
    cd /mongodb-1.1.6 && \
    phpize && \
    ./configure --with-php-config=/usr/bin/php-config --with-libdir=/lib/x86_64-linux-gnu && \
    make all && make install && \
    rm -rf /mongodb-1.1.6 /package.xml /etc/supervisor/supervisord.conf /etc/rsyslog.conf 

COPY supervisord.conf /etc/supervisor/supervisord.conf
COPY rsyslog.conf /etc/rsyslog.conf

VOLUME ["/data"]

EXPOSE 9000

CMD ["/usr/bin/supervisord","-n"]
