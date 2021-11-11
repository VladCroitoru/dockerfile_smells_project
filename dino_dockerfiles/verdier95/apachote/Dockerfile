FROM debian:jessie
MAINTAINER someguy <verdier95@gmail.com>

RUN apt-get update
RUN apt-get -y install apache2
RUN apt-get clean

RUN rm -rf /var/lib/apt/lists/*

EXPOSE 80

ADD ["index.html", "/var/www/html/"]

ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
