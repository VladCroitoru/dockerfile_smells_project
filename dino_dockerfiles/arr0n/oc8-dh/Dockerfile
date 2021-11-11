FROM ubuntu:latest
MAINTAINER arr0n <afinnon@gmail.com>

# Setting timezome
RUN echo "Europe/Berlin" | tee /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

# making sure i have nano and wget 
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y nano wget

# installing owncloud 
RUN cd /tmp/ && \
    wget http://download.opensuse.org/repositories/isv:ownCloud:community/xUbuntu_14.04/Release.key && \
    apt-key add - < Release.key && \
    sh -c "echo 'deb http://download.opensuse.org/repositories/isv:/ownCloud:/community/xUbuntu_14.04/ /' >> /etc/apt/sources.list.d/owncloud.list" && \
    apt-get update && \
    apt-get install -y owncloud && \
    chown -hR www-data:www-data /var/www/owncloud/ && \
    apt-get install -y php5-ldap php5-intl php5-curl php5-gd php5-json php5-curl php5-intl php5-mcrypt php5-imagick && \
    apt-get install -y libreOffice

# sed owncloud location    
RUN sed -i 's_DocumentRoot /var/www/html_DocumentRoot /var/www/owncloud_' /etc/apache2/sites-enabled/000-default.conf 
RUN sed -i 's_DocumentRoot /var/www/html_DocumentRoot /var/www/owncloud_' /etc/apache2/sites-available/default-ssl.conf

RUN a2enmod rewrite && \
    a2enmod headers && \
    a2enmod ssl && \
    a2ensite default-ssl.conf

VOLUME ["/var/www/owncloud/data/"]

EXPOSE 80 443

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
