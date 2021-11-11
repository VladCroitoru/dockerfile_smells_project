FROM nhenderson/nginx-php5fpm-supervisor:latest
MAINTAINER Nathan Henderson <nate908@gmail.com>

# Add PHP 5.5 debugger config file
ADD dbg_php_5_5.ini /etc/php5/mods-available/dbg_php_5_5.ini

# Add PHP 5.5 debugger module
ADD dbg-php-5.5.so /usr/lib/php5/20121212/dbg-php-5.5.so

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" > /etc/apt/sources.list; \

# Install dependencies
  apt-get update && apt-get install -y \
  wget mcrypt php5-cli php5-mcrypt curl git \
  mysql-client php5-mysql; \

# Enable PHP 5.5 debugger
  php5enmod dbg_php_5_5; \

# Laravel requirements
  curl -sS https://getcomposer.org/installer | php && \
  mv composer.phar /usr/bin/composer; \

# Enable the mcyrpt module for php
  php5enmod mcrypt; \

# Install composer and PHPUnit
  bash -c "wget http://getcomposer.org/composer.phar && chmod +x composer.phar && mv composer.phar /usr/local/bin/composer"; \
  bash -c "wget https://phar.phpunit.de/phpunit.phar && chmod +x phpunit.phar && mv phpunit.phar /usr/local/bin/phpunit"; \
  
# Change file ownership and permissions for the vhosts directory
  mkdir /var/www/vhosts && chown www-data:www-data /var/www/vhosts; \

# Install Orchestra via composer
  composer create-project orchestra/platform /var/www/vhosts/orchestra 2.2.x --prefer-dist; \

# Update file ownership and permissions for the orchestra directory
  chown -R www-data:www-data /var/www/vhosts/orchestra && \
  chmod -R 775 /var/www/vhosts/orchestra/app/storage; \

# We need to set security.limit_extensions to FALSE in www.conf to fix an access denied message from nginx. 
# For more info see: http://stackoverflow.com/a/23393266
   sed -i -e '/;security.limit_extensions = .php .php3 .php4 .php5/ s/;security.limit_extensions = .php .php3 .php4 .php5/security.limit_extensions = FALSE/' /etc/php5/fpm/pool.d/www.conf; \

# Edit some Laravel settings 
# Change the default timezone
  sed -i -e '/UTC/ s/UTC/America\/New_York/' /var/www/vhosts/orchestra/app/config/app.php; \
# Change the default url
  sed -i -e '/http:\/\/localhost/ s/http:\/\/localhost/http:\/\/localhost:8080/' /var/www/vhosts/orchestra/app/config/app.php; \

# Clean up
  apt-get remove -y --purge openssh-client && apt-get autoremove -y && apt-get clean; \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Add config files
ADD ./nginx-site.conf /etc/nginx/sites-enabled/default

# Initialization and Startup Script
ADD ./start.sh /start.sh
RUN chmod 755 /start.sh

# private expose. Port 7869 is used for PHP debugger.
EXPOSE 80 7869

CMD ["/bin/bash", "/start.sh"]
