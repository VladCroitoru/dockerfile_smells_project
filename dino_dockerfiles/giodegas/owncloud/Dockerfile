FROM        debian:wheezy

MAINTAINER  Giovanni De Gasperis <giovanni@giodegas.it>

RUN         apt-get update && apt-get -y install curl bzip2 g++ libgettextpo0 gettext file

ADD         https://download.owncloud.org/community/owncloud-7.0.2.tar.bz2 /var/www/
ADD         bootstrap.sh /usr/bin/
ADD         nginx_ssl.conf /root/
ADD         nginx.conf /root/

RUN         DEBIAN_FRONTEND=noninteractive apt-get install -y php5-cli php5-gd php5-pgsql php5-sqlite php5-mysqlnd php5-curl php5-intl php5-mcrypt php5-ldap php5-gmp php5-imagick php5-fpm smbclient nginx
RUN         mkdir /var/www/owncloud && mkdir /var/www/owncloud/data && \
            chown -R www-data:www-data /var/www/owncloud
            chmod +x /usr/bin/bootstrap.sh

ADD         php.ini /etc/php5/fpm/

EXPOSE      80
EXPOSE      443

ENTRYPOINT  ["bootstrap.sh"]
