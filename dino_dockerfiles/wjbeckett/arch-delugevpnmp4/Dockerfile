FROM binhex/arch-openvpn
MAINTAINER binhex

# additional files
##################

# add supervisor conf file for app
ADD build/*.conf /etc/supervisor/conf.d/

# add bash scripts to install app
ADD build/root/*.sh /root/

# add bash script to setup iptables
ADD run/root/*.sh /root/

# add bash script to run deluge
ADD run/nobody/*.sh /home/nobody/

# add python script to configure deluge
ADD run/nobody/*.py /home/nobody/

# add pre-configured config files for deluge
ADD config/nobody/ /home/nobody/

# add startup file to update mp4automator at boot
ADD run/root/update.service /etc/systemd/system/

# add update script
ADD /run/init/update.sh /usr/bin/update.sh

# set permissions on update script
RUN chmod -v +x /usr/bin/update.sh

# enable update script service
RUN systemctl enable update.service

# install app
#############

# make executable and run bash scripts to install app
RUN chmod +x /root/*.sh /home/nobody/*.sh /home/nobody/*.py && \
	/bin/bash /root/install.sh

#Set mp4automator script file permissions
RUN chmod 775 -R /mp4automator

# docker settings
#################

# map /config to host defined config path (used to store configuration from app)
VOLUME /config

# map /downloads to host defined data path (used to store data from app)
VOLUME /downloads

# map /mp4automator to host defined mp4automator path (used to store mp4automator config)
VOLUME /mp4automator

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