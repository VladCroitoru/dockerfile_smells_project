# https://registry.hub.docker.com/u/phusion/baseimage/
FROM phusion/baseimage:0.9.16
MAINTAINER Chris Peters <chris.peters@liquifusion.com>

# base packages
RUN apt-get update -y && apt-get install -y wget nginx unzip

# install lucee
RUN LUCEE_VERSION="4.5.1.000" \
  && LUCEE_INSTALLER="lucee-$LUCEE_VERSION-pl0-linux-x64-installer.run" \
  && wget -O /tmp/$LUCEE_INSTALLER http://railo.viviotech.net/downloader.cfm/id/133/file/$LUCEE_INSTALLER \
  && chmod -R 744 /tmp/$LUCEE_INSTALLER \
  && /tmp/$LUCEE_INSTALLER --mode unattended --installconn false --installiis false --railopass 0tEb1-2oLf3-4Inch5-6uC7-8muD9 \
  && rm -rf /tmp/$LUCEE_INSTALLER

# make web root
RUN mkdir /var/www
# copy entire contents of app directories into webroot
ADD app/ /var/www/

# nginx config
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/cfwheels-rewrite-rules /etc/nginx/cfwheels-rewrite-rules
COPY nginx/proxy-params /etc/nginx/proxy-params
COPY nginx/default /etc/nginx/sites-enabled/default

# tomcat/lucee config
COPY lucee/web.xml /opt/lucee/tomcat/conf/web.xml
COPY lucee/server.xml /opt/lucee/tomcat/conf/server.xml

# start script
ADD scripts/start.sh /start.sh
RUN chmod +x /start.sh
