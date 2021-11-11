FROM netivism/docker-wheezy-mariadb 
MAINTAINER Jimmy Huang <jimmy@netivism.com.tw>

ENV \
  APACHE_RUN_USER=www-data \
  APACHE_RUN_GROUP=www-data \
  APACHE_LOG_DIR=/var/log/apache2 \
  APACHE_LOCK_DIR=/var/lock/apache2 \
  APACHE_PID_FILE=/var/run/apache2.pid \
  COMPOSER_HOME=/root/.composer \
  PATH=/root/.composer/vendor/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

WORKDIR /etc/apt/sources.list.d
RUN echo "deb http://packages.dotdeb.org wheezy all" > dotdeb.list \
    && echo "deb-src http://packages.dotdeb.org wheezy all" >> dotdeb.list \
    && echo "deb http://packages.dotdeb.org wheezy-php55 all" >> dotdeb.list \
    && echo "deb-src http://packages.dotdeb.org wheezy-php55 all" >> dotdeb.list \
    && apt-get update && apt-get install -y wget && wget http://www.dotdeb.org/dotdeb.gpg \
    && apt-key add dotdeb.gpg && \
    rm -f dotdeb.gpg

WORKDIR /
RUN \
  apt-get update && \
  apt-get install -y \
    rsyslog \
    apache2 \
    libapache2-mod-php5 \
    php5-common \
    php5-curl \
    php5-gd \
    php5-mcrypt \
    php5-memcached \
    php5-mysql \
    php5-curl \
    php5-cli \
    php5-imap \
    curl \
    vim \
    git-core && \
  curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer && \
  composer global require drush/drush:7.0.0 && \
  git clone https://github.com/NETivism/docker-sh.git /home/docker

### Apache
# remove default enabled site
RUN \
  rm -f /etc/apache2/sites-enabled/000-default && \
  a2enmod php5 && a2enmod rewrite && \ 
  rm -f /etc/apache2/conf.d/security.conf && \
  rm -f /etc/apache2/conf.d/security && \
  cp -f /home/docker/apache/netivism.conf /etc/apache2/conf.d/ && \
  cp -f /home/docker/php/default55.ini /etc/php5/docker_setup.ini && \
  ln -s /etc/php5/docker_setup.ini /etc/php5/apache2/conf.d/ && \
  cp -f /home/docker/php/default55_cli.ini /etc/php5/cli/conf.d/ && \
  cp -f /home/docker/php/default_opcache_blacklist /etc/php5/opcache_blacklist && \
  mkdir -p /var/www/html/log/supervisor && \
  sed -i 's/KeepAlive[ ]*On*/KeepAlive Off/g' /etc/apache2/apache2.conf && \
  sed -i 's/StartServers[ ]*[0-9]*/StartServers 1/g' /etc/apache2/apache2.conf && \
  sed -i 's/MinSpareServers[ ]*[0-9]*/MinSpareServers 1/g' /etc/apache2/apache2.conf && \
  sed -i 's/MaxSpareServers[ ]*[0-9]*/MaxSpareServers 2/g' /etc/apache2/apache2.conf && \
  sed -i 's/MaxClients[ ]*[0-9]*/MaxClients 8/g' /etc/apache2/apache2.conf

RUN apt-get install -y supervisor

# wkhtmltopdf
RUN \
  apt-get install -y fonts-droid fontconfig libfontconfig1 libfreetype6 libpng12-0 libjpeg8 libssl1.0.0 libx11-6 libxext6 libxrender1 xfonts-75dpi xfonts-base && \
  cd /tmp && \
  wget -nv https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz -O wkhtmltox.tar.xz && \
  tar xf wkhtmltox.tar.xz && \
  rm -f wkhtmltox.tar.xz && \
  mv wkhtmltox/bin/wkhtmlto* /usr/local/bin/ && \
  apt-get clean && rm -rf /tmp/wkhtmltox

# Update certificates
RUN sed -i "s/^mozilla\/AddTrust_External_Root.crt/!mozilla\/AddTrust_External_Root.crt/" /etc/ca-certificates.conf
RUN update-ca-certificates

ADD container/apache/security.conf /etc/apache2/conf.d/security.conf
ADD container/supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD container/mysql/mysql-init.sh /usr/local/bin/mysql-init.sh
ADD container/rsyslogd/rsyslog.conf /etc/rsyslog.conf

### END
WORKDIR /var/www/html
CMD ["/usr/bin/supervisord"]
