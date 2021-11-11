# the debian wheezy image is needed to get apache 2.2 and because the httpd image doesn't provide a2enmod etc.
FROM debian:wheezy

MAINTAINER datingcafe.de <dev@datingcafe.de>

# Update repositories and install apache
# After that remove apt status information
RUN apt-get update && \
    apt-get install -y apache2 libapache2-mod-jk

# configure env variables for apache
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2

# enable apache modules
RUN a2enmod rewrite \
            proxy \
            proxy_ajp \
            headers \
            jk

EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
