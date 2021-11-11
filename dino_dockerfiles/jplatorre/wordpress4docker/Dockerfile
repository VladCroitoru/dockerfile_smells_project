FROM wordpress:4.8.0-php5.6-apache

# Install PDO-MySQL
# Activate extension
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install php5-mysql -y && \
    apt-get clean -y && \
    apt-get autoremove -y

# Activate the PHP extension we need
# See http://php.net/manual/en/ref.pdo-mysql.php
RUN { \
              echo 'extension=/usr/lib/php5/20131226/pdo.so'; \
              echo 'extension=/usr/lib/php5/20131226/pdo_mysql.so'; \
       } > /usr/local/etc/php/conf.d/pdo-mysql.ini

# RUN a2enmod rewrite expires
