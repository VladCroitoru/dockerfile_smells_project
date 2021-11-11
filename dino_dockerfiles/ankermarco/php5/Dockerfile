FROM ubuntu:14.04

RUN apt-get update && apt-get install -y apache2

RUN rm -rf /var/www/html && mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/apache2 /var/www/html \
    && chown -R www-data:www-data /var/lock/apache2 /var/run/apache2 /var/log/apache2 /var/www/html

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
ENV APACHE_LOCK_DIR=/var/lock/apache2
ENV APACHE_PID_FILE=/var/run/apache2/apache2.pid
ENV APACHE_RUN_DIR=/var/run/apache2/
ENV APACHE_RUN_USER=www-data
ENV APACHE_RUN_GROUP=www-data
ENV APACHE_LOG_DIR=/var/log/apache2
#ENV APACHE_SERVER_NAME=mymagentostore.com

RUN a2enmod rewrite ssl

RUN apt-get update && apt-get install -y php5 libapache2-mod-php5

# Enable required php5 modules
RUN apt-get update && apt-get install -y php5-mcrypt php5-mysql php5-xsl php5-gd php5-intl php5-curl \
    && php5enmod mcrypt mysql xsl gd intl curl

# Add the Apache virtual host file
ADD config/apache_default_vhost /etc/apache2/sites-available/magento2.conf
ADD config/apache_default_vhost_ssl /etc/apache2/sites-available/ssl.conf
RUN rm -f /etc/apache2/sites-enabled/000-default.conf
RUN a2ensite magento2.conf
RUN a2ensite ssl.conf

# Copy SSL cert over
COPY ssl /etc/apache2/ssl/


COPY apache2-foreground /usr/local/bin/
RUN chmod +x /usr/local/bin/apache2-foreground
WORKDIR /var/www/html

# Install vim, nano, git, curl
RUN apt-get update && apt-get install -y vim nano git curl

# Install php-composer
RUN curl -sS https://getcomposer.org/installer | \
    php -- --filename=composer --install-dir=/usr/local/bin

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 80
EXPOSE 443
CMD ["apache2-foreground"]
