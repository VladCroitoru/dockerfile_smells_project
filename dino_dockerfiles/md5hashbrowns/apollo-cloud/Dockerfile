############################################################
# Dockerfile to build Apollo Cloud
############################################################

# Set the base image
FROM debian:latest

# Original author is Carlos Tighe
MAINTAINER MD5HashBrowns

# Install packages
RUN apt-get update && apt-get install -y apache2 \
    libapache2-mod-wsgi \
    build-essential \
    python \
    python-dev\
    python-pip \
    nano \
    libav-tools \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

# Copy over and install the requirements
COPY ./app/requirements.txt /var/www/apollo-cloud/app/requirements.txt
RUN pip install -r /var/www/apollo-cloud/app/requirements.txt
RUN pip install -U youtube-dl

# Copy over the apache configuration file and enable the site
COPY ./apollo-cloud.conf /etc/apache2/sites-available/apollo-cloud.conf
RUN a2ensite apollo-cloud
RUN a2enmod headers

# Copy over the wsgi file
COPY ./apollo-cloud.wsgi /var/www/apollo-cloud/apollo-cloud.wsgi

COPY ./run.py /var/www/apollo-cloud/run.py
COPY ./app /var/www/apollo-cloud/app/

RUN a2dissite 000-default.conf
RUN a2ensite apollo-cloud.conf


# Set permissions for the static directory
RUN chmod -R 777 /var/www/apollo-cloud/app/static/  

EXPOSE 80

WORKDIR /var/www/apollo-cloud

# CMD ["/bin/bash"]
CMD  /usr/sbin/apache2ctl -D FOREGROUND
# The commands below get apache running but there are issues accessing it online
# The port is only available if you go to another port first
# ENTRYPOINT ["/sbin/init"]
# CMD ["/usr/sbin/apache2ctl"]
