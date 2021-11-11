FROM debian:stretch-slim
MAINTAINER info@analogic.cz

ENV DEBIAN_FRONTEND noninteractive
ENV TERM=xterm

ADD https://github.com/just-containers/s6-overlay/releases/download/v1.21.4.0/s6-overlay-amd64.tar.gz /tmp/
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /
ENTRYPOINT ["/init"]

RUN apt-get update && apt-get -y upgrade

RUN apt-get install -y dirmngr wget apt-transport-https && \
    echo "deb https://packages.sury.org/php/ stretch main" > /etc/apt/sources.list.d/php.list && \
    wget -O - https://packages.sury.org/php/apt.gpg | apt-key add - && \
    apt-get update && \
    apt-get upgrade -y && \

    apt-get install -y --no-install-recommends --reinstall git \
            php7.4-fpm php7.4-cli php7.4-json php7.4-mysql php7.4-sqlite3 php7.4-curl php7.4-zip \
            php7.4-xml php7.4-imap php7.4-mbstring php7.4-mbstring php7.4-bcmath php7.4-soap \
            php7.4-intl php-apcu php-gd \
            nginx-light libnginx-mod-nchan ca-certificates sudo busybox-syslogd cron nano locales \
            ssmtp logrotate unzip && \

    sed 's/listen = \/run\/php\/php7.4-fpm\.sock/listen = \/var\/run\/php-fpm.sock/' -i /etc/php/7.4/fpm/pool.d/www.conf && \
    sed 's/pid = \/run\/php\/php7.4-fpm\.pid/pid = \/var\/run\/php-fpm.pid/' -i /etc/php/7.4/fpm/php-fpm.conf && \
    echo "expose_php = off" >> /etc/php/7.4/fpm/php.ini && \

    apt-get remove -y dirmngr wget apt-transport-https && apt-get autoremove -y

ADD rootfs /
EXPOSE 9000 80
