FROM linuxconfig/lamp
MAINTAINER Lubos Rendek <web@linuxconfig.org>

# Install prerequisites 
RUN apt-get install -y wget

# Download Revive ad server 
RUN rm -fr /var/www/html/*
RUN cd /var/www/html/; wget -q -O- https://download.revive-adserver.com/revive-adserver-3.2.4.tar.gz | tar xz --strip 1 

# Create database
RUN service mysql start; mysqladmin -uadmin -ppass create revive

# Update file ownership
RUN chown -R www-data.www-data /var/www/html

# Allow ports
EXPOSE 80

CMD ["supervisord"]