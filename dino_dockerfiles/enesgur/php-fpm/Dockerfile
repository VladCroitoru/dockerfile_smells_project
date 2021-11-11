FROM enesgur/php-fpm:7.3

MAINTAINER Enes Gür

# Install Packages
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install php7.3-dev gcc libpcre3-dev -y
RUN git clone https://github.com/phalcon/cphalcon --branch 3.4.x
RUN cd /cphalcon/build && ./install
RUN cp /cphalcon/build/php7/64bits/modules/phalcon.so $(php-config --extension-dir)
RUN echo "extension=phalcon.so" >> /etc/php/7.3/mods-available/phalcon.ini

# Enable PHP Extension Settings Before Run PHP-FPM
RUN phpenmod phalcon

# Remove Source Files.
RUN rm -rf /cphalcon

CMD ["supervisord"]
