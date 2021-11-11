FROM phusion/baseimage:0.9.16

MAINTAINER Leone Parise <leone.parise@gmail.com>

# Environment variables
ENV VERSION 15.08

ENV DIR /opt/countly

ENV INSIDE_DOCKER 1

# Install base packages
RUN apt-get update && apt-get install -y python-software-properties wget g++ software-properties-common unzip

# Install NodeJs and other packages
RUN wget -qO- https://deb.nodesource.com/setup | bash - && \ 
	apt-get install -y nginx nodejs supervisor imagemagick sendmail && \
	apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Countly
RUN cd /tmp && \
	wget https://github.com/Countly/countly-server/releases/download/$VERSION/countly-community-edition-v$VERSION.zip && \
	unzip countly-community-edition-v$VERSION.zip -d /opt

# Load default configurations
RUN cp $DIR/bin/config/nginx.server.conf /etc/nginx/sites-enabled/default &&\
	cp $DIR/bin/config/nginx.conf /etc/nginx/nginx.conf && \
	echo "" >> /etc/nginx/nginx.conf && \
    echo "daemon off;" >> /etc/nginx/nginx.conf && \
	cp $DIR/api/config.sample.js $DIR/api/config.js && \
	touch $DIR/plugins/plugins.json && echo '["plugins","density","locale","enterpriseinfo","push"]' > $DIR/plugins/plugins.json && \
	cp $DIR/frontend/express/config.sample.js $DIR/frontend/express/config.js && \
	cp $DIR/frontend/express/public/javascripts/countly/countly.config.sample.js $DIR/frontend/express/public/javascripts/countly/countly.config.js

# Install plugins
RUN cd $DIR && \
	npm install -g grunt-cli --unsafe-perm && npm install && \
	node $DIR/bin/scripts/install_plugins.js && \
	grunt dist-all

# Add countly services
RUN mkdir -p /etc/service/nginx && \
    mkdir -p /etc/service/countly-api && \
    mkdir -p /etc/service/countly-dashboard && \
    cp $DIR/bin/commands/docker/nginx.sh /etc/service/nginx/run && \
    cp $DIR/bin/commands/docker/countly-api.sh /etc/service/countly-api/run && \
    cp $DIR/bin/commands/docker/countly-dashboard.sh /etc/service/countly-dashboard/run && \
	bash $DIR/bin/scripts/detect.init.sh

# Add user countly
RUN useradd -r -M -U -d /opt/countly -s /bin/false countly && \
	echo "countly ALL=(ALL) NOPASSWD: /usr/bin/sv restart countly-api countly-dashboard" >> /etc/sudoers.d/countly && \
	chown -R countly:countly $DIR

# Copy entrypoint files
COPY ./entrypoint.sh /
COPY ./_config.api.js /
COPY ./_config.frontend.js /

ENTRYPOINT ["/entrypoint.sh"]

# Expose port 80
EXPOSE 80
