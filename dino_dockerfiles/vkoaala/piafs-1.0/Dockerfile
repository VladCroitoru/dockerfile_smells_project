FROM ubuntu:16.04

ENV HOME /root

RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get dist-upgrade -y \
    && apt-get install apache2 libapache2-mod-php7.0 -y

ADD apache.sh /apache.sh
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_SERVER_NAME **NONE**

RUN apt-get update && \
    apt-get install -y php7.0-mysql php7.0-gd imagemagick wget unzip mediainfo ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    wget -q -O piafs.zip https://github.com/linuq/PIAFS/archive/master.zip && \
    unzip piafs.zip && \
    mv PIAFS-master/src/* /var/www/html && \
    chown -R www-data:www-data /var/www/html && \
    rm -r piafs* && \
	chmod +x /apache.sh && \
    rm /var/www/html/index.html

VOLUME ["/var/www/html/galleries", "/var/www/html/themes", "/var/www/html/plugins", "/var/www/html/local"]

EXPOSE 80
CMD ["/apache.sh"]
