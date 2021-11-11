FROM 1and1internet/ubuntu-16-nginx-php-7.2:latest
MAINTAINER brian.wilkinson@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive

COPY files/ /

RUN \
  rm /var/www/html/index.html && \
  curl --location https://www.phpmyadmin.net/downloads/phpMyAdmin-latest-all-languages.tar.gz | tar xzf - && \
  mv phpMyAdmin*/* /var/www/html/ && \
  rm -rf /var/www/html/js/jquery/src/ /var/www/html/examples /var/www/html/po/ && \
  chmod 777 /var/www/html && \
  chmod 755 /hooks /var/www /hooks/supervisord-pre.d/40_phpmyadmin_config_secret  && \
  sed -i "s|; max_input_vars = 1000|max_input_vars = 3000|" /etc/php/7.2/fpm/php.ini

ENV PHP_UPLOAD_MAX_FILESIZE=64M  \
    PHP_MAX_INPUT_VARS=2000      \
    PMA_ARBITRARY=1              \
    PMA_HOST=localhost           \
    PMA_PORT=3306                \
    PMA_HOSTS=""                 \
    PMA_ABSOLUTE_URI=""          \
    PMA_CONTROL_HOST=localhost   \
    PMA_CONTROL_PORT=3306        \
    PMA_CONTROL_USER=pma         \
    PMA_CONTROL_PASSWORD=pma

# variables explained:
#   PMA_ARBITRARY - when set to 1 connection to the arbitrary server will be allowed
#   PMA_HOST - define address/host name of the MySQL server
#   PMA_PORT - define port of the MySQL server
#   PMA_HOSTS - define comma separated list of address/host names of the MySQL servers
#   PMA_ABSOLUTE_URI - define user-facing URI
#   PHP_UPLOAD_MAX_FILESIZE - define upload_max_filesize and post_max_size PHP settings
#   PHP_MAX_INPUT_VARS - define max_input_vars PHP setting

EXPOSE 8080
