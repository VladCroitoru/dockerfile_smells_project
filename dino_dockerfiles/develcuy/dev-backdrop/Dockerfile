#
# Dockerfile for Backdrop (Apache+PHP7 only)
#
# version: 0.1.0
#

FROM ubuntu:16.04
MAINTAINER Fernando Paredes Garcia <fernando@develcuy.com>

# Update packages
RUN apt-get update
RUN apt-get dist-upgrade -y

# Install package dependencies
RUN apt-get install -y supervisor vim make less git curl unzip mysql-client

# Install Apache
RUN apt-get install -y apache2

# Configure Apache
RUN echo '[supervisord]\n\
nodaemon=true\n\
\n\
[program:apache2]\n\
command=/usr/bin/pidproxy /var/run/apache2/apache2.pid /bin/bash -c "source /etc/apache2/envvars && /usr/sbin/apache2 -DFOREGROUND"\n\
redirect_stderr=true\n'\
>> /etc/supervisor/conf.d/supervisord.conf
RUN mkdir /var/run/apache2 /var/lock/apache2 && chown www-data: /var/lock/apache2 /var/run/apache2
RUN echo '<VirtualHost *:80>\n\
\n\
        ServerAdmin webmaster@localhost\n\
\n\
        DocumentRoot /var/www\n\
        <Directory />\n\
                Options FollowSymLinks\n\
                AllowOverride None\n\
        </Directory>\n\
        <Directory /var/www/>\n\
                Options Indexes FollowSymLinks MultiViews\n\
                AllowOverride All\n\
                Order allow,deny\n\
                allow from all\n\
        </Directory>\n\
\n\
        ErrorLog ${APACHE_LOG_DIR}/error.log\n\
        CustomLog ${APACHE_LOG_DIR}/access.log combined\n\
\n\
</VirtualHost>'\
> /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite vhost_alias
RUN service apache2 restart
VOLUME ["/var/www/"]
EXPOSE 80 443

# Install PHP7
RUN apt-get install -y php php-curl php-mysql php-xmlrpc php-soap php-gd php-mbstring php7.0-xml php-cli libapache2-mod-php7.0

# Configure PHP7
RUN \
  sed -i "s/\(max_execution_time *= *\).*/\160/" /etc/php/7.0/apache2/php.ini;\
  sed -i "s/\(display_errors *= *\).*/\1On/" /etc/php/7.0/apache2/php.ini;\
  sed -i "s/\(display_startup_errors *= *\).*/\1Off/" /etc/php/7.0/apache2/php.ini;\
  sed -i "s/\(html_errors *= *\).*/\1On/" /etc/php/7.0/apache2/php.ini;\
  sed -i "s/\(post_max_size *= *\).*/\120M/" /etc/php/7.0/apache2/php.ini;\
  sed -i "s/\(upload_max_filesize *= *\).*/\120M/" /etc/php/7.0/apache2/php.ini;\
  sed -i "s/\(\;date.timezone *= *\).*/date.timezone\"America\\\Lima\"/" /etc/php/7.0/apache2/php.ini;\
  sed -i "s/\(memory_limit *= *\).*/\1512M/" /etc/php/7.0/apache2/php.ini

# Create deploy user
RUN mkdir /home/deploy; useradd deploy; chown deploy: /home/deploy

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer; ln -s /usr/local/bin/composer /usr/bin/composer

# Install Drush
RUN mkdir /usr/local/src/composer; chown :deploy /usr/local/src/composer; chmod g+w /usr/local/src/composer; su deploy -c "composer global require drush/drush -d /usr/local/src/composer/"
RUN su deploy -c "cd /usr/local/src/composer/vendor/drush/drush/commands; mkdir backdrop; cd backdrop; git clone https://github.com/backdrop-contrib/drush.git .; rm -rf .git"
RUN ln -s /usr/local/src/composer/vendor/drush/drush/drush /usr/local/bin/

WORKDIR /var/www

# Start supervisor
CMD ["/usr/bin/supervisord"]
