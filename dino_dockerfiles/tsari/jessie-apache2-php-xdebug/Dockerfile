# First docker test, so this is a all in one docker file
FROM tsari/jessie-apache2-php
MAINTAINER Tibor Sári <tiborsari@gmx.de>

ENV DEBIAN_FRONTEND noninteractive

# update, install and clean up to minimize the image size
RUN \
    apt-get update -qq && \
    apt-get install --no-install-recommends -y \
        php7.0-xdebug \
        openssh-server \
        supervisor \
    && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# use our own xdebug configuration
COPY 20-xdebug.ini /etc/php/7.0/apache2/conf.d/20-xdebug.ini
RUN sed -i -e '1izend_extension=\'`find / -name "xdebug.so"` /etc/php/7.0/apache2/conf.d/20-xdebug.ini

# add an user for later ssh connection (remote phpunit)
# sshd configuration
RUN groupadd --system --gid=100022 docker && useradd --system --create-home --gid=100022 --uid=100022 -p '*' docker

RUN mkdir /var/run/sshd
COPY ssh/sshd_config /etc/ssh/sshd_config
COPY ssh/docker-insecure-rsa.public.key /home/docker/docker-insecure-rsa.public.key

RUN mkdir -p /home/docker/.ssh && \
    cat /home/docker/docker-insecure-rsa.public.key > /home/docker/.ssh/authorized_keys2 && \
    chown -R docker:docker /home/docker

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]