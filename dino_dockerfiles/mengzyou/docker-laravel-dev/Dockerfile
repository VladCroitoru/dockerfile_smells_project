# This is a Dockerfile for build a opensuse image for development based on laravel
FROM mengzyou/docker-php:5.6-apache-server
MAINTAINER Mengz You <mengz.you@outlook.com>

# Add repo, Refresh repositories and install packages
RUN zypper -q ar -f -r http://download.opensuse.org/repositories/server:/php:/extensions/openSUSE_13.2/server:php:extensions.repo \
  && zypper -qn --gpg-auto-import-keys ref \
  && zypper -qn in -l --no-recommends curl php5-mcrypt php5-openssl php5-phar php5-pdo \
  && zypper clean -a

# Install php-composer
COPY tools/composer /usr/local/bin/

# Configure the directory for app
RUN mkdir -p /srv/laravel \
  && chown -R wwwrun:www /srv/laravel

# Customize apache2 configuration
RUN sed -i -e 's#APACHE_CONF_INCLUDE_FILES=""#APACHE_CONF_INCLUDE_FILES="/etc/apache2/httpd.conf.local"#' /etc/sysconfig/apache2 \
  && sed -i -e 's#/srv/www/htdocs#/srv/laravel/public#' /etc/apache2/default-server.conf

ADD conf/httpd.conf.local /etc/apache2/httpd.conf.local

# Set Volume
VOLUME ["/srv/laravel"]

ENTRYPOINT ["start_apache2"]

# Expose ports
EXPOSE 80

# Start apache
CMD ["-DFOREGROUND"]
