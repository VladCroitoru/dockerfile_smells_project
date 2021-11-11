FROM jbbodart/arch-base
MAINTAINER jbbodart

# additional files
##################

# add supervisor conf file for app
ADD *.conf /etc/supervisor.d/

# add bash scripts to install app, and setup iptables, routing etc
ADD *.sh /root/

# add bash script to run rtorrent
ADD apps/nobody/*.sh /home/nobody/

# add bash script to run sshd
ADD apps/root/*.sh /root/

# add default config directory
ADD config /home/nobody/config

# install app
#############

# make executable and run bash scripts to install app
RUN chmod +x /root/*.sh /home/nobody/*.sh && \
	/bin/bash /root/install.sh

# docker settings
#################

# map /config to host defined config path (used to store configuration from app)
VOLUME /config
# map /data to host defined data path (used to store data from app)
VOLUME /data

# expose port for rutorrent
EXPOSE 8080
# expose port for privoxy
EXPOSE 8118

# run supervisor
################

# run supervisor
CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]
