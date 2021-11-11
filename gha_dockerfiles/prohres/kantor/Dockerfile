###/
# Dockefile to build Docker Image of Apache WebServer running on Ubuntu
#
# Solovii Serhii 23/03/2019
###/
FROM ubuntu:18.04

# Install dependencies
RUN apt-get update
RUN apt-get -y install apache2

# Copy web in docker image
COPY . /var/www/html/
WORKDIR /var/www/html/

# Configure apache
RUN echo '. /etc/apache2/envvars' > /root/run_apache.sh
RUN echo 'mkdir -p /var/run/apache2' >> /root/run_apache.sh
RUN echo 'mkdir -p /var/lock/apache2' >> /root/run_apache.sh
RUN echo '/usr/sbin/apache2 -D FOREGROUND' >> /root/run_apache.sh
RUN chmod 755 /root/run_apache.sh

EXPOSE 80

CMD /root/run_apache.sh

