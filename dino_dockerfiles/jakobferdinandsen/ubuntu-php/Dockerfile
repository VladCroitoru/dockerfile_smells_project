FROM ubuntu:xenial
LABEL maintainer="jakob@jhaaf.dk"

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
RUN apt-get update \
    && apt-get install --no-install-recommends -y -q  \
        software-properties-common \
        python-software-properties \
    && LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php \
    && apt-get update \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
RUN apt-get update \
    && apt-get install --no-install-recommends -y -q  \
        php7.2-fpm \
    && apt-get -y clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
RUN sed -i -e "s/^error_log =/;error_log =/" /etc/php/7.2/fpm/php-fpm.conf && \
    sed -i -e "s/;daemonize = yes/daemonize = no/" /etc/php/7.2/fpm/php-fpm.conf && \
    sed -i -e "/^;error_log =/ a \
error_log = /proc/self/fd/2 " /etc/php/7.2/fpm/php-fpm.conf

RUN mkdir -p /run/php/ && \
    touch /run/php/php7.2-fpm.sock
    
CMD ["php-fpm7.2", "--nodaemonize", "--fpm-config", "/etc/php/7.2/fpm/php-fpm.conf"]

WORKDIR /var/www
