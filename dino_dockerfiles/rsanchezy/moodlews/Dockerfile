FROM ubuntu:latest 
MAINTAINER Roger Sánchez <rsanchezy@gmail.com> 
#VOLUME ["/var/moodledata"]
EXPOSE 80 443 
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
apt -y install apache2 php7.0 libapache2-mod-php7.0 php7.0-pspell php7.0-curl php7.0-gd php7.0-intl php7.0-mysql php7.0-xmlrpc php7.0-ldap php7.0-xml php7.0-zip 
RUN apt -y install wget 
RUN wget https://download.moodle.org/moodle/moodle-latest.tgz
RUN tar xzvf moodle-latest.tgz -C /var/www/html
RUN sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 200M/g" /etc/php/7.0/apache2/php.ini && \
    sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 200M/g" /etc/php/7.0/apache2/php.ini && \
    sed -i -e "s/max_execution_time = 30/Max_execution_time = 600/g" /etc/php/7.0/apache2/php.ini
RUN a2enmod ssl && a2ensite default-ssl
RUN chown -R www-data /var/www/html
RUN mkdir /var/moodledata
RUN chown -R www-data:www-data /var/moodledata

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]



