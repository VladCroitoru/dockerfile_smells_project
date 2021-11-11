FROM ubuntu:14.04

MAINTAINER Tyler Payne <tyler43636@gmail.com>

ENV VERSION 3.0.0

RUN mkdir -p /mattermost/data

# add supervisor file for application
ADD mattermost.conf /etc/supervisor/conf.d/
ADD config.template.json /

# add bash scripts
RUN mkdir /scripts
ADD scripts/*.sh /scripts/

# make executable and run bash scripts to install app
RUN chmod +x /scripts/*.sh && \
	/bin/bash /scripts/install.sh

# map /config to host defined config path (used to store configuration from app)
VOLUME /mattermost

EXPOSE 8065

# run script to set uid, gid and permissions
CMD ["/bin/bash", "/scripts/init.sh"]
