# ------------------------------------------------------------------------------
# Based on a work at https://github.com/docker/docker.
# Forked from kdelfour/lychee-docker
# ------------------------------------------------------------------------------
# Pull base image.
FROM phusion/baseimage:0.9.16
MAINTAINER Kevin Delfour <kevin@delfour.eu>

# ------------------------------------------------------------------------------
# Set Environment Variables
ENV HOME /root

# ------------------------------------------------------------------------------
# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# ------------------------------------------------------------------------------
# Install base
RUN apt-get update && apt-get dist-upgrade -y
RUN apt-get update && apt-get install -yq wget git unzip nginx fontconfig-config fonts-dejavu-core \
    php5-fpm php5-common php5-json php5-cli php5-common php5-mysql\
    php5-gd php5-json php5-mcrypt php5-readline php5-imagick psmisc ssl-cert \
    ufw php-pear libgd-tools libmcrypt-dev mcrypt mysql-client

# ------------------------------------------------------------------------------
# Install locales
ENV DEBIAN_FRONTEND noninteractive
RUN locale-gen cs_CZ.UTF-8
RUN locale-gen de_DE.UTF-8
RUN locale-gen es_ES.UTF-8
RUN locale-gen fr_FR.UTF-8
RUN locale-gen it_IT.UTF-8
RUN locale-gen pl_PL.UTF-8
RUN locale-gen pt_BR.UTF-8
RUN locale-gen ru_RU.UTF-8
RUN locale-gen sl_SI.UTF-8
RUN locale-gen uk_UA.UTF-8

# ------------------------------------------------------------------------------
# Configure php-fpm
RUN echo "cgi.fix_pathinfo = 0" >> /etc/php5/fpm/php.ini
RUN sed -i -e "s/output_buffering\s*=\s*4096/output_buffering = Off/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 1G/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 1G/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/max_execution_time\s*=\s*30/max_execution_time = 1000/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s/memory_limit\s*=\s*128M/memory_limit = 1G/g" /etc/php5/fpm/php.ini
RUN sed -i -e "s:;\s*session.save_path\s*=\s*\"N;/path\":session.save_path = /tmp:g" /etc/php5/fpm/php.ini
RUN chown -R www-data:www-data /tmp
RUN php5enmod mcrypt

# ------------------------------------------------------------------------------
# Configure nginx
RUN mkdir /var/www
RUN chown www-data:www-data /var/www
RUN rm /etc/nginx/sites-enabled/*
RUN rm /etc/nginx/sites-available/*
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf
RUN sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
ADD conf/php.conf /etc/nginx/
ADD conf/lychee /etc/nginx/sites-enabled/

# ------------------------------------------------------------------------------
# Install Lychee
WORKDIR /var/www
RUN git clone https://github.com/electerious/Lychee.git lychee
RUN chown -R www-data:www-data /var/www/lychee
RUN chmod -R 770 /var/www/lychee
RUN chmod -R 777 /var/www/lychee/uploads/
RUN chmod -R 777 /var/www/lychee/data/

# ------------------------------------------------------------------------------
# Configure Startup Items
RUN mkdir /etc/service/php5-fpm
COPY conf/php5-fpm.sh /etc/service/php5-fpm/run
RUN chmod a+x /etc/service/php5-fpm/run

RUN mkdir /etc/service/nginx
COPY conf/nginx.sh /etc/service/nginx/run
RUN chmod a+x /etc/service/nginx/run

# ------------------------------------------------------------------------------
# Expose ports.
EXPOSE 80

# ------------------------------------------------------------------------------
# Expose volumes
WORKDIR /
RUN ln -s /var/www/lychee/uploads uploads
RUN ln -s /var/www/lychee/data data
RUN ln -s /var/www/lychee/plugins plugins

VOLUME /uploads
VOLUME /data
VOLUME /plugins

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
