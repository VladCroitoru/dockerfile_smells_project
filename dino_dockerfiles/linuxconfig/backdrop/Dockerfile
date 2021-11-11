FROM linuxconfig/lamp
MAINTAINER Lubos Rendek <web@linuxconfig.org>

# Install prerequisites 
RUN apt-get update
RUN apt-get install -y wget unzip

# Download and unzip Backdrop
RUN wget -qO /tmp/backdrop-1.1.3.zip https://github.com/backdrop/backdrop/archive/1.1.3.zip
RUN rm -fr /var/www/html
RUN unzip -d /tmp /tmp/backdrop-1.1.3.zip
RUN rm /tmp/backdrop-1.1.3.zip
RUN mv /tmp/backdrop-*/ /var/www/html

# Create database
RUN service mysql start; mysqladmin -uadmin -ppass create backdrop

# Apache configuration
ADD 000-default.conf /etc/apache2/sites-available/
RUN a2enmod rewrite


# Update file and directory ownership
RUN chown -R www-data.www-data /var/www/html

# Allow ports
EXPOSE 80

CMD ["supervisord"]
