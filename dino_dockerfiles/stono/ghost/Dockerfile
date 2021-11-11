FROM centos:7
MAINTAINER Karl Stoney <me@karlstoney.com>

# Get dependencies
RUN yum -y -q install curl wget gettext patch

# Get nodejs repos
RUN curl --silent --location https://rpm.nodesource.com/setup_12.x | bash -

RUN yum -y -q install nodejs-12.* gcc-c++ make git bzip2 unzip && \
    yum -y -q clean all

# Configuration
ENV GHOST_CONFIG /data/config.js
ENV GHOST_HOME /var/www/ghost
ENV GHOST_VERSION 3.35.0 

# Setup www-data user
RUN groupadd www-data && \
    useradd -r -g www-data www-data

RUN mkdir -p /var/www && \
    mkdir -p /home/www-data && \
    mkdir -p /data && \
    chown -R www-data:www-data /var/www && \
    chown -R www-data:www-data /home/www-data && \
    chown -R www-data:www-data /data

# Install Ghost
WORKDIR $GHOST_HOME
ENV GHOST_CLI_VERSION 1.14.1
RUN npm install -g ghost-cli@$GHOST_CLI_VERSION
RUN chown -R www-data:www-data $GHOST_HOME
USER www-data
RUN ghost install local --no-setup --db sqlite3
 
USER root

VOLUME /data

EXPOSE 2368

COPY run.sh /usr/local/bin/run.sh
CMD ["/usr/local/bin/run.sh"]

# Add static content generator
RUN npm install -g ghost-static-site-generator

RUN mkdir -p /usr/local/etc/ghost/patches
COPY patches/ /usr/local/etc/ghost/patches/
COPY data/config.json /var/www/ghost/current/config.production.json
