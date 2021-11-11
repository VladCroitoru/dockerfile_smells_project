FROM phusion/baseimage:0.9.17

MAINTAINER Jacob Kiers <jacob@alphacomm.nl>

CMD ["/sbin/my_init"]

ENV DEBIAN_FRONTEND=noninteractive

# Enable php5.6 repository
RUN echo "deb http://ppa.launchpad.net/ondrej/php5-5.6/ubuntu trusty main" > /etc/apt/sources.list.d/ondrej-php5-5_6-trusty.list && \
    apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C

# Install php5
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
        ca-certificates \
        curl \
        git \
        libzmq3 \
        memcached \
        php5-cli \
        php5-curl \
        php5-mcrypt \
        php5-memcached \
        php5-mysqlnd

RUN curl -O http://archive.ubuntu.com/ubuntu/pool/universe/p/php-zmq/php5-zmq_1.1.2-1build1_amd64.deb && \
    dpkg -i php5-zmq_1.1.2-1build1_amd64.deb && \
    rm php5-zmq_1.1.2-1build1_amd64.deb

# Install composer
RUN curl https://getcomposer.org/composer.phar -o /usr/local/bin/composer && \
    chmod +x /usr/local/bin/composer

# Add user alpharpc and change workdir
RUN /usr/sbin/useradd -m alpharpc
WORKDIR /home/alpharpc/alpharpc

# Add init files and services
COPY docker/init/ /etc/my_init.d/
COPY docker/services/ /etc/service/

RUN git clone https://github.com/alphacomm/alpharpc.git . && \
    composer install --no-dev --optimize-autoloader && \
    chown -R alpharpc:alpharpc . && \
    ln -s /home/alpharpc/alpharpc/bin/alpharpc /usr/bin/alpharpc

COPY docker/config /home/alpharpc/alpharpc/app/config

EXPOSE 61002 61003
