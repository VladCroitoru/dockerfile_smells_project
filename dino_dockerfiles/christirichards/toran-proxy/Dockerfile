FROM christirichards/ubuntu:latest
MAINTAINER christi@christirichards.com

# Avoid ERROR: invoke-rc.d: policy-rc.d denied execution of start.
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d

# Install Supervisor
RUN apt-get update -qq \
    && apt-get install -qqy \
    supervisor

# Install SSH
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update -qq \
    && apt-get install -qqy \
    ssh

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update \
    && apt-get install -y \
    language-pack-en-base \
    && export LC_ALL=en_US.UTF-8 \
    && export LANG=en_US.UTF-8

RUN DEBIAN_FRONTEND=noninteractive \
    apt-get update \
    && apt-get install -y \
    software-properties-common

# Install PHP 7 Repository
RUN DEBIAN_FRONTEND=noninteractive \
    LC_ALL=en_US.UTF-8 \
    add-apt-repository ppa:ondrej/php -y \
    && apt-get update

# Install PHP and Nginx
RUN DEBIAN_FRONTEND=noninteractive LC_ALL=en_US.UTF-8 \
    && apt-get update -qq \
    && apt-get install -qqy \
        git \
        apt-transport-https \
        daemontools \
        php7.0 \
        php7.0-fpm \
        php7.0-json \
        php7.0-cli \
        php7.0-intl \
        php7.0-curl \
        php7.0-xml \
        nginx \
        libapache2-mod-php7.0 \
        apache2-utils

# Configure PHP and Nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Toran Proxy Version
ENV TORAN_PROXY_VERSION 1.5.3

# Download Toran Proxy
RUN curl -sL https://toranproxy.com/releases/toran-proxy-v${TORAN_PROXY_VERSION}.tgz | tar xzC /tmp \
    && mv /tmp/toran /var/www

# Load Scripts bash for Installing Toran Proxy
COPY scripts /scripts/toran-proxy/
RUN chmod -R u+x /scripts/toran-proxy

# Load Binaries
COPY bin /bin/toran-proxy/
RUN chmod -R u+x /bin/toran-proxy
ENV PATH $PATH:/bin/toran-proxy

# Load Assets
COPY assets/supervisor/conf.d /etc/supervisor/conf.d
COPY assets/supervisor/supervisord.conf /etc/supervisor/supervisord.conf
COPY assets/vhosts /etc/nginx/sites-available
COPY assets/config /assets/config

# Clean Up
RUN rm -rf /var/lib/apt/lists/*

VOLUME /data/toran-proxy

EXPOSE 80
EXPOSE 443

CMD /scripts/toran-proxy/launch.sh
