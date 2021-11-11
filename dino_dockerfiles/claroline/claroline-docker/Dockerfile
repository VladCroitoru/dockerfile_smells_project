FROM ubuntu:16.04

MAINTAINER Donovan Tengblad

# Install packages
ENV DEBIAN_FRONTEND noninteractive

RUN echo "mysql-server-5.6 mysql-server/root_password password root" | debconf-set-selections
RUN echo "mysql-server-5.6 mysql-server/root_password_again password root" | debconf-set-selections

RUN apt-get update && apt-get install -y \
  supervisor \
  vim \
  git \
  wget \
  curl \
  apache2 \
  unzip \
  zip \
  wkhtmltopdf \
  xz-utils \
  php-zip \
  mysql-client \
  mysql-server \
  xfonts-75dpi \
  libav-tools \
  php \
  libapache2-mod-php \
  libav-tools \
  php-xml \
  php-mcrypt \
  php-mysql \
  php-curl \
  php-intl \
  php-gd \
  npm \
  apache2-utils \
  php-mbstring \
  php-gettext

RUN npm cache clean -f \
  && npm install -g n \
  && n 5.11.1

RUN a2enmod rewrite

WORKDIR /var/www/html
RUN rm index.html

RUN git clone http://github.com/claroline/Claroline claroline

COPY files/claroline/parameters.yml /var/www/html/claroline/app/config/
COPY files/apache2/claroline.conf /etc/apache2/sites-available/

WORKDIR /var/www/html/claroline
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
RUN php composer-setup.php
RUN php -r "unlink('composer-setup.php');"
RUN mv composer.phar /usr/local/bin/composer
# This needs to be a tag, once the repo is tagged
# RUN git checkout 7.x
RUN mkdir -p /var/run/mysqld && chown mysql:mysql /var/run/mysqld
RUN /bin/bash -c "/usr/bin/mysqld_safe &" && sleep 5 && echo "create database claroline" | mysql -u root -proot
RUN /bin/bash -c "/usr/bin/mysqld_safe &" && sleep 5 && composer sync
RUN chmod -R 777 /var/www/html/claroline/app/cache /var/www/html/claroline/app/logs /var/www/html/claroline/app/config /var/www/html/claroline/app/sessions /var/www/html/claroline/files /var/www/html/claroline/web/uploads
RUN a2dissite 000-default && a2ensite claroline.conf

#increase de file upload limite to 20M
RUN sed -i -- 's/upload_max_filesize = 2M/upload_max_filesize = 20M/g' /etc/php/7.0/apache2/php.ini
RUN sed -i -- 's/post_max_size = 8M/post_max_size = 20M/g' /etc/php/7.0/apache2/php.ini

# Install supervisor to allow starting mutliple processes
RUN        mkdir -p /var/log/supervisord && \
           mkdir -p /etc/supervisor/conf.d

# Add supervisor configuration
ADD        files/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN wget http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-generic-amd64.tar.xz
RUN tar -xf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz

RUN mv wkhtmltox/bin/wkhtmltopdf /usr/bin/wkhtmltopdf.sh
RUN mv wkhtmltox/bin/wkhtmltoimage /usr/bin/wkhtmltoimage.sh
RUN rm -r wkhtmltox

COPY files/bootstrap.sh /usr/local/bin/bootstrap.sh
RUN chmod +x /usr/local/bin/bootstrap.sh

EXPOSE 80

CMD ["/usr/bin/supervisord"]
