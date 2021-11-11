
FROM debian:latest
MAINTAINER Maksim Koldaev <mail@koldaev.com>

RUN mkdir /soft

ADD ./testdobroin.tar.gz /soft/testdobroin.tar.gz

# Install
RUN  \
        apt-get update && \
DEBIAN_FRONTEND=noninteractive apt-get install -y nginx \
    php5-fpm php5-mysql php5-imagick php5-mcrypt php5-gd mysql-server

ADD ./my.cnf /etc/mysql/my.cnf
	
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini
ADD nginx.conf /etc/nginx/nginx.conf
ADD https://raw.github.com/h5bp/server-configs-nginx/master/h5bp/location/expires.conf /etc/nginx/conf/expires.conf
ADD nginx-site.conf /etc/nginx/sites-available/default
RUN sed -i -e '/access_log/d' /etc/nginx/conf/expires.conf
RUN sed -i -e 's/^listen =.*/listen = \/var\/run\/php5-fpm.sock/' /etc/php5/fpm/pool.d/www.conf

# Install MySQL.

RUN \
  rm -rf /var/lib/apt/lists/* && \
  sed -i 's/^\(bind-address\s.*\)/# \1/' /etc/mysql/my.cnf && \
  sed -i 's/^\(log_error\s.*\)/# \1/' /etc/mysql/my.cnf && \
  echo "mysqld_safe &" > /tmp/config && \
  echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \
  echo "mysqladmin create testdobroin || exit 1" >> /tmp/config && \
  echo "mysql testdobroin < /soft/testdobroin.tar.gz/testdobroin.sql  || exit 1" >> /tmp/config && \
  echo "mysqlcheck --check-upgrade --all-databases --auto-repair -u root  || exit 1" >> /tmp/config && \
  echo "mysql_upgrade --force -u root -p || exit 1" >> /tmp/config && \
  echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" WITH GRANT OPTION;'" >> /tmp/config && \
  bash /tmp/config && \
  rm -f /tmp/config

VOLUME ["/etc/mysql", "/var/lib/mysql"]

# Define working directory.
VOLUME ["/data"]

EXPOSE 80

EXPOSE 3306

ADD start.sh /start.sh
ADD ./data /data
RUN chmod +x /start.sh
ENTRYPOINT ["/start.sh"]

