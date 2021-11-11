# Dockerfile for thenets/phalcon:latest
#
# https://github.com/thenets/phalcon

FROM ubuntu:16.04

MAINTAINER Luiz Felipe F M Costa <luiz@thenets.org>

ENV USER_HOME=/home/phalcon/
ENV APP=/home/phalcon/html/

USER root

# Upgrade system
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y

# Install basic content
RUN apt-get install -y git curl wget nano htop && \
    apt-get autoclean

# =====================================
# Install Phalcon core
# =====================================

# Install Phalcon PHP module
RUN curl -s "https://packagecloud.io/install/repositories/phalcon/stable/script.deb.sh" | bash && \
    apt-get install -y php php-mysql php7.0-phalcon && \
    apt-get autoclean

# Create Phalcon user
RUN groupadd -r -g 1000 phalcon && \
    useradd -mr -c "Phalcon" -d $USER_HOME -g 1000 -u 1000 phalcon

# Create app dir and set permissions
RUN mkdir -p $APP && chown -R 1000.1000 $USER_HOME

# Create link for Phalcon CLI
RUN ln -s /home/phalcon/phalcon-devtools/phalcon.php /usr/bin/phalcon


# =====================================
# Install Phalcon CLI
# =====================================

# Change to Phalcon user
USER phalcon

# Install Phalcon CLI
RUN cd ~ && php --version && \
    git clone git://github.com/phalcon/phalcon-devtools.git && \
    cd phalcon-devtools/ && ./phalcon.sh

# Create hello world file
RUN echo "<?php echo 'Hello from PHP. You did\'t set a volume for your application.'; ?>" > $APP/index.php


# =====================================
# Install Apache
# =====================================
USER root
RUN apt-get install -y apache2 libapache2-mod-php php-mcrypt php-cli
ADD httpd.conf /home/phalcon/httpd.conf
RUN a2enmod rewrite && \
    adduser phalcon www-data && \
    chown 1000.1000 /home/phalcon/httpd.conf && \
    rm /etc/apache2/sites-available/000-default.conf && \
    ln -s /home/phalcon/httpd.conf /etc/apache2/sites-available/000-default.conf && \
    echo '' > /etc/apache2/ports.conf && \
    chmod 777 -R /var/log/apache2/ /var/lock/apache2/
USER phalcon

# Config and volume
WORKDIR $APP
CMD apachectl -e debug -DFOREGROUND
EXPOSE 8080
VOLUME [$APP]


