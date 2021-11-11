FROM ubuntu:14.04

MAINTAINER Tyler Payne <tyler43636@gmail.com>

# add supervisor file for application
ADD plexpy.conf /etc/supervisor/conf.d/

# add bash scripts
RUN mkdir /scripts
ADD scripts/*.sh /scripts/

# make executable and run bash scripts to install app
RUN chmod +x /scripts/*.sh && \
	/bin/bash /scripts/install.sh

# map /config to host defined config path (used to store configuration from app)
VOLUME /config

# expose the default port for plexpy
EXPOSE 8181

# run script to set uid, gid and permissions
CMD ["/bin/bash", "/scripts/init.sh"]
