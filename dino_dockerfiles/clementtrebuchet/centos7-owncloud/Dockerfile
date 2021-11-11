

#Owncloud 8.0.2 On CentOS 7 

From centos:latest
MAINTAINER C.TREBUCHET

#General variable definition for generation ssl scription keys
ENV C FR
ENV ST MIDI-PYRENEENS
ENV L TOULOUSE
ENV O dockerapp.tk
ENV OU dockerApp LAB
ENV CN main.dockerapp.tk

COPY nginx_ssl.conf /etc/nginx_ssl.conf
ADD initApp.sh /initApp.sh
#Install Nginx PHP-FPM wget tar unzip
RUN yum install -y http://rpms.famillecollet.com/enterprise/remi-release-7.rpm
RUN yum clean all
RUN yum install -y  tar wget unzip nginx php-fpm php-cli php-gd php-mcrypt php-mysql php-pear php-xml bzip2; yum clean all
RUN chmod +x /initApp.sh
#Get Owncloud version 8.02 https://download.owncloud.org/ extract it in /usr/share/nginx/
RUN if [[ ! -d /usr/share/nginx/ ]]; then mkdir -p /usr/share/nginx/ ; fi ;
RUN wget https://download.owncloud.org/community/owncloud-8.0.2.tar.bz2
RUN tar xfv owncloud-8.0.2.tar.bz2 -C /usr/share/nginx/
RUN chown -R nginx:nginx /usr/share/nginx/owncloud
RUN rm -f owncloud-8.0.2.tar.bz2
#Set user and group to nginx           
RUN sed -i 's/user = apache/user = nginx/' /etc/php-fpm.d/www.conf
RUN sed -i 's/group = apache/group = nginx/' /etc/php-fpm.d/www.conf
RUN if [[ ! -d /var/lib/php/session ]]; then mkdir -p /var/lib/php/session ; fi ;
RUN chown nginx:nginx /var/lib/php/session/
#Set volume for users data
RUN mkdir -p /datastore; chown nginx:nginx /datastore
#create Volume for the data for owncloud
VOLUME /datastore

EXPOSE 443
EXPOSE 80
CMD ["/initApp.sh"]
