FROM dockenizer/php7-fpm
MAINTAINER Jacques Moati <jacques@moati.net>

RUN apk --update \
        --repository http://dl-3.alpinelinux.org/alpine/v3.6/main/ \
        --repository http://dl-3.alpinelinux.org/alpine/v3.6/community/ \
        add mysql-client make g++ autoconf nano htop supervisor sudo nodejs git openssh zsh make redis yarn && \
    pecl install xdebug && \
    apk del --purge make g++ autoconf libtool && \
    rm -rf /var/cache/apk/* && \
    mkdir /etc/supervisor.d/ && \
    echo "www-data ALL=(ALL:ALL) NOPASSWD: ALL" | (EDITOR="tee -a" visudo) && \
    rm -rf /var/cache/apk/*

RUN cd /tmp && \
    php -r "readfile('https://getcomposer.org/installer');" | php && \
    mv composer.phar /usr/local/bin/composer

USER www-data
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"; exit 0
USER root

ADD squire /usr/local/bin/squire

VOLUME /var/www
VOLUME /etc/supervisor.d

WORKDIR /home/www-data

COPY docker-entrypoint.sh /docker-entrypoint.sh
COPY docker-root-entrypoint.sh /docker-root-entrypoint.sh

RUN chmod +x /docker-entrypoint.sh
RUN chmod +x /docker-root-entrypoint.sh

ADD run.sh /run.sh
RUN chmod +x /run.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD /run.sh
