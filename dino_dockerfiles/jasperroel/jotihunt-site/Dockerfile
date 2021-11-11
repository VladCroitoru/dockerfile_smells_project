FROM nimmis/apache-php7

MAINTAINER Jasper Roel <jasperroel@gmail.com>

# Update aptitude, install git
RUN apt-get update && apt-get install -y git

## Setup apache
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
RUN a2enmod rewrite

# Make sure we can log apache
RUN ln -sf /dev/stdout /var/log/apache2/access.log 
RUN ln -sf /dev/stderr /var/log/apache2/error.log

WORKDIR /var/www
RUN git clone https://github.com/roothaan/jotihunt-site.git

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

EXPOSE 80
EXPOSE 443
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
