FROM 1and1internet/ubuntu-16:latest
MAINTAINER brian.wojtczak@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files /
RUN \
    apt-get update && \
    apt-get install -y software-properties-common python-software-properties && \
    add-apt-repository -y -u ppa:ondrej/php && \
    apt-get update && \
    apt-get install -y php7.1-cli php7.1-fpm php7.1-common php7.1-curl php7.1-gd php7.1-mysql php7.1-sqlite3 php7.1-soap php7.1-xml php7.1-zip php7.1-gettext php7.1-mbstring php7.1-mcrypt php7.1-intl php7.1-imap imagemagick php-imagick graphicsmagick && \
    mkdir /tmp/composer/ && \
    cd /tmp/composer && \
    curl -sS https://getcomposer.org/installer | php && \
    mv composer.phar /usr/local/bin/composer && \
    chmod a+x /usr/local/bin/composer && \
    cd / && \
    rm -rf /tmp/composer && \
    apt-get autoremove -y
