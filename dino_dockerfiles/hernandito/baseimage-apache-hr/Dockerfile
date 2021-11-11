FROM phusion/baseimage
MAINTAINER hernandito

# Set correct environment variables
ENV BASE_APTLIST="apache2-mpm-worker nano libapache2-mod-fastcgi openssl php5 php5-cli php5-curl php5-fpm libapache2-mod-php5 wget mc inotify-tools php5-gd php5-sqlite php5-mcrypt php5-tidy php5-mysql libapache2-mod-proxy-html" LANG="en_US.UTF-8" LANGUAGE="en_US:en" LC_ALL="en_US.UTF-8"

# Set the locale
RUN locale-gen en_US.UTF-8

# install main packages
RUN apt-get update -qy && \
apt-get install $BASE_APTLIST -qy && \

# cleanup 
apt-get clean -y && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# add some files 
ADD defaults/ /defaults/
ADD init/ /etc/my_init.d/
ADD services/ /etc/service/
RUN chmod -v +x /etc/service/*/run /etc/my_init.d/*.sh && \

# enable apache mods
cp /etc/apache2/ports.conf /defaults/ports.conf && \
mv /defaults/envvars /etc/apache2/envvars && \
mv /defaults/php5-fpm.conf /etc/apache2/conf-available/ && \ 
ln -s /etc/apache2/conf-available/php5-fpm.conf /etc/apache2/conf-enabled/ && \
sed -i "s/www-data/abc/g" /etc/php5/fpm/pool.d/www.conf && \
sed -i "s#/var/www#/config/www#g" /etc/apache2/apache2.conf && \
sed -i "s#IncludeOptional sites-enabled#IncludeOptional /config/apache/site-confs#g" /etc/apache2/apache2.conf && \
sed -i '/Include ports.conf/s/^/#/g' /etc/apache2/apache2.conf && \
echo "Include /config/apache/ports.conf"  >> /etc/apache2/apache2.conf && \
cp /etc/apache2/apache2.conf /defaults/apache2.conf && \
a2enmod actions rewrite fastcgi alias ssl

# expose ports
EXPOSE 80 443

# set volumes
VOLUME /config
