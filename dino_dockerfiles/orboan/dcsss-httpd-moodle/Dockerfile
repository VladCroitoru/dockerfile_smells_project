FROM orboan/dcsss-httpd-php
MAINTAINER Oriol Boix Anfosso <dev@orboan.com>

RUN \
cd /var/www/ && \
mkdir moodledata && \
chmod -R 755 /var/www/moodledata && \
chown -R apache:apache /var/www/moodledata

RUN \ 
cd /var/www/html && \
wget https://download.moodle.org/stable32/moodle-3.2.tgz && \
tar -xvf moodle-3.2.tgz && \
mv /var/www/html/moodle/* /var/www/html/ && \
rm -rf /var/www/html/moodle && \
chown -R apache:apache /var/www/html && \
chmod -R 755 /var/www/html
#
# - Clean YUM caches to minimise Docker image size...
RUN \
  yum clean all && rm -rf /tmp/yum*

# default
ENV MYSQL_HOST=mysql
ENV MYSQL_DATABASE=moodle
ENV MYSQL_USER=vle_user
ENV MYSQL_PASSWORD=iaw
ENV MOODLE_URL=http://vle.iaw.io
ENV MOODLE_DATADIR=/var/www/moodledata

ENV USER=www
ENV PASSWORD=iaw

ADD container-files /
