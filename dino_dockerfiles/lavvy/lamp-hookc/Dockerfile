FROM ubuntu:trusty
MAINTAINER Fernando Mayo <fernando@tutum.co>, Feng Honglin <hfeng@tutum.co>

ENV VERSION 1.80
ENV AWSS3User AWSS3User
ENV AWSS3Secret AWSS3Secret
ENV BUCKETNAME mycloudbucketname
ENV MOUNTPOINT /app/file


# Install packages
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
  apt-get -y install supervisor git automake curl libtool build-essential tar libfuse-dev libcurl4-openssl-dev \
  libxml2-dev mime-support apache2 libapache2-mod-php5 mysql-server php5-mysql pwgen php-apc wget unzip php5-gd php5-mcrypt && \
  echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Add image configuration and scripts
ADD start-apache2.sh /start-apache2.sh
ADD start-mysqld.sh /start-mysqld.sh
ADD run.sh /run.sh
RUN chmod 755 /*.sh

ADD my.cnf /etc/mysql/conf.d/my.cnf
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf
#ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf

# Remove pre-installed database
RUN rm -rf /var/lib/mysql/*

# for s3fs ################################
RUN rm -rf /var/lib/apt/lists/*
RUN curl -L https://github.com/s3fs-fuse/s3fs-fuse/archive/v${VERSION}.tar.gz | tar zxv -C /usr/src
RUN cd /usr/src/s3fs-fuse-${VERSION} && ./autogen.sh && ./configure --prefix=/usr && make && make install
ADD s3fs.sh /root/s3fs.sh
RUN chmod +x /root/s3fs.sh
##############################################


# Add MySQL utils
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh
RUN chmod 755 /*.sh

# config to enable .htaccess
ADD apache_default /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite

# Configure /app folder with sample app
RUN git clone https://github.com/fermayo/hello-world-lamp.git /app
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html

#Enviornment variables to configure php
ENV PHP_UPLOAD_MAX_FILESIZE 10M
ENV PHP_POST_MAX_SIZE 10M
ENV SQLBUDDY_URL https://codeload.github.com/lavvy/sqlbuddy/tar.gz/v1.0.0
ENV HTTP_DOCUMENTROOT /app

# Add volumes for MySQL 
VOLUME  ["/etc/mysql", "/var/lib/mysql" ]

EXPOSE 80 3306
CMD ["/run.sh"]
