FROM debian:jessie

WORKDIR /tmp

RUN apt-get update -y && \
    apt-get install -y curl git && \
    curl -sL https://deb.nodesource.com/setup_0.12 | bash - && \
    apt-get install -y \
    nodejs \
    libnotify4 && \
    npm -g install npm@latest-2 && \
    apt-get remove --purge curl -y  && \
    apt-get clean

RUN npm install -g \
    bower \
    webpack \
    gulp

RUN addgroup --gid 1000 worker  \
 && adduser --disabled-login --gecos "" worker --uid=1000 --gid=1000

# For some strange reason Bower doesn't like running
# without a /var/www directory! Even if we're running
# it from a completely different directory! Strange!? 
RUN mkdir -p /data /var/www && \
    chown www-data:www-data /var/www

RUN chown worker /data
RUN mkdir /data/bower_components

VOLUME ["/data"]
WORKDIR /data

USER worker

