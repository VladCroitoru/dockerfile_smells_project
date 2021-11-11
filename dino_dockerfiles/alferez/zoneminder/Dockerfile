FROM debian:8
MAINTAINER Jose A Alferez <correo@alferez.es>


ENV DEBIAN_FRONTEND noninteractive

#### Configure TimeZone
RUN echo "Europe/Madrid" > /etc/timezone
RUN dpkg-reconfigure tzdata

#### Instalamos dependencias, Repositorios y Paquetes
RUN echo "deb http://httpredir.debian.org/debian jessie-backports main" >> /etc/apt/sources.list
RUN apt-get update -y --fix-missing
RUN apt-get -y upgrade

RUN apt-get install -y --fix-missing wget curl nano apache2 mysql-server php5 php5-mysql build-essential libmysqlclient-dev libssl-dev libbz2-dev libpcre3-dev libdbi-perl libarchive-zip-perl libdate-manip-perl libdevice-serialport-perl libmime-perl libpcre3 libwww-perl libdbd-mysql-perl libsys-mmap-perl yasm automake autoconf apache2-mpm-prefork libapache2-mod-php5 php5-cli libphp-serialization-perl libavcodec-dev libavformat-dev libswscale-dev libavutil-dev libv4l-dev libtool libnetpbm10-dev libavdevice-dev libmime-lite-perl dh-autoreconf dpatch vlc ntp ntpdate libvlc-dev libvlccore-dev zoneminder libapache2-mod-perl2

#### Configuramos Apache y MySQL
RUN chmod 740 /etc/zm/zm.conf
RUN chown root:www-data /etc/zm/zm.conf
RUN echo "innodb_file_per_table" >> /etc/mysql/my.cnf
RUN echo 'date.timezone = "Europe/Madrid"' >> /etc/php5/apache2/php.ini
RUN adduser www-data video
RUN a2enmod cgi
RUN a2enconf zoneminder
RUN a2enmod rewrite
RUN rm /var/www/html/index.html
ADD ./assets/index.html /var/www/html/index.html
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf
RUN ln -s /etc/apache2/conf-available/fqdn.conf /etc/apache2/conf-enabled/fqdn.conf



#### Creamos las tablas necesarias
RUN service mysql start &&\
	mysql -uroot < /usr/share/zoneminder/db/zm_create.sql &&\
	mysql -uroot -e "grant all on zm.* to 'zmuser'@localhost identified by 'zmpass';"

### Creamos los crons para el backup y la hora
RUN echo "*/15 * * * *	root mysqldump -uroot zm > /var/cache/zoneminder/backups/zm.sql" >> /etc/crontab
RUN echo "!/bin/sh ntpdate 0.ubuntu.pool.ntp.org" >> /etc/cron.daily/ntpdate
RUN chmod 750 /etc/cron.daily/ntpdate

### Instalacion de FFmpeg
RUN echo "" >> /etc/apt/sources.list
RUN echo "deb http://http.debian.net/debian jessie         contrib non-free" >> /etc/apt/sources.list
RUN echo "" >> /etc/apt/sources.list
RUN echo "deb http://http.debian.net/debian jessie-updates         contrib non-free" >> /etc/apt/sources.list
RUN echo "" >> /etc/apt/sources.list
RUN echo "deb http://security.debian.org/ jessie/updates    contrib non-free" >> /etc/apt/sources.list
RUN echo "" >> /etc/apt/sources.list
RUN echo "deb http://deb-multimedia.org jessie main non-free" >> /etc/apt/sources.list
RUN echo "" >> /etc/apt/sources.list
RUN echo "deb-src http://deb-multimedia.org jessie main non-free" >> /etc/apt/sources.list
RUN echo "" >> /etc/apt/sources.list
WORKDIR /tmp
RUN apt-get install -y wget

RUN wget https://www.deb-multimedia.org/pool/main/d/deb-multimedia-keyring/deb-multimedia-keyring_2016.3.7_all.deb
RUN dpkg -i deb-multimedia-keyring_2016.3.7_all.deb
RUN rm deb-multimedia-keyring_2016.3.7_all.deb


RUN apt-get update -y --fix-missing
RUN apt-get install -y -q build-essential git-core checkinstall yasm texi2html libvorbis-dev libx11-dev libvpx-dev libxfixes-dev zlib1g-dev pkg-config libx264-dev libfaac-dev libmp3lame-dev netcat

WORKDIR /usr/local/src
RUN wget "http://ffmpeg.org/releases/ffmpeg-2.8.6.tar.bz2"
RUN tar -xjf "ffmpeg-2.8.6.tar.bz2"
RUN rm "ffmpeg-2.8.6.tar.bz2"

WORKDIR /usr/local/src/ffmpeg-2.8.6
RUN ./configure --enable-version3 --enable-postproc --enable-libmp3lame --enable-libvorbis --enable-libvpx --enable-gpl --enable-libx264 --enable-nonfree --enable-libfaac
RUN make
RUN make install
#RUN checkinstall --pkgname=ffmpeg --pkgversion="5:2.8.6" --backup=no --deldoc=yes --default

RUN rm -R "/usr/local/src/ffmpeg-2.8.6"


### Instalamos cambozola
WORKDIR /usr/src
RUN wget http://www.andywilcock.com/code/cambozola/cambozola-latest.tar.gz
RUN tar zxvf cambozola-latest.tar.gz
RUN mv cambozola-*/dist/cambozola.jar /usr/share/zoneminder/www
RUN rm -rf cambozola*


### Limpiamos
RUN apt-get clean
RUN rm -rf /tmp/* /var/tmp/*
RUN rm -rf /var/lib/apt/lists/*

### Add Entrypoing
ADD ./assets/start.sh /start.sh
RUN chmod +x /start.sh

WORKDIR /root

ENTRYPOINT "/start.sh"


