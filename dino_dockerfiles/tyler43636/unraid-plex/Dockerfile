FROM ubuntu:14.04

MAINTAINER Tyler Payne <tyler43636@gmail.com>

ENV VERSION 1.5.6.3790-4613ce077

# add supervisor file for application
ADD plexmediaserver.conf /etc/supervisor/conf.d/

# add bash scripts
RUN mkdir /scripts
ADD scripts/*.sh /scripts/

# make executable and run bash scripts to install app
RUN chmod +x /scripts/*.sh && \
	/bin/bash /scripts/install.sh

# map /config to host defined config path (used to store configuration from app)
VOLUME /config

# map /media to host defined media path (used to read/write to media library)
VOLUME /media

# run script to set uid, gid and permissions
CMD ["/bin/bash", "/scripts/init.sh"]
