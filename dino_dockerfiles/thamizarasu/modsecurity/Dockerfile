# Dockerfile for Modsecurity
FROM ubuntu:latest
MAINTAINER Sankara Shunmugasundaram <sankara.shunmuga@appdirect.com>

# Update packages
RUN apt-get update -y

RUN apt-get install -y apache2 libapache2-mod-security2 supervisor
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/supervisor

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN a2enmod security2
RUN service apache2 restart

EXPOSE 80
CMD ["/usr/bin/supervisord"]