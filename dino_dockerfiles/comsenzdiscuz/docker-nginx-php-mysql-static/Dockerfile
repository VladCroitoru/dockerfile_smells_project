FROM ubuntu:16.04
MAINTAINER Robin Ostlund <me@robinostlund.name>

##################################################################
# avoid debconf and initrd
ENV DEBIAN_FRONTEND noninteractive
ENV INITRD No

##################################################################
# create folders
RUN mkdir -p /root/nginx

##################################################################
# install packages
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install apt-utils supervisor nginx php7.0-fpm php7.0-mysql pwgen python-setuptools curl git unzip cron anacron rsyslog memcached mysql-server mysql-client && \
    apt-get -y install php7.0-curl php7.0-gd php7.0-intl php-pear php-imagick php7.0-imap php7.0-mcrypt php-memcache php7.0-ps php7.0-pspell php7.0-recode php7.0-sqlite php7.0-tidy php7.0-xmlrpc php7.0-xsl && \
    apt-get clean && \
    rm -rf /var/lib/mysql && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    rm -f /etc/memcached.conf && \
    rm -rf /var/www && \

    # fix container bug for syslog, by disabling: emerg and imklog
    sed -i 's/\$KLogPermitNonKernelFacility/#$KLogPermitNonKernelFacility/g' /etc/rsyslog.conf && \
    sed -i "s|\*.emerg|\#\*.emerg|" /etc/rsyslog.conf && \
    sed -i 's/$ModLoad imklog/#$ModLoad imklog/' /etc/rsyslog.conf && \

    # modify nginx
    rm -f /etc/nginx/sites-enabled/* && \
    rm -rf /etc/nginx/ssl && \
    ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default && \
    sed -i 's/worker_processes auto;/worker_processes 2;/g' /etc/nginx/nginx.conf && \
    sed -i -e "s/keepalive_timeout\s*65/keepalive_timeout 2/" /etc/nginx/nginx.conf && \
    sed -i -e "s/keepalive_timeout 2/keepalive_timeout 2;\n\tclient_max_body_size 100m/" /etc/nginx/nginx.conf && \

    # modify mysql
    sed -e "s/^bind-address\(.*\)=.*/bind-address = 0.0.0.0/" -i /etc/mysql/mysql.conf.d/mysqld.cnf && \
    sed 's/datadir.*/datadir=\/data\/var\/lib\/mysql/g' -i /etc/mysql/mysql.conf.d/mysqld.cnf && \
    sed 's/password = .*/password = /g' -i /etc/mysql/debian.cnf && \
    sed 's/^log_error/# log_error/g' -i /etc/mysql/mysql.conf.d/mysqld.cnf && \
    echo "[mysqld]" > /etc/mysql/conf.d/mysql-skip-name-resolv.cnf && \
    echo "skip_name_resolve" >> /etc/mysql/conf.d/mysql-skip-name-resolv.cnf && \

    # modify php
    sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g" /etc/php/7.0/fpm/php.ini && \
    sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g" /etc/php/7.0/fpm/php.ini && \
    sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g" /etc/php/7.0/fpm/php.ini && \
    sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g" /etc/php/7.0/fpm/pool.d/www.conf && \
    find /etc/php/7.0/cli/conf.d/ -name "*.ini" -exec sed -i -re 's/^(\s*)#(.*)/\1;\2/g' {} \;


##################################################################
# copy files
COPY supervisord/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY scripts/* /usr/local/bin/
RUN chmod +x /usr/local/bin/*
COPY nginx/index.html /root/nginx/index.html
COPY nginx/site.conf /root/nginx/site.conf
COPY nginx/site-git.conf /root/nginx/site-git.conf
COPY nginx/phpinfo.php /root/nginx/phpinfo.php
COPY nginx/nginx.conf /root/nginx/nginx.conf
COPY nginx/logrotate /etc/logrotate.d/nginx

##################################################################
# ports
EXPOSE 3306
EXPOSE 80

##################################################################
# volumes
VOLUME /data

##################################################################
# specify healthcheck script
HEALTHCHECK CMD /usr/local/bin/healthcheck.sh || exit 1

CMD ["supervisord"]
