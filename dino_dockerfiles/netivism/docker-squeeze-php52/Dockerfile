FROM debian:squeeze
MAINTAINER Fuyuan Cheng <gloomcheng@netivism.com.tw>

# Use lenny repository for PHP 5.2.17.
RUN echo "" > /etc/apt/sources.list
RUN echo "deb http://archive.debian.org/debian squeeze main contrib non-free" >> /etc/apt/sources.list
RUN echo "deb http://archive.debian.org/debian lenny main contrib non-free" >> /etc/apt/sources.list
ADD container/apt/lenny /etc/apt/preferences.d/
RUN apt-get update \
    && apt-get install -y \
        apache2 \
        libapache2-mod-php5 \
        php5-common \
        php5-curl \
        php5-gd \
        php5-mcrypt \
        php5-mysql \
        php5-curl \
        php5-cli \
        curl \
        lynx-cur \
        vim \
        git-core \
        wget && \
  a2enmod php5 && a2enmod rewrite && \
  rm -f /etc/apache2/sites-enabled/000-default && \
  git clone https://github.com/NETivism/docker-sh.git /home/docker

### Apache
# remove default enabled site
RUN \
  mkdir -p /var/www/html/log/supervisor && \
  rm -f /etc/apache2/sites-enabled/000-default && \
  a2enmod php5 && a2enmod rewrite && \ 
  rm -f /etc/apache2/conf.d/security.conf && \
  rm -f /etc/apache2/conf.d/security && \
  ln -s /home/docker/apache/netivism.conf /etc/apache2/conf.d/ && \
  ln -s /home/docker/php/default52.ini /etc/php5/apache2/conf.d/ && \
  sed -i 's/KeepAlive[ ]*On*/KeepAlive Off/g' /etc/apache2/apache2.conf && \
  sed -i 's/StartServers[ ]*[0-9]*/StartServers 1/g' /etc/apache2/apache2.conf && \
  sed -i 's/MinSpareServers[ ]*[0-9]*/MinSpareServers 1/g' /etc/apache2/apache2.conf && \
  sed -i 's/MaxSpareServers[ ]*[0-9]*/MaxSpareServers 2/g' /etc/apache2/apache2.conf && \
  sed -i 's/MaxClients[ ]*[0-9]*/MaxClients 10/g' /etc/apache2/apache2.conf

ENV \
  APACHE_RUN_USER=www-data \
  APACHE_RUN_GROUP=www-data \
  APACHE_LOG_DIR=/var/log/apache2 \
  APACHE_LOCK_DIR=/var/lock/apache2 \
  APACHE_PID_FILE=/var/run/apache2.pid

### MySQL
# Install MySQL server and client.
RUN apt-get install -y \
     mysql-server \
     mysql-client \
     supervisor \
     rsyslog \
     procps && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

### DRUSH
RUN wget --quiet -O - https://github.com/drush-ops/drush/archive/5.11.0.tar.gz | tar -zxf - -C /usr/local/share
RUN ln -s /usr/local/share/drush-5.11.0/drush /usr/local/bin/drush

ADD container/apache/security.conf /etc/apache2/conf.d/security.conf
ADD container/supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD container/rsyslogd/rsyslog.conf /etc/rsyslog.conf

### 
WORKDIR /var/www/html
CMD ["/usr/bin/supervisord"]
