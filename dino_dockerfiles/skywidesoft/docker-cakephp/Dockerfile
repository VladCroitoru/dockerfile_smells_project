FROM tutum/lamp:latest
MAINTAINER Clarence Ho <clarence@skywidesoft.com>

RUN apt-get update && \
  	apt-get -y install php5-gd php5-imagick php5-mcrypt php5-imap php5-memcache php5-curl \
                       imagemagick graphicsmagick && \
    php5enmod mcrypt imap

# Download latest version of CakePHP into /app
RUN rm -fr /app

# Configure Wordpress to connect to local DB
#ADD database.php /app/app/Config/database.php

# Modify permissions to allow plugin upload
#RUN mkdir /app/app/tmp
#RUN chmod -R 777 /app/app/tmp

# Add database setup script
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh
RUN chmod 755 /*.sh

EXPOSE 80 3306
CMD ["/run.sh"]
