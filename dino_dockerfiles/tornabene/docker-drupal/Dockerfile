FROM ubuntu:trusty
MAINTAINER Tindaro Tornabene <tindaro.tornabene@gmail.com>

# Install packages
RUN apt-get update && \
 DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
 DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor pwgen && \
 apt-get -y install git apache2 libapache2-mod-php5 php5-mysql php5-pgsql php5-gd php-pear php-apc curl && \
 curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin && \
 mv /usr/local/bin/composer.phar /usr/local/bin/composer

# Enable apache rewrite module
RUN a2enmod rewrite

# Add image configuration and scripts
ADD start.sh /start.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf

# Configure /app folder
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html

# Install packages
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
  DEBIAN_FRONTEND=noninteractive apt-get -y install supervisor pwgen && \
  apt-get -y install mysql-client && \
  apt-get -y install postgresql-client &&\
  apt-get install -y curl git drush
  
  
RUN apt-get -y install openssh-server && mkdir /var/run/sshd

# Download v7.32 of Drupal into /app
RUN rm -fr /app && mkdir /app && cd /app && \
  curl -O http://ftp.drupal.org/files/projects/drupal-7.32.tar.gz && \
  tar -xzvf drupal-7.32.tar.gz && \
  rm drupal-7.32.tar.gz && \
  mv drupal-7.32/* drupal-7.32/.htaccess ./ && \
  mv drupal-7.32/.gitignore ./ && \
  rmdir drupal-7.32

#Config and set permissions for setting.php
RUN cp app/sites/default/default.settings.php app/sites/default/settings.php && \
    chmod a+w app/sites/default/settings.php && \
    chmod a+w app/sites/default


RUN echo 'root:ntipa' |chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

EXPOSE 80
EXPOSE 22

CMD ["/run.sh"]

