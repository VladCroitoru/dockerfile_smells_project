FROM php:7.4-apache

RUN cd /etc/apache2/mods-enabled && \
    ln -s ../mods-available/rewrite.load

# Install required PHP extensions
# -- GD
RUN apt-get update
RUN apt-get install
RUN apt-get install
RUN apt-get clean

COPY 000-default.conf /etc/apache2/sites-available/