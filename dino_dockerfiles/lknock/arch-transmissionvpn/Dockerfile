FROM binhex/arch-openvpn

# additional files
##################

ADD setup/*.conf /etc/supervisor/conf.d/
ADD setup/root/*.sh /root/
ADD apps/root/*.sh /root/
ADD apps/nobody/*.sh /home/nobody/

# install app
#############

# make executable and run bash scripts to install app
RUN chmod +x /root/*.sh /home/nobody/*.sh && \
	/bin/bash /root/install.sh

# docker settings
#################

VOLUME ["/config"]
VOLUME ["/data"]

# expose port for transmission webui
EXPOSE 9091/tcp

# expose port for privoxy
EXPOSE 8118

# expose port for transmission incoming port (used only if VPN_ENABLED=no)
EXPOSE 51413
EXPOSE 51413/udp

# set permissions
#################

# run script to set uid, gid and permissions
CMD ["/bin/bash", "/root/init.sh"]
