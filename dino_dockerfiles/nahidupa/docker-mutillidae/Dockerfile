FROM ubuntu:15.04
MAINTAINER nahidul kibria <nahidupa@gmail.com>

RUN apt-get update \
 && apt-get install -y apache2 apache2-utils \
 libapache2-mod-auth-mysql php5-mysql php5 \
 php-pear php5-gd php5-mcrypt php5-curl \
 unzip curl

COPY ./mutillidae-2.6.36.zip /tmp/mutillidae-2.6.36.zip
RUN cd /var/www/html && unzip /tmp/mutillidae-2.6.36.zip

COPY ./run.sh /run.sh

EXPOSE 80
CMD ["/bin/sh", "/run.sh"]
