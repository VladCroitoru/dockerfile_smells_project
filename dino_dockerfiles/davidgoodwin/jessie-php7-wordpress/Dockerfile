FROM debian:stretch-slim

ENV DEBIAN_FRONTEND=noninteractive

COPY sources.list /etc/apt/sources.list
#COPY 90-expire-check /etc/apt/apt.conf.d/90-expire-check

RUN apt-get -qq update && \
    apt-get -qy install eatmydata && \
    eatmydata -- apt-get -qy install apt-transport-https && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY debsury.gpg /etc/apt/trusted.gpg.d/debsury.gpg
COPY debsury.list /etc/apt/sources.list.d/debsury.list
COPY php-local.ini /etc/php/7.0/apache2/conf.d/php-local.ini
COPY msmtprc /etc/msmtprc

RUN apt-get -qq update && \
    eatmydata -- apt-get -qy install ca-certificates curl \
        php7.0 libapache2-mod-php7.0 \
        php7.0-xsl php7.0-xml php7.0-zip php7.0-gd php7.0-pdo php7.0-opcache php7.0-mysql php7.0-curl php7.0-cli php7.0-intl php7.0-mbstring \
        msmtp-mta && \ 
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY apache-security.conf /etc/apache2/conf-available/security.conf
COPY apache-site.conf     /etc/apache2/sites-available/000-default.conf
COPY apache-remoteip.conf        /etc/apache2/conf-enabled/sita-remoteip.conf

RUN /usr/sbin/a2enmod rewrite deflate expires headers php7.0 remoteip  && \
    echo GMT > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata && \
    ln -sf /dev/stdout /var/log/apache2/access.log && ln -sf /dev/stderr /var/log/apache2/error.log 

WORKDIR /var/www/html

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

EXPOSE 80
