FROM phusion/baseimage:0.9.18

MAINTAINER mnbf9rca

# /config - where we will put the DB
# /var/cache/zoneminder - events, images and temp
VOLUME ["/config", "/var/cache/zoneminder"]

EXPOSE 80

RUN export DEBCONF_NONINTERACTIVE_SEEN=true DEBIAN_FRONTEND=noninteractive && \
apt-get update && \
apt-get install -y \
software-properties-common \
python-software-properties && \
add-apt-repository -y ppa:iconnor/zoneminder-master && \
apt-get update && \
apt-get install -y \
wget \
apache2 \
mysql-server \
php5 \
php5-gd \
libapache2-mod-php5 \
usbutils && \
service apache2 restart  && \
sed -i '/\[mysqld\]/ainnodb_file_per_table\=1' /etc/mysql/my.cnf && \
service mysql restart && \
apt-get install -y \
zoneminder \
libvlc-dev \
libvlccore-dev \
vlc && \
sed -i 's/\;date\.timezone\ \=/date\.timezone\ \=\ Europe\/London/g' /etc/php5/cli/php.ini && \
sed -i 's/\;date\.timezone\ \=/date\.timezone\ \=\ Europe\/London/g' /etc/php5/apache2/php.ini && \
a2enmod cgi && \
a2enmod rewrite && \
a2enconf zoneminder && \
service apache2 restart && \
service mysql restart && \
adduser www-data video && \
service apache2 restart && \
chmod 775 /etc/zm/zm.conf

# add my startup script & clean up APT when done.
ADD startup.sh /etc/my_init.d/startup.sh
# ADD atboot.sh /etc/my_init.d/atboot.sh

RUN chmod +x /etc/my_init.d/startup.sh && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

