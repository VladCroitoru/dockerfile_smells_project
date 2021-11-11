# Base system is the LTS version of Ubuntu.
FROM   ubuntu:14.04


# Make sure we don't get notifications we can't answer during building.
ENV    DEBIAN_FRONTEND noninteractive


# Download and install everything from the repos.
RUN    apt-get --yes update; apt-get --yes upgrade; apt-get --yes install software-properties-common

# Java
RUN    apt-add-repository --yes ppa:webupd8team/java; apt-get --yes update
RUN    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections  && \
       echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections  && \
       apt-get --yes install curl oracle-java8-installer unzip wget screen

# NGINX
RUN    apt-get --yes install nginx php5-fpm php5-gd

ADD    nginx/default /etc/nginx/sites-available/default

# MCHostPanel
RUN    apt-get --yes install git
RUN    rm -rf /usr/share/nginx/html && \
       git clone https://github.com/JRogaishio/MCHostPanel /usr/share/nginx/html && \
       mkdir /data && \
       chown -R www-data:www-data /usr/share/nginx/html && \
       chown -R www-data:www-data /data && \
       service nginx restart

# Load in all of our config files.
ADD    ./scripts/start /start


# Fix all permissions
RUN    chmod +x /start


ENV VIRTUAL_HOST localhost
ENV VIRTUAL_PORT 80

# 80 for Webserver
EXPOSE 80

# 25565 is for minecraft
EXPOSE 25565

# /data contains Minecraft server
VOLUME ["/data"]

# /start runs it.
CMD    ["/start"]