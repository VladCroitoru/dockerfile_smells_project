FROM asteris/apache-php-mongo:latest

ENV MONGO_VERSION=3.2.10
ENV MONGO_PGP=3.4
ENV MONGO_PHP_VERSION=1.6.14
ENV TZ=Asia/Bangkok


# Set the timezone.
RUN echo $TZ > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata


RUN apt-get update && \
    apt-get -yq install \
    php5-mysql \
    xinetd \
    telnetd \
    openssl

RUN a2enmod ssl
RUN a2enmod headers
RUN a2enmod rewrite

VOLUME ["/var/www", "/etc/apache2/sites-enabled"]

EXPOSE 80 443

CMD ["/run.sh"]
