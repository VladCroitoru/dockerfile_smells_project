FROM debian:jessie
MAINTAINER Pavel Sterba <email@pavelsterba.com>

ENV DEBIAN_FRONTEND noninteractive

# Update & upgrade
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y curl pwgen vim

# Remove old PHP5
RUN apt-get purge php5-*

# Remove Apache
RUN apt-get remove -y apache2*
RUN rm -rf /etc/apache2

# Install nginx
RUN apt-get install -y nginx
COPY data/nginx.conf /etc/nginx/nginx.conf

# Add repository for PHP7
RUN echo 'deb http://packages.dotdeb.org jessie all' >> /etc/apt/sources.list
ADD https://www.dotdeb.org/dotdeb.gpg /tmp/dotdeb.gpg
RUN apt-key add /tmp/dotdeb.gpg
RUN rm -f /tmp/dotdeb.gpg
RUN apt-get update

# Install PHP7
RUN apt-get install -y php7.0-fpm php7.0-mysql php7.0-gd php7.0-curl php7.0-imagick php7.0-imap php7.0-mcrypt php7.0-xmlrpc
COPY data/www.conf /etc/php/7.0/fpm/pool.d

# Install MariaDB
RUN apt-get install -y mariadb-server mariadb-client
COPY data/my.cnf /etc/mysql/
VOLUME /var/lib/mysql

# Expose port 80
EXPOSE 80

# Add run script
ADD data/run.sh run.sh
RUN chmod +x run.sh

# Run it!
CMD /run.sh
