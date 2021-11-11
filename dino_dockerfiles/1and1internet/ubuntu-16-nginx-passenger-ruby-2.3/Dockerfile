FROM 1and1internet/ubuntu-16-nginx-passenger
MAINTAINER brian.wilkinson@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive


ENV GEM_HOME=/var/www/._gems

ENV GEM_PATH=$GEM_HOME \
    PATH=${GEM_HOME}/bin:$PATH

# TODO: Remove this line
ENV PASSENGER_APP_ENV development


RUN \
	apt-get update -q && \
	apt-get install -y curl gnupg build-essential ruby2.3-dev libsqlite3-dev nodejs && \
	ln -sf /usr/bin/nodejs /usr/local/bin/node && \
	sed -i -e 's|passenger_app_type wsgi|passenger_ruby /usr/bin/ruby2.3|' /etc/nginx/sites-enabled/default && \
	/usr/bin/passenger-config validate-install  --auto --no-colors && \
	apt-get -y clean && \
	rm -rf /var/lib/apt/lists/*

COPY src /usr/src
COPY files /
