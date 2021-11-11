FROM ubuntu:14.04

# setup workdir
RUN mkdir /data
WORKDIR /data

# environment for osticket
ENV OSTICKET_VERSION 1.9.12
ENV HOME /data

# requirements
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -y install \
  nano \
  wget \
  unzip \
  msmtp \
  ca-certificates \
  supervisor \
  nginx \
  php5-cli \
  php5-fpm \
  php5-imap \
  php5-gd \
  php5-curl \
  php5-mysql && \
  rm -rf /var/lib/apt/lists/*

# Download & install OSTicket
RUN wget -nv -O osTicket.zip http://osticket.com/sites/default/files/download/osTicket-v${OSTICKET_VERSION}.zip && \
    unzip osTicket.zip && \
    rm osTicket.zip && \
    chown -R www-data:www-data /data/upload/ && \
    mv /data/upload/setup /data/upload/setup_hidden && \
    chown -R root:root /data/upload/setup_hidden && \
    chmod 700 /data/upload/setup_hidden
    
# Download languages packs
RUN wget -nv -O upload/include/i18n/fr.phar http://osticket.com/sites/default/files/download/lang/fr.phar && \
    wget -nv -O upload/include/i18n/ar.phar http://osticket.com/sites/default/files/download/lang/ar.phar && \
    wget -nv -O upload/include/i18n/pt_BR.phar http://osticket.com/sites/default/files/download/lang/pt_BR.phar && \
    wget -nv -O upload/include/i18n/it.phar http://osticket.com/sites/default/files/download/lang/it.phar && \
    wget -nv -O upload/include/i18n/es_ES.phar http://osticket.com/sites/default/files/download/lang/es_ES.phar && \
    wget -nv -O upload/include/i18n/de.phar http://osticket.com/sites/default/files/download/lang/de.phar

# Configure nginx
RUN sed -i -e"s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf && \
    sed -i -e"s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf && \
    echo "daemon off;" >> /etc/nginx/nginx.conf

# Configure php-fpm & PHP5
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php5/fpm/php.ini && \
    sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" /etc/php5/fpm/php.ini && \
    sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" /etc/php5/fpm/php.ini && \
    sed -i -e 's#;sendmail_path\s*=\s*#sendmail_path = "/usr/bin/msmtp -C /etc/msmtp -t "#g' /etc/php5/fpm/php.ini && \
    sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf && \
    sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" /etc/php5/fpm/pool.d/www.conf && \
    php5enmod imap

# Add nginx site
ADD virtualhost /etc/nginx/sites-available/default
ADD supervisord.conf /data/supervisord.conf
ADD msmtp.conf /data/msmtp.conf
ADD bin/ /data/bin

VOLUME ["/data/upload/include/plugins","/var/log/nginx"]
EXPOSE 80
CMD ["/data/bin/start.sh"]
