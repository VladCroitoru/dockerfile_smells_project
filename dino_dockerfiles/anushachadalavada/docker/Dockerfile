FROM ubuntu:12.04
MAINTAINER Kimbro Staken version: 0.1
#RUN apt-get update && apt-get install -y apache2 && apt-get clean && rm -f /var/lib/apt/lists/*
ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /VAR/LOG/APACHE2
EXPOSE 80
CMD ["/usr/sbin/apche2","-D","FOREGROUND"] 
