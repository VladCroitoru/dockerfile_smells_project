FROM linuxserver/baseimage

# Install Depends
RUN add-apt-repository ppa:transmissionbt/ppa && \
apt-get update -q && \
apt-get install -y transmission-cli transmission-common transmission-daemon openvpn curl && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

#Mappings and Ports
EXPOSE 9091
VOLUME /config
VOLUME /downloads

#Adding Custom files
ADD init/ /etc/my_init.d/
RUN chmod -v +x /etc/my_init.d/*.sh
