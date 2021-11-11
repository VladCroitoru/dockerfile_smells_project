FROM debian:jessie
MAINTAINER Mohammad Abdoli Rad <m.abdolirad@gmail.com>

RUN echo "deb http://mirror.leaseweb.net/debian/ stable main" > /etc/apt/sources.list \
    && echo "deb http://mirror.leaseweb.net/debian/ jessie-updates main" >> /etc/apt/sources.list \
    && echo "deb http://security.debian.org/ jessie/updates main" >> /etc/apt/sources.list \
    && apt-get update \
    && DEBCONF_FRONTEND=noninteractive apt-get install -y curl sudo zsh git \
        zip dnsutils mlocate logrotate locales nano \
        nginx openssh-server postgresql-client-9.4 postgresql-9.4 \
        php5-cli php5-curl php-pear php5-dev php5-fpm php5-gd php5-mcrypt \
        php5-intl php5-mysql php5-pgsql php5-redis php5-xdebug php5-xsl \
    && rm -rf /var/lib/apt/lists/*

COPY assets/ /opt/radphp/
RUN chmod 755 /opt/radphp/install.sh
RUN chmod 755 /opt/radphp/init.sh

RUN /opt/radphp/install.sh

WORKDIR /srv/www
ENTRYPOINT ["/opt/radphp/init.sh"]
CMD ["start"]

EXPOSE 80 8080 443 5432 53/udp
