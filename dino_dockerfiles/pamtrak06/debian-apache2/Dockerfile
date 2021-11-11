FROM debian:wheezy

MAINTAINER pamtrak06 <pamtrak06@gmail.com>

# Update os & install Apache
RUN apt-get update && apt-get install -y \
	openssh-server \
	apache2 \
	apache2-threaded-dev

# Set Apache environment variables
#RUN source /etc/apache2/envvars

# Configure localhost in Apache
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

# Volumes
VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2"]

# Expose ports
EXPOSE 22 80 443

# Define default command
CMD ["apachectl", "-D", "FOREGROUND"]
