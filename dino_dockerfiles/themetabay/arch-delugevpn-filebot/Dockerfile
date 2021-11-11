FROM binhex/arch-delugevpn
MAINTAINER themetabay

# additional files
##################

# add bash script to setup iptables
ADD run/root/*.sh /root/
ADD run/nobody/*.sh /home/nobody/

# install filebot
#############

# make executable and run bash scripts to install app
RUN chmod +x /home/nobody/*.sh /root/*.sh 
#&& /bin/bash /root/filebot-install.sh

# docker settings
#################

# map /config to host defined config path (used to store configuration from app)
VOLUME /config

# map /data to host defined data path (used to store data from app)
VOLUME /data

# expose port for deluge webui
EXPOSE 8112

# expose port for privoxy
EXPOSE 8118

# expose port for deluge daemon (used in conjunction with LAN_NETWORK env var)
EXPOSE 58846

# expose port for deluge incoming port (used only if VPN_ENABLED=no)
EXPOSE 58946
EXPOSE 58946/udp

# set permissions
#################

# run script to set uid, gid and permissions
CMD ["/bin/bash", "/root/init.sh"]
