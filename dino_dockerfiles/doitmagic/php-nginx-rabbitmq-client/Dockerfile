FROM ubuntu:trusty

LABEL maintainer="Doitmagic <razvan@doitmagic.com>"

ENV DEBIAN_FRONTEND noninteractive
ENV RABBITMQ_C_VER 0.8.0

# add NGINX official stable repository
RUN echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/nginx.list \
# add PHP7 unofficial repository (https://launchpad.net/~ondrej/+archive/ubuntu/php)
&& echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/php.list \
# install packages
&& apt-get update && \
    apt-get -y --force-yes --no-install-recommends install \   
    supervisor \
    curl \
    wget \
    cmake \
    nginx \
    zip \
    unzip \
    git \
    gcc make autoconf libc-dev \
    pkg-config librabbitmq-dev libmagickwand-dev  libmcrypt-dev libpng-dev zlib1g-dev\
    php7.0-fpm php7.0-cli php7.0-common php7.0-curl php7.0-intl php7.0-json php7.0-mbstring php7.0-mcrypt php7.0-mysql php7.0-opcache \
    php7.0-bcmath  php7.0-soap php7.0-xml php-xml php7.0-xmlrpc php7.0-xsl php7.0-zip php7.0-gd php7.0-dev  php-amqp php-pear php-dev \
    && update-alternatives --set php /usr/bin/php7.0 \
    # Install the composer
    && curl -sS http://getcomposer.org/installer | php -- --install-dir=/usr/bin/ --filename=composer \
    && chmod +x /usr/bin/composer \
    && echo "daemon off;" >> /etc/nginx/nginx.conf && sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.0/fpm/php-fpm.conf \
    && git clone git://github.com/alanxz/rabbitmq-c.git \
    && cd rabbitmq-c \
    && mkdir build && cd build \
    && cmake -DENABLE_SSL_SUPPORT=OFF .. \
    && cmake --build . --target install  \
    && cp -r /usr/local/lib/x86_64-linux-gnu/* /usr/lib/ \
    && pecl install amqp imagick xdebug \
    && apt-get autoclean && apt-get -y autoremove    

# copy config file for Supervisor
COPY config/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf 
COPY config/nginx/default /etc/nginx/sites-available/default

RUN touch /etc/php/7.0/fpm/conf.d/uploads.ini \
    && echo "upload_max_filesize = 20M;" >> /etc/php/7.0/fpm/conf.d/uploads.ini 

# php7.0-fpm will not start if this directory does not exist
RUN mkdir /run/php && echo extension=amqp.so > /etc/php/7.0/mods-available/amqp.ini && echo extension=bcmath.so > /etc/php/7.0/mods-available/bcmath.ini \
    && phpenmod amqp && phpenmod bcmath && phpenmod xdebug && service php7.0-fpm restart

# NGINX mountable directories for config and logs
VOLUME ["/var/www","/etc/nginx/sites-enabled","/etc/nginx/sites-available", "/etc/nginx/certs", "/etc/nginx/conf.d", "/var/log/nginx"]

WORKDIR /var/www
# NGINX ports
EXPOSE 80 443

CMD ["/usr/bin/supervisord"]
