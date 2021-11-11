# Use phusion/baseimage as base image. To make your builds reproducible, make
# sure you lock down to a specific version, not to `latest`!
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for
# a list of version numbers.
FROM phusion/baseimage
EXPOSE 80

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

ENV PHP_UPLOAD_MAX_FILESIZE=512M
ENV PHP_POST_MAX_SIZE=512M

RUN apt-get update
RUN apt-get -o Dpkg::Options::="--force-confold" -y install \
         php7.0 php7.0-zip php7.0-mbstring php7.0-mysql php7.0-gd php7.0-imap php7.0-xml
RUN apt-get -o Dpkg::Options::="--force-confold" -y install \
         apache2 libapache2-mod-php7.0
RUN apt-get -o Dpkg::Options::="--force-confold" -y install bzip2
RUN apt-get -o Dpkg::Options::="--force-confold" -y install php7.0-pgsql
# RUN ufw allow 'Apache'

RUN sed -ri -e "s/^upload_max_filesize.*/upload_max_filesize = ${PHP_UPLOAD_MAX_FILESIZE}/" \
    -e "s/^post_max_size.*/post_max_size = ${PHP_POST_MAX_SIZE}/" /etc/php/7.0/cli/php.ini


COPY limesurvey.tar.bz2 /
RUN tar xvjf /limesurvey.tar.bz2
RUN rm /limesurvey.tar.bz2
RUN rm -rf /var/www/html
RUN mv /limesurvey /var/www/html
RUN chown -R www-data:www-data /var/www/html
### RUN chown -R www-data:www-data /var/lib/php/modules

COPY apache.service /etc/service/apache/run

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
