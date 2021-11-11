FROM ubuntu:16.04
MAINTAINER Vikash Kumar <vikash.iitb@gmail.com>

# Update and upgrade
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y vim unzip wget curl

# Install PHP
RUN apt-get install -y \
    php7.0 \
    php7.0-cli \
    php7.0-mbstring \ 
    php7.0-zip \
    php7.0-dom \
    php7.0-curl \
    php7.0-mysql \
    composer

# Install Apache
RUN apt-get install -y apache2 libapache2-mod-php7.0
RUN a2enmod rewrite

# Install MySQL
RUN echo 'mysql-server mysql-server/root_password password password' | debconf-set-selections
RUN echo 'mysql-server mysql-server/root_password_again password password' | debconf-set-selections
RUN apt-get install -y mysql-client mysql-server

# Install Redis
RUN apt-get install -y redis-server
RUN apt-get install -y php-redis

# Install Node
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install --yes nodejs

# Copy configurations
WORKDIR /var/www/application
COPY apache.config /etc/apache2/sites-available/000-default.conf
COPY index.php /var/www/application/public/
COPY start.sh /usr/bin/

# Install Selenium
RUN mkdir /root/selenium/
ADD https://selenium-release.storage.googleapis.com/3.4/selenium-server-standalone-3.4.0.jar /root/selenium/
ADD https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz /root/selenium/geckodriver-linux64.tar.gz
RUN cd /root/selenium; tar -xvzf geckodriver-linux64.tar.gz; rm geckodriver-linux64.tar.gz
RUN apt-get install -y firefox xvfb default-jdk

# Install AWS cli for deployements
RUN apt-get install -y awscli

# Expose apache and mysql ports
EXPOSE 80
EXPOSE 3306
EXPOSE 6379

CMD ["/usr/bin/start.sh"]
