FROM ubuntu:16.04

# set env vars
ENV container docker
ENV LC_ALL C.UTF-8
ENV COMPOSER_VERSION=1.6.3 \
    COMPOSER_HOME=/composer \
    PATH=$COMPOSER_HOME/vendor/bin:$PATH

#set build vars
ARG DEBIAN_FRONTEND=noninteractive

# configure apt behaviour
RUN echo "APT::Get::Install-Recommends 'false'; \n\
  APT::Get::Install-Suggests 'false'; \n\
  APT::Get::Assume-Yes "true"; \n\
  APT::Get::force-yes "true";" > /etc/apt/apt.conf.d/00-general

# systemd tweaks
RUN rm -rf /lib/systemd/system/getty*;

# install
RUN apt-get update && apt-get install -yq apt-utils

# install typical requirements for testing
RUN apt-get install -yq \
    apt-transport-https \
    build-essential expect \
    ca-certificates \
    curl \
    git \
    gnupg2 \
    iproute \
    net-tools \
    pinentry-tty \
    procps \
    python \
    rpm \
    ruby-dev \
    software-properties-common \
    ssl-cert \
    sudo \
    syslog-ng \
    unzip \
    vim \
    wget

# add current php repository
RUN add-apt-repository ppa:ondrej/php -y
RUN apt-get update

# install php
RUN apt-get install -yq \
    php \
    php-common \
    php-curl \
    php-gd \
    php-imap \
    php-intl \
    php-mbstring \
    php-mcrypt \
    php-mysql \
    php-xml

# install composer + parallel install plugin
COPY install-composer.sh /usr/local/bin/install-composer.sh
RUN mkdir -p $COMPOSER_HOME \
    && ( install-composer.sh && rm /usr/local/bin/install-composer.sh ) \
    && export COMPOSER_ALLOW_SUPERUSER=1 \
    && composer global require -a --prefer-dist "hirak/prestissimo:^0.3" \
    && export COMPOSER_ALLOW_SUPERUSER=0 \
    && chmod -R 0777 $COMPOSER_HOME/cache \
    && rm -Rf /var/cache/apk/* \
    && rm -Rf $COMPOSER_HOME/cache/*

# install fpm
RUN apt-get install -yq libffi-dev
RUN gem install fpm --no-ri --no-rdoc

# install ghr
RUN wget -O /tmp/ghr.zip https://github.com/tcnksm/ghr/releases/download/v0.5.4/ghr_v0.5.4_linux_amd64.zip && (cd /usr/local/bin && unzip /tmp/ghr.zip) && chmod +x /usr/local/bin/ghr

# cleanup
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# finally run script on startup
CMD ["/bin/bash"]
