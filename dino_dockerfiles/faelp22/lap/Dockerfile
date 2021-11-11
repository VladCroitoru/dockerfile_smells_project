# Lap
#
# VERSION               0.4

FROM ubuntu:18.04
MAINTAINER Isael Sousa <faelp22@gmail.com>

#timezone
ENV TZ=America/Fortaleza
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install apache2 and php7.2.x
RUN apt-get update
RUN apt-get install php php-xml php-mysql php-mbstring php-curl apache2 apache2-bin libapache2-mod-php -y
RUN apt-get clean
RUN a2enmod rewrite
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*
RUN adduser --uid 1000 --gecos 'My Apache User' --disabled-password dev
RUN chmod -R 777 /var/www/html
RUN chown -R 1000:www-data /var/www/html
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf
COPY docker-entrypoint.sh /root/docker-entrypoint.sh
RUN chmod +x /root/docker-entrypoint.sh

# volumes
VOLUME ["/var/www/html"]

EXPOSE 80

ENTRYPOINT ["/root/docker-entrypoint.sh"]
