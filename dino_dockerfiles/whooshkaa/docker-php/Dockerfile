FROM ubuntu:16.04
MAINTAINER Phil Dodd "phil@whooshkaa.com"
ENV REFRESHED_AT 2019-12-19

# avoid debconf and initrd
ENV DEBIAN_FRONTEND noninteractive
ENV INITRD No

# Install all dependencies: PHP, Apache, eyed3, extra repositories,
# waveform generator dependencies, image compression tools, s3fuse
# supervisor, filebeat, AWS cli
RUN apt-get update && apt-get install -y --allow-downgrades \
--allow-remove-essential --allow-change-held-packages \
--allow-unauthenticated \
apache2 php php-mysql php-mcrypt \
php-curl php-zip php-gd php-imagick php-xml cron libapache2-mod-php wget eyed3 \
php-mbstring php7.0-mbstring php-gettext \
software-properties-common git-core make cmake gcc g++ libmad0-dev libsndfile1-dev \
libgd2-xpm-dev libboost-filesystem-dev libboost-program-options-dev libboost-regex-dev \
advancecomp pngcrush gifsicle jpegoptim libjpeg8-dbg \
libimage-exiftool-perl imagemagick pngnq libpng-dev pngquant optipng libjpeg-turbo-progs \
libav-tools \
automake autotools-dev git libcurl4-gnutls-dev libfuse-dev libssl-dev libxml2-dev pkg-config \
apt-transport-https \
python-pip supervisor \
libid3tag0-dev

# SN: Removed ffmpeg from repo as the PPA was not available any more
#     and it was not being used.

# Remove any unused packages
RUN apt-get autoremove -y

# SN: Removed audio waveform generator as it is not being used any more.

# s3fuse
RUN git clone https://github.com/s3fs-fuse/s3fs-fuse.git \
&& cd s3fs-fuse && ./autogen.sh && ./configure && make && make install \
&& cd / && rm -rf s3fs-fuse

# Python and aws cli to copy things from s3
RUN pip install awscli

#supervisord
RUN mkdir -p /var/log/supervisor

#supervisor config
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/supervisor

#apache env vars
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid
ENV APACHE_RUN_DIR /var/run/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2

#apache modules and config
RUN a2enmod rewrite
RUN a2enmod expires
ADD apache/000-default.conf /etc/apache2/sites-available/000-default.conf

#php config
#RUN rm -rf /etc/php5/apache2/conf.d
RUN rm /etc/php/7.0/apache2/php.ini
ADD php/php.ini /etc/php/7.0/apache2/php.ini


EXPOSE 80
CMD ["/usr/bin/supervisord"]

