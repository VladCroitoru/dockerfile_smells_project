# Use stratolinux/baseimage-docker
FROM stratolinux/baseimage-docker:0.9.19

# ports needed
EXPOSE 80

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# install the PHP extensions we need
RUN apt-get update && apt-get install -y \
    apache2 \
    git \
    php \
    libpng12-dev \
    libjpeg-dev \
    zlib1g-dev \
		php-gd \
    php-zip \
    php-mbstring \
    wget \
    unzip \
    libapache2-mod-php \
    php-curl \
    php-xml

# enable apache mods
RUN a2enmod rewrite expires

ENV GRAV_VERSION 1.1.15
RUN cd /root && \
    wget https://getgrav.org/download/core/grav-admin/${GRAV_VERSION} -O grav-admin.zip && \
    rm -rf /var/www/html/*


COPY etc/ /etc/

RUN find /etc/service -name run -exec chmod +x {} \;
RUN chmod +x /etc/my_init.d/setup_grav

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
