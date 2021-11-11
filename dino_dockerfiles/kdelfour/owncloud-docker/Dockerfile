# ------------------------------------------------------------------------------
# Based on a work at https://github.com/docker/docker.
# ------------------------------------------------------------------------------
# Pull base image.
FROM kdelfour/supervisor-docker
MAINTAINER Kevin Delfour <kevin@delfour.eu>

# ------------------------------------------------------------------------------
# Install base
RUN apt-get update
RUN apt-get install -y bzip2 wget apache2 sendmail smbclient \
  fontconfig-config fonts-dejavu-core ghostscript gsfonts imagemagick-common \
  libapache2-mod-php5 libcupsfilters1 libcupsimage2 libfftw3-double3 \
  libfontconfig1 libfreetype6 libgd3 libgs9 libgs9-common libicu52 libijs-0.35 \
  libjasper1 libjbig0 libjbig2dec0 libjpeg-turbo8 libjpeg8 liblcms2-2 \
  liblqr-1-0 libltdl7 libmagickcore5 libmagickwand5 libmcrypt4 libopts25 \
  libpaper-utils libpaper1 libpq5 libtiff5 libvpx1 libxpm4 lsof ntp \
  php-pear php-xml-parser php5 php5-cli php5-common php5-curl php5-gd \
  php5-imagick php5-intl php5-json php5-mcrypt php5-mysqlnd php5-pgsql \
  php5-readline php5-sqlite poppler-data psmisc ttf-dejavu-core curl \
  libc6 libcurl3 zlib1g

RUN update-rc.d sendmail defaults

# ------------------------------------------------------------------------------
# Install Owncloud
RUN curl -k http://download.owncloud.org/community/owncloud-8.1.1.tar.bz2 | tar jx -C /var/www/
RUN mkdir /var/www/owncloud/data
RUN chown -R www-data:www-data /var/www/owncloud
RUN chmod -R 770 /var/www/owncloud/data

# ------------------------------------------------------------------------------
# Make some changes
RUN cp /etc/php5/cli/php.ini /etc/php5/php.ini
RUN sed -i 's/^;\?\(post_max_size =\).*$/\1 4G/' /etc/php5/php.ini && \
  sed -i 's/^;\?\(upload_max_filesize =\).*$/\1 4G/' /etc/php5/php.ini && \
  sed -i 's/^;\?\(output_buffering =\).*$/\1 Off/' /etc/php5/php.ini && \
  sed -i 's/^;\?\(default_charset =\).*$/\1 "UTF-8"/' /etc/php5/php.ini
RUN sed -i -e "s:;\s*session.save_path\s*=\s*\"N;/path\":session.save_path = /tmp:g" /etc/php5/php.ini

WORKDIR /etc/php5/cli
RUN rm -f php.ini
RUN ln -s ../php.ini php.ini

WORKDIR /etc/php5/apache2
RUN rm -f php.ini
RUN ln -s ../php.ini php.ini

RUN chown -R www-data:www-data /tmp

RUN php5enmod mcrypt

RUN sed -i 's/AllowOverride None/AllowOverride All/'  /etc/apache2/apache2.conf
RUN sed -i -e"s/html/owncloud/" /etc/apache2/sites-available/000-default.conf
RUN sed -i -e"s/html/owncloud/" /etc/apache2/sites-available/default-ssl.conf
RUN a2enmod ssl
RUN a2ensite default-ssl

# ------------------------------------------------------------------------------
# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# ------------------------------------------------------------------------------
# Expose port & volumes
WORKDIR /
RUN ln -s /var/www/owncloud/data data
VOLUME /data

EXPOSE 80
EXPOSE 443

# ------------------------------------------------------------------------------
# Add supervisord conf
ADD conf/startup.conf /etc/supervisor/conf.d/

# ------------------------------------------------------------------------------
# Start supervisor, define default command.
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]
