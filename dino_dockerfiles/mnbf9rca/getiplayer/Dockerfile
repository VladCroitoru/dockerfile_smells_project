FROM phusion/baseimage:0.9.19

MAINTAINER mnbf9rca

# /output = location of downloaded files
# /tmp for transcoding? not sure
# /var/www/get_iplayer/.get_iplayer --> profile directory, including PVR searches and cache
# /etc/get_iplayer --> options file stored here
VOLUME ["/output", "/tmp", "/var/www/get_iplayer/.get_iplayer", "/etc/get_iplayer"]

EXPOSE 80

#apache configuration to serve get_iplayer.cgi at /iplayer
ADD getiplayer.conf /root/getiplayer.conf
COPY startup.sh /etc/my_init.d/startup.sh

ENV DEBCONF_NONINTERACTIVE_SEEN=true DEBIAN_FRONTEND=noninteractive TERM="xterm" LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8"

RUN apt-get update && \
apt-get install -y \
software-properties-common \
python-software-properties && \
add-apt-repository -y ppa:jon-hedgerows/get-iplayer && \
apt-get update && \
apt-get install -y \
apache2 \
atomicparsley \
ffmpeg \
get-iplayer \
libcgi-fast-perl \
libjson-pp-perl \
libproc-background-perl \
php \
php-cgi \
rsync \
rtmpdump \
wget && \
mkdir -p /var/www/get_iplayer/output /var/www/get_iplayer/.get_iplayer /var/www/get_iplayer/.get_iplayer/pvr/ && \
chown www-data:www-data /var/www/get_iplayer/output /var/www/get_iplayer/.get_iplayer && \
ln -s /root/.get_iplayer/pvr /var/www/get_iplayer/.get_iplayer/pvr && \
ln -s /usr/bin/get_iplayer /var/www/get_iplayer/ && \
ln -s /usr/share/get_iplayer/get_iplayer.cgi /var/www/get_iplayer/ && \
sed -i '/packagemanager apt/d' /etc/get_iplayer/options && \
sed -i '$ aoutput \/output/incomplete' /etc/get_iplayer/options && \
cp /root/getiplayer.conf /etc/apache2/conf-available/getiplayer.conf && \
sed -i '/\<VirtualHost \*\:80\>/aInclude /etc/apache2/conf-available/getiplayer.conf\n' /etc/apache2/sites-available/000-default.conf && \
a2enmod cgi && \
service apache2 restart && \
crontab -l | { cat; echo "57 0,6,12,18 * * * timed-process 21600 /var/www/get_iplayer/get_iplayer --profile-dir /var/www/get_iplayer/.get_iplayer --hash --type=radio,tv --fps50 --modes=tvbest,radiobest --output=/output/incomplete --pvr --nopurge --tag-format-title=\"<name> <episode>\" --file-prefix=\"<nameshort> <senum> <descshort>\"" \$GIP_OPTIONS; } | crontab - && \
crontab -l | { cat; echo "0 10 * * * timed-process 300 /var/www/get_iplayer/get_iplayer --profile-dir /var/www/get_iplayer/.get_iplayer --update --plugins-update"; } | crontab - && \
crontab -l | { cat; echo "@hourly rsync --recursive --remove-source-files --exclude=*.partial.* /output/incomplete/*.mp3 /output/mp3/ #copy MP3s"; } | crontab - && \
crontab -l | { cat; echo "@hourly rsync --recursive --remove-source-files --exclude=*.partial.* /output/incomplete/*.m4a /output/mp3/ #copy MP3s"; } | crontab - && \
crontab -l | { cat; echo "@hourly rsync --recursive --remove-source-files --exclude=*.partial.* /output/incomplete/*.mp4 /output/tv/ #move tv"; } | crontab - && \
crontab -l | { cat; echo "@hourly timed-process 900 /var/www/get_iplayer/get_iplayer --profile-dir /var/www/get_iplayer/.get_iplayer --refresh --refresh-future --type=all --nopurge   #refresh get_iplayer cache"; } | crontab - && \
chmod +x /etc/my_init.d/startup.sh


# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]D

