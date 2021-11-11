FROM python:3-onbuild
MAINTAINER Alexis Couronne

RUN apt-get update -y
RUN apt-get install -y locales

# Set the locale
RUN sed -i -e 's/# fr_FR.UTF-8 UTF-8/fr_FR.UTF-8 UTF-8/' /etc/locale.gen && \
    echo 'LANG="fr_FR.UTF-8"'>/etc/default/locale && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=fr_FR.UTF-8

ENV LANG fr_FR.UTF-8


RUN pelican content/ -o /var/www/blog/ -s pelicanconf.py

VOLUME ["/usr/src/app", "/var/www/blog"]
