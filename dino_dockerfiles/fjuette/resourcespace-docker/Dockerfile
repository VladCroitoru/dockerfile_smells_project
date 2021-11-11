FROM phusion/baseimage:0.11
LABEL maintainer="Fabian Juette <fabian.juette@tu-clausthal.de>"

ENV DEBIAN_FRONTEND noninteractive


EXPOSE 80

# Install basic system
RUN apt-get update && apt-get install -y \
software-properties-common
RUN add-apt-repository ppa:ondrej/php
RUN apt-get update && apt-get install -y \
apache2 \
php7.2-gd \
php7.2-mysql \
php7.2-dev \
php7.2-dom \
php7.2-ldap \
php-mbstring \
php-zip \
libapache2-mod-php \
subversion \
imagemagick \
ghostscript \
antiword \
xpdf \
ffmpeg \
postfix \
libimage-exiftool-perl \
cron \
wget \
mysql-client

# Configure apache
ADD rs-config.conf /etc/apache2/sites-available/000-default.conf

# Configure php.ini
RUN cp -a /etc/php/7.2/apache2/php.ini /etc/php/7.2/apache2/php.ini-original
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 1G/g" /etc/php/7.2/apache2/php.ini
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 1G/g" /etc/php/7.2/apache2/php.ini
RUN sed -i -e "s/max_execution_time\s*=\s*30/max_execution_time = 1000/g" /etc/php/7.2/apache2/php.ini
RUN sed -i -e "s/memory_limit\s*=\s*128M/memory_limit = 1G/g" /etc/php/7.2/apache2/php.ini

# Install resourcespace
WORKDIR /var/www
RUN mkdir resourcespace \
&& cd resourcespace \
&& svn co https://svn.resourcespace.com/svn/rs/releases/8.6 . \
&& mkdir filestore \
&& chmod 777 filestore \
&& chmod -R 777 include

# Set cron job
ADD resourcespace /etc/cron.daily/resourcespace

ADD init.sh /etc/service/apache2/run
RUN chmod a+x /etc/service/apache2/run

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*